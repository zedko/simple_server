import functools
from pathlib import Path

from pydantic import BaseModel

from settings import JSON_FILES_PATH


class ExtendedBaseModel(BaseModel):
    @classmethod
    def get_files_folder(cls) -> Path:
        return JSON_FILES_PATH / cls.__name__

    class Config:
        arbitrary_types_allowed = True
        keep_untouched = (property, functools.cached_property)

