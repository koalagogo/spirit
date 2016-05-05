# -*- coding: utf-8 -*-
import pytest

from spirit.app import Application
from spirit.config import load_config


@pytest.fixture
def app():
    return Application(load_config('development'))


@pytest.mark.gen_test
def test_index(http_client, base_url):
    response = yield http_client.fetch(base_url)
    assert response.code == 200
