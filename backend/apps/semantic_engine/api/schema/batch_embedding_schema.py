class BatchEmbeddingGenerateResponseSchema:

    @staticmethod
    def build(original_text, chunks, embedding_dimension, total_chunks):

        return {
            "success": True,
            "message": "Batch embeddings generated successfully.",
            "data": {
                "original_text": original_text,
                "total_chunks": total_chunks,
                "embedding_dimension": embedding_dimension,
                "chunks": chunks,
            },
        }
