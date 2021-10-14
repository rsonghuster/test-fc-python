# -*- coding: utf-8 -*-
import fastapi


def handler(environ, start_response):
    print(fastapi.__version__)
    return "ok"
