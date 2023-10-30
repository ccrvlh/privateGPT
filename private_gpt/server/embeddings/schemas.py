from pydantic import BaseModel, Field


class Embedding(BaseModel):
    index: int
    object: str = Field(enum=["embedding"])
    embedding: list[float] = Field(examples=[[0.0023064255, -0.009327292]])


class EmbeddingsBody(BaseModel):
    input: str | list[str]


class EmbeddingsResponse(BaseModel):
    object: str = Field(enum=["list"])
    model: str = Field(enum=["private-gpt"])
    data: list[Embedding]

