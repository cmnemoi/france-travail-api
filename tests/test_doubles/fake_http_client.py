import http
import uuid
from typing import Any

from france_travail_api.http_transport._http_response import HTTPResponse


class FakeHttpClient:
    def __init__(self) -> None:
        self.responses: list[HTTPResponse] = []
        self.last_get_url: str | None = None
        self.last_post_url: str | None = None

    def add_response(self, response: HTTPResponse) -> None:
        self.responses.append(response)

    def add_json_response(self, body: Any, status_code: http.HTTPStatus = http.HTTPStatus.OK) -> None:
        self.add_response(
            HTTPResponse(
                status_code=status_code,
                body=body,
                headers={},
                request_id=uuid.uuid4(),
            )
        )

    def get(self, url: str, headers: dict[str, str] | None = None) -> HTTPResponse:
        self.last_get_url = url
        return self.responses.pop(0)

    async def get_async(self, url: str, headers: dict[str, str] | None = None) -> HTTPResponse:
        self.last_get_url = url
        return self.responses.pop(0)

    def post(self, url: str, payload: dict[str, str], headers: dict[str, str] | None = None) -> HTTPResponse:
        self.last_post_url = url
        return self.responses.pop(0)

    async def post_async(
        self, url: str, payload: dict[str, str], headers: dict[str, str] | None = None
    ) -> HTTPResponse:
        self.last_post_url = url
        return self.responses.pop(0)
