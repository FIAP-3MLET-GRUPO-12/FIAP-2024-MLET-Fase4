import time
from typing import Callable
from fastapi import Request, Response
import logging
from pythonjsonlogger import jsonlogger

# Configure JSON logger
logger = logging.getLogger("api_logger")
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter(
    fmt="%(asctime)s %(levelname)s %(name)s %(request_id)s %(url)s %(method)s %(status_code)s %(response_time)s"
)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

async def logging_middleware(request: Request, call_next: Callable) -> Response:
    """Middleware to log request/response details and timing."""
    start_time = time.time()
    
    # Generate request ID
    request_id = request.headers.get("X-Request-ID", str(time.time()))
    
    # Process the request
    response = await call_next(request)
    
    # Calculate timing
    process_time = time.time() - start_time
    
    # Log the request details
    logger.info(
        "Request processed",
        extra={
            "request_id": request_id,
            "url": str(request.url),
            "method": request.method,
            "status_code": response.status_code,
            "response_time": f"{process_time:.3f}s"
        }
    )
    
    # Add timing header to response
    response.headers["X-Process-Time"] = str(process_time)
    response.headers["X-Request-ID"] = request_id
    
    return response 