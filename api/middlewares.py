import logging
from http.client import HTTPException
from typing import Any

import ujson
from aiohttp.web_middlewares import middleware
from aiohttp.web_response import Response


@middleware
async def catch_exceptions(request: Any, handler: Any) -> Response:
    """Отправить error_response на любое исключение в обработчике запроса.

    Returns:
        Ответ перехваченного запроса.
    """
    try:
        resp = await handler(request)
    except HTTPException as exc:
        logging.error(
            "HTTPException error -- {0}: {1}.".format(
                type(exc),
                exc,
            ),
        )
        return Response(status=400, text=str(exc))
    except Exception as exc:  # pylint: disable=broad-except
        logging.error("Unexpected Error -- {0}: {1}".format(type(exc), exc), exc_info=True)
        return Response(status=500, text=str(exc))
    return resp
