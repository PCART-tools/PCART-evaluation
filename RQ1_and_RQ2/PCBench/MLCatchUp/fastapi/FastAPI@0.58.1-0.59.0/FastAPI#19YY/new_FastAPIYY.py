from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(openapi_prefix='', root_path_in_servers=True)
