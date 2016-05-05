# -*- coding: utf-8 -*-
import pytest

from spirit.config import load_config
from spirit.app import Application


@pytest.fixture
def app():
    return Application(load_config('testing'))
