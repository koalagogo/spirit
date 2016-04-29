# -*- coding: utf-8 -*-
from .controllers import site


routers = [
    (r"/", site.IndexHandler)
]
