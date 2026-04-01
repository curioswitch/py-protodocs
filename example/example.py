from pathlib import Path

from connectrpc.request import RequestContext
from starlette.applications import Starlette
from starlette.routing import Mount

from protodocs import protodocs_app

from .greet_connect import GreetService, GreetServiceASGIApplication
from .greet_pb2 import Greeting, GreetingRequest, GreetingResponse


class ExampleGreetService(GreetService):
    async def greet(
        self, request: GreetingRequest, ctx: RequestContext
    ) -> GreetingResponse:
        response = "Who are you?"
        match request.greeting.WhichOneof("name"):
            case "nickname":
                response = f"Hello there, {request.greeting.nickname}"
            case "full_name":
                response = f"Hello there, {request.greeting.full_name.first_name} {request.greeting.full_name.last_name}"
            case "known_name":
                match request.greeting.known_name:
                    case Greeting.KnownName.BOB:
                        response = "Hello there, Bob"
                    case Greeting.KnownName.ALICE:
                        response = "Hello there, Alice"
        return GreetingResponse(result=response)


greeting_app = GreetServiceASGIApplication(ExampleGreetService())

descriptors = (Path(__file__).parent / "descriptorset.pb").read_bytes()
docs_app = protodocs_app(
    services=greeting_app.path,
    serialized_descriptors=descriptors,
    example_requests={
        f"{greeting_app.path}/Greet": [
            GreetingRequest(greeting=Greeting(nickname="Choko")),
            GreetingRequest(
                greeting=Greeting(
                    full_name=Greeting.FullName(first_name="Choko", last_name="Switch")
                )
            ),
            GreetingRequest(greeting=Greeting(known_name=Greeting.KnownName.BOB)),
        ]
    },
)


app = Starlette(
    routes=[Mount(greeting_app.path, greeting_app), Mount("/internal/docs", docs_app)]
)
