from __future__ import annotations

from fastapi import FastAPI

from models import SimplestModel

app = FastAPI()


# TODO use proper http error for the exception
@app.get("/simplest/{file_name}")
def simplest(file_name: str) -> dict | SimplestModel.schema_json():
    try:
        return SimplestModel.from_json_file(file_name).dict()
    except FileNotFoundError as ex:
        return {"error": f"File {file_name}.json not found",
                "full_path": ex.filename}


@app.get("/")
async def read_root():
    hide_urls = {'/openapi.json', '/docs/oauth2-redirect', '/'}
    doc_urls = {'/docs', '/redoc'}
    a = app
    return {
        "url_list": f"{[route.path for route in app.router.routes if route.path not in hide_urls | doc_urls]}",
        "docs": doc_urls
    }
