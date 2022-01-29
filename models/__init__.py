from __future__ import annotations

from typing import TYPE_CHECKING, Type

from .simplest import *


if TYPE_CHECKING:
    from .base import ExtendedBaseModel

MODELS_WITH_SCHEMAS: list[Type[ExtendedBaseModel]] = [
    simplest.SimplestModel,
]
