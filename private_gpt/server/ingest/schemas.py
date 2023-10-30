
from typing import Any

from pydantic import BaseModel, Field


class IngestedDoc(BaseModel):
    object: str = Field(enum=["ingest.document"])
    doc_id: str = Field(examples=["c202d5e6-7b69-4869-81cc-dd574ee8ee11"])
    doc_metadata: dict[str, Any] | None = Field(
        examples=[
            {
                "page_label": "2",
                "file_name": "Sales Report Q3 2023.pdf",
            }
        ]
    )

    @staticmethod
    def curate_metadata(metadata: dict[str, Any]) -> dict[str, Any]:
        """Remove unwanted metadata keys."""
        metadata.pop("doc_id", None)
        metadata.pop("window", None)
        metadata.pop("original_text", None)
        return metadata


class IngestResponse(BaseModel):
    object: str = Field(enum=["list"])
    model: str = Field(enum=["private-gpt"])
    data: list[IngestedDoc]