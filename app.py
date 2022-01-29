# TODO global.
#  1) Запихонить все в докер или на хероку
#  2) Сделать простой спопоб "загрузить" json и его получать по имени файла https://fastapi.tiangolo.com/tutorial/path-params/#path-convertor

from __future__ import annotations

from fastapi import FastAPI, HTTPException

from models import SimplestModel

app = FastAPI()


# TODO fix documentation
@app.get("/simplest/{file_name}")
def simplest(file_name: str) -> SimplestModel.schema():
    try:
        return SimplestModel.from_json_file(file_name).dict()
    except FileNotFoundError as ex:
        raise HTTPException(status_code=404,
                            detail={"error": f"File {file_name}.json not found", "full_path": ex.filename})


@app.get("/")
async def read_root():
    hide_urls = {'/openapi.json', '/docs/oauth2-redirect', '/'}
    doc_urls = {'/docs', '/redoc'}
    a = app
    return {
        "url_list": f"{[route.path for route in app.router.routes if route.path not in hide_urls | doc_urls]}",
        "docs": doc_urls
    }
