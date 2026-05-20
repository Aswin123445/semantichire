from apps.semantic_engine.domain.chunking.sentence_chunker import (
    SentenceChunker
)


class ChunkingPipeline:
    """
    Domain-level chunking workflow pipeline.

    Responsibility:
    - coordinate chunking workflow
    - prepare semantic chunks
    - validate chunks
    - structure chunking results

    Flow:
    processed text
    ↓
    sentence chunking
    ↓
    chunk validation
    ↓
    structured chunk result
    """

    @staticmethod
    def process(text: str) -> dict:
        """
        Execute chunking workflow.
        """

        # Step 1 — Generate sentence chunks
        chunks = SentenceChunker.chunk(text)

        # Step 2 — Remove empty chunks
        validated_chunks = [
            chunk.strip()
            for chunk in chunks
            if chunk.strip()
        ]

        # Step 3 — Prepare structured chunk metadata
        structured_chunks = []

        for index, chunk in enumerate(validated_chunks, start=1):

            structured_chunks.append({
                "chunk_id": index,
                "chunk_text": chunk,
                "word_count": len(chunk.split())
            })

        # Step 4 — Return structured chunking result
        return {
            "chunks": structured_chunks,
            "total_chunks": len(structured_chunks)
        }