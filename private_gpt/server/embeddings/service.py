from injector import inject, singleton

from private_gpt.components.embedding import EmbeddingComponent
from private_gpt.server.embeddings.schemas import Embedding


@singleton
class EmbeddingsService:
    @inject
    def __init__(self, embedding_component: EmbeddingComponent) -> None:
        self.embedding_model = embedding_component.embedding_model

    def texts_embeddings(self, texts: list[str]) -> list[Embedding]:
        texts_embeddings = self.embedding_model.get_text_embedding_batch(texts)
        return [
            Embedding(
                index=texts_embeddings.index(embedding),
                object="embedding",
                embedding=embedding,
            )
            for embedding in texts_embeddings
        ]
