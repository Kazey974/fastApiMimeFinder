from fastapi import FastAPI, Request
from starlette.datastructures import UploadFile
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from analyze import analyze_content
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static", html=True, follow_symlink=True), name="static")

@app.get("/", include_in_schema=False)
def index():
    return FileResponse("app/static/index.html")

@app.post("/mime-type", tags=["Files"], status_code=200)
async def get_mime_type(request: Request):
    """
    Get mimetype of files passed through forms or curl
    """
    async with request.form() as form:
        return {
            file[1].filename: await analyze_content(file[1])
            for file in form.multi_items()
            if isinstance(file[1], UploadFile)
        }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="8080")