from fastapi import APIRouter
from starlette.responses import StreamingResponse

from private_gpt.open_ai.models import OpenAICompletion, OpenAIMessage
from private_gpt.server.chat.router import ChatBody, chat_completion
from private_gpt.server.completions.schemas import CompletionsBody

completions_router = APIRouter(prefix="/v1")


@completions_router.post(
    "/completions",
    response_model=None,
    summary="Completion",
    responses={200: {"model": OpenAICompletion}},
    tags=["Contextual Completions"],
)
def prompt_completion(body: CompletionsBody) -> OpenAICompletion | StreamingResponse:
    """We recommend most users use our Chat completions API.

    Given a prompt, the model will return one predicted completion. If `use_context`
    is set to `true`, the model will use context coming from the ingested documents
    to create the response. The documents being used can be filtered using the
    `context_filter` and passing the document IDs to be used. Ingested documents IDs
    can be found using `/ingest/list` endpoint. If you want all ingested documents to
    be used, remove `context_filter` altogether.

    When using `'stream': true`, the API will return data chunks following [OpenAI's
    streaming model](https://platform.openai.com/docs/api-reference/chat/streaming):
    ```
    {"id":"12345","object":"completion.chunk","created":1694268190,
    "model":"private-gpt","choices":[{"index":0,"delta":{"content":"Hello"},
    "finish_reason":null}]}
    ```
    """
    message = OpenAIMessage(content=body.prompt, role="user")
    chat_body = ChatBody(
        messages=[message],
        use_context=body.use_context,
        stream=body.stream,
        context_filter=body.context_filter,
    )
    return chat_completion(chat_body)
