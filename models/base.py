from __future__ import annotations

import functools
import json
from pathlib import Path

from pydantic import BaseModel

from settings import JSON_FILES_PATH


class ExtendedBaseModel(BaseModel):
    @classmethod
    def get_files_folder(cls) -> Path:
        modified_name = cls.__name__.lower().removesuffix('model')
        return JSON_FILES_PATH / modified_name

    @classmethod
    def from_json_file(cls, file_name: str) -> ExtendedBaseModel:
        if not file_name.endswith('.json'):
            file_name += '.json'

        with open(cls.get_files_folder() / file_name) as file:
            loaded_dict: dict = json.load(file)
            # noinspection PyArgumentList
            return cls(**loaded_dict)

    class Config:
        arbitrary_types_allowed = True
        keep_untouched = (property, functools.cached_property)

