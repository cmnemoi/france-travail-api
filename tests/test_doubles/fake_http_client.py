from france_travail_api.http_transport._http_response import HTTPResponse


class FakeHttpClient:
    def __init__(self) -> None:
        self.responses: list[HTTPResponse] = []

    def add_response(self, response: HTTPResponse) -> None:
        self.responses.append(response)

    def get(self, url: str, headers: dict[str, str] | None = None) -> HTTPResponse:
        return self.responses.pop(0)

    def post(self, url: str, payload: dict[str, str], headers: dict[str, str] | None = None) -> HTTPResponse:
        return self.responses.pop(0)
