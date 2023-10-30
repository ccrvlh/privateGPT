from pydantic import BaseModel

from private_gpt.open_ai.context_filter import ContextFilter


class CompletionsBody(BaseModel):
    prompt: str
    use_context: bool = False
    context_filter: ContextFilter | None = None
    stream: bool = False

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "prompt": "How do you fry an egg?",
                    "stream": False,
                    "use_context": False,
                }
            ]
        }
    }