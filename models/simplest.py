from typing import Optional

from models.base import ExtendedBaseModel

__all__ = ['SimplestModel']


class SimplestModel(ExtendedBaseModel):
    id: int
    name: str
    array: Optional[list]
    object: Optional[dict]
