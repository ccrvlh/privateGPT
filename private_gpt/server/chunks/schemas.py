from pydantic import BaseModel, Field

from private_gpt.open_ai.context_filter import ContextFilter
from private_gpt.server.ingest.schemas import IngestedDoc


class Chunk(BaseModel):
    object: str = Field(enum=["context.chunk"])
    score: float = Field(examples=[0.023])
    document: IngestedDoc
    text: str = Field(examples=["Outbound sales increased 20%, driven by new leads."])
    previous_texts: list[str] | None = Field(
        examples=[["SALES REPORT 2023", "Inbound didn't show major changes."]]
    )
    next_texts: list[str] | None = Field(
        examples=[
            [
                "New leads came from Google Ads campaign.",
                "The campaign was run by the Marketing Department",
            ]
        ]
    )


class ChunksBody(BaseModel):
    text: str = Field(examples=["Q3 2023 sales"])
    context_filter: ContextFilter | None = None
    limit: int = 10
    prev_next_chunks: int = Field(default=0, examples=[2])


class ChunksResponse(BaseModel):
    object: str = Field(enum=["list"])
    model: str = Field(enum=["private-gpt"])
    data: list[Chunk]

