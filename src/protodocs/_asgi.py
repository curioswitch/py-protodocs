import json
from collections.abc import Awaitable, Callable, Iterable, Mapping
from pathlib import Path

from google.protobuf.message import Message
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from ._jsonschema import generate_json_schema
from ._proto_specification import generate_proto_specification


class EncodingMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        orig_path: str = request.scope["path"]
        if orig_path.endswith((".ttf", ".png")):
            return await call_next(request)
        path = orig_path
        if (root_path := request.scope["root_path"]) and path.startswith(root_path):
            path = path[len(root_path) :]
        if path == "/":
            path = "/index.html"
        request.scope["path"] = f"{path}.gz"
        try:
            response = await call_next(request)
        finally:
            # We restore path mostly for request loggers.
            request.scope["path"] = orig_path
        response.headers["Content-Encoding"] = "gzip"
        return response


def protodocs_app(
    services: Iterable[str] | str,
    serialized_descriptors: bytes | None = None,
    example_requests: Mapping[str, Iterable[Message]] | None = None,
    injected_script_suppliers: Iterable[Callable[[], str]] | Callable[[], str] = (),
) -> Starlette:
    # Allow passing in singletons for convenience
    if isinstance(services, str):
        services = [services]
    if isinstance(injected_script_suppliers, Callable):
        injected_script_suppliers = [injected_script_suppliers]

    services = [s if not s.startswith("/") else s[1:] for s in services]
    spec = generate_proto_specification(
        services, serialized_descriptors, example_requests
    )
    spec_json = json.dumps(spec.to_json())

    jsonschema = generate_json_schema(spec)
    jsonschema_json = json.dumps([s.to_json() for s in jsonschema])

    def serve_spec(_request: Request) -> Response:
        return Response(
            content=spec_json,
            headers={"Content-Type": "application/json; charset=utf-8"},
        )

    def serve_schemas(_request: Request) -> Response:
        return Response(
            content=jsonschema_json,
            headers={"Content-Type": "application/json; charset=utf-8"},
        )

    def serve_versions(_request: Request) -> Response:
        # TODO: Consider allowing users to provide this.
        return Response(
            content="[]", headers={"Content-Type": "application/json; charset=utf-8"}
        )

    def serve_injected(_request: Request) -> Response:
        content = "\n".join(supplier() for supplier in injected_script_suppliers)
        return Response(
            content=content,
            headers={"Content-Type": "application/javascript; charset=utf-8"},
        )

    return Starlette(
        routes=[
            Route("/specification.json", serve_spec),
            Route("/schemas.json", serve_schemas),
            Route("/versions.json", serve_versions),
            Route("/injected.js", serve_injected),
            Mount(
                "/",
                StaticFiles(directory=Path(__file__).parent / "docsclient"),
                middleware=[Middleware(EncodingMiddleware)],
            ),
        ]
    )
