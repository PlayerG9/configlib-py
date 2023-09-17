#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from ..exceptions import NotSupportedError
from ..loader import register_loader
from .json_loader import ReturnType
try:
    import json5
except ModuleNotFoundError:
    raise NotSupportedError('please install config-library[json5] for this')


@register_loader('json5')
def load_json5(self) -> ReturnType:
    with open(self.fp, 'r') as file:
        return json5.load(file)
