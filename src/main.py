from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi import Request
from starlette.responses import JSONResponse
from routes import movie_router

app = FastAPI(
    title="Movies homework",
    description="Description of project"
)

@app.exception_handler(RequestValidationError)
async def schema_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(str(exc), status_code=400)

api_version_prefix = "/api/v1"

app.include_router(movie_router, prefix=f"{api_version_prefix}/theater", tags=["theater"])
