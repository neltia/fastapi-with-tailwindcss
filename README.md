# FastAPI + TailwindCSS

## Getting Started

### Installation
**virtualenv**
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

**FastAPI**

```
pip install fastapi
```

**Uvicorn**

```
pip install uvicorn
```

**FastAPI-TailwindCSS Lib**
refer.
- https://tailwindcss.com/
- https://pypi.org/project/fastapi-tailwind/
```
pip install fastapi-tailwind
```

### tailwind config
Make sure the static folder exists.
```
mkdir ./static
```

Get output.css (test)
```
python main.py dev
```

Generate tailwind.config.js, then configure it appropriately.
refer.
- https://tailwindcss.com/docs/configuration
```
fastapi-tailwind-init
```

tailwind.config.js path: root & html in same path
```js
module.exports = {
  content: ["*.html"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

tailwind.config.js path: ./tailwindcss & html in templates
```js
module.exports = {
  content: "../templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Get appyled tailwind css in app
```
python main.py dev
```

### Refer.
lifespan -> `npx tailwindcss -i ./styles/app.css -o ../static/output.css --watch`
```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    process = tailwind.compile(static_files.directory + "/output.css")

    yield

    process.terminate()

app = FastAPI(
    lifespan=lifespan
)
```