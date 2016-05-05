# -*- coding: utf-8 -*-
import pytest


@pytest.mark.usefixtures('app')
@pytest.mark.gen_test
def test_index(http_client, base_url):
    response = yield http_client.fetch(base_url)
    assert response.code == 200
