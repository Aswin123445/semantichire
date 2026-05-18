from sentence_transformers import SentenceTransformer
class EmbeddingGenerator:
    """
    Responsible for semantic embedding generation.

    Responsibilities:
    - interact with transformer embedding model
    - perform semantic encoding
    - convert processed text into vector representations
    """

    # Load model once at class level
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    @staticmethod
    def generate(text: str) -> list:
        """
        Generate semantic embedding vector from text.

        Flow:
        processed text
        ↓
        transformer tokenizer
        ↓
        token IDs
        ↓
        transformer semantic encoding
        ↓
        embedding vector
        """

        # Generate embedding vector
        embedding = EmbeddingGenerator.model.encode(text)

        # Convert NumPy array to Python list
        return embedding.tolist()
