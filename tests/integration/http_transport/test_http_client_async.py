import http

import httpx
import pytest

from france_travail_api.http_transport._http_client import HttpClient


@pytest.mark.integration
@pytest.mark.asyncio
async def test_http_client_get_async_returns_response() -> None:
    async with HttpClient() as client:
        response = await client.get_async("https://jsonplaceholder.typicode.com/todos/1")

        assert response.status_code == http.HTTPStatus.OK
        assert response.body == {"id": 1, "userId": 1, "title": "delectus aut autem", "completed": False}


@pytest.mark.integration
@pytest.mark.asyncio
async def test_http_client_get_async_includes_request_id() -> None:
    async with HttpClient() as client:
        response = await client.get_async("https://jsonplaceholder.typicode.com/todos/1")

        import uuid

        assert uuid.UUID(str(response.request_id))


@pytest.mark.integration
@pytest.mark.asyncio
async def test_http_client_get_async_with_custom_headers() -> None:
    async with HttpClient() as client:
        response = await client.get_async("https://httpbin.org/headers", headers={"X-Custom-Header": "test-value"})

        assert response.body["headers"]["Host"] == "httpbin.org"
        assert response.body["headers"]["X-Custom-Header"] == "test-value"


@pytest.mark.integration
@pytest.mark.asyncio
async def test_http_client_close_without_context_manager() -> None:
    client = HttpClient()
    await client.close_async()
    with pytest.raises(RuntimeError):
        await client.get_async("https://jsonplaceholder.typicode.com/todos/1")


@pytest.mark.integration
@pytest.mark.asyncio
async def test_http_client_respects_timeout() -> None:
    async with HttpClient(timeout=10**-2) as client:
        with pytest.raises(httpx.TimeoutException):
            await client.get_async("https://httpbin.org/delay/1")


@pytest.mark.integration
@pytest.mark.asyncio
async def test_http_client_post_returns_response() -> None:
    async with HttpClient() as client:
        response = await client.post_async(
            "https://jsonplaceholder.typicode.com/todos",
            payload={"title": "test", "completed": False, "userId": 1},
        )

        assert response.status_code == http.HTTPStatus.CREATED
        assert response.body["title"] == "test"
