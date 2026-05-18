from .generators import EmbeddingGenerator


class EmbeddingPipeline:
    """
    Embedding domain workflow pipeline.

    Responsibility:
    - coordinate embedding-specific workflows
    - manage embedding generation stages
    - return structured embedding results

    Flow:
    processed text
    ↓
    embedding generation
    ↓
    embedding analysis
    ↓
    structured vector result
    """

    @staticmethod
    def generate(text: str) -> dict:
        """
        Generate semantic embedding from processed text.
        """

        # Step 1 — Generate embedding vector
        embedding = EmbeddingGenerator.generate(text)

        # Step 2 — Determine embedding dimension
        embedding_dimension = len(embedding)

        # Step 3 — Return structured result
        return {
            "text": text,
            "embedding_dimension": embedding_dimension,
            "embedding": embedding,
        }
