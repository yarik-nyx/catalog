from fastapi import FastAPI, Request, status, Response
from fastapi.responses import ORJSONResponse
from pydantic import ValidationError
from fastapi.exceptions import ResponseValidationError
from sqlalchemy.exc import DatabaseError
from core.utils.logger import logger as log



def register_errors_handlers(app: FastAPI) -> None:
    
    @app.exception_handler(ValidationError)
    def handle_pydantic_validation_error(
        request: Request,
        exc: ValidationError
    ) -> ORJSONResponse:
        return ORJSONResponse(
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
            content = {
                "message": "Unhandled error",
                "error": exc.errors(),
            }
        )
    
    @app.exception_handler(ResponseValidationError)
    def handle_pydantic_resp_validation_error(
        request: Request,
        exc: ResponseValidationError
    ) -> ORJSONResponse:
        errors = []
        for error in exc.errors():
            errors.append({
                "field": "->".join(str(loc) for loc in error["loc"]),
                "message": error["msg"],
                "type": error["type"]
            })
        return ORJSONResponse(
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
            content = {
                "message": "Unhandled error",
                "error": errors,
            }
        )
    
    @app.exception_handler(DatabaseError)
    def handle_db_error(
        request: Request,
        exc: DatabaseError
    ) -> ORJSONResponse:
        log.error("Unhandled database error", exc_info = exc)
        return ORJSONResponse(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            content = {
                "message": "An unexpected error has occured."
            }
        )

    