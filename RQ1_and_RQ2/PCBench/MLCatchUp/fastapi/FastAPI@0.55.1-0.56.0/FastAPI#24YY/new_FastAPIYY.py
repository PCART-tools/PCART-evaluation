from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(default_response_class=JSONResponse, version='0.1.0', openapi_prefix='', debug=False, title='FastAPI', routes=None, openapi_url='/openapi.json', description='', root_path='')
