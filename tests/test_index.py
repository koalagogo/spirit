# -*- coding: utf-8 -*-
import pytest

from . import app  # noqa


@pytest.mark.gen_test
def test_index(http_client, base_url):
    response = yield http_client.fetch(base_url)
    assert response.code == 200
