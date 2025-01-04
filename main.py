import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi_tailwind import tailwind
from contextlib import asynccontextmanager

static_files = StaticFiles(directory="static")


# lifespan:
#  Because this code is executed before the application starts taking requests,
#  and right after it finishes handling requests, it covers the whole application lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # our tailwind get's compiled here!
    process = tailwind.compile(static_files.directory + "/output.css")

    yield  # code after this is called on shutdown

    process.terminate()  # We must terminate the compiler on shutdown to
    # prevent multiple compilers running in development mode or when watch is enabled.


app = FastAPI(
    lifespan=lifespan
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", static_files, name="static")


# tailwind css sample
@app.get("/")
async def index_page():
    return FileResponse("index.html")


# apply template
@app.get("/list")
async def list_page(request: Request):
    return templates.TemplateResponse(name="list.html", request=request, )


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0")
