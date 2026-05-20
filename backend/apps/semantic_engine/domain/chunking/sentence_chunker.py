import re


class SentenceChunker:
    """
    Simple sentence-based chunker.

    Responsibility:
    - split text into semantic sentence units
    - prepare chunks for batch embedding

    Current Strategy:
    - sentence-based chunking

    Future Evolution:
    - token-aware chunking
    - overlap chunking
    - semantic chunking
    """

    @staticmethod
    def chunk(text: str) -> list:
        """
        Split text into sentence chunks.
        """

        # Split using sentence-ending punctuation
        chunks = re.split(r"[.!?]+", text)

        # Remove empty chunks and normalize spacing
        cleaned_chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

        return cleaned_chunks
