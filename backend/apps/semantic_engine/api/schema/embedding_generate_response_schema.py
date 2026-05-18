class EmbeddingGenerateResponseSchema:

    @staticmethod
    def build(text: str, embedding_dimension: int, embedding: list):

        return {
            "success": True,
            "message": "Embedding generated successfully.",
            "data": {
                "text": text,
                "embedding_dimension": embedding_dimension,
                "embedding": embedding,
            },
        }
