from apps.semantic_engine.domain.preprocessing.pipeline import PreprocessingPipeline
from apps.semantic_engine.domain.embeddings.pipelines import EmbeddingPipeline
from apps.semantic_engine.domain.chunking.pipeline import ChunkingPipeline


class BatchEmbeddingApplicationPipeline:
    """
    Application-level embedding workflow pipeline.

    Responsibility:
    - coordinate multiple domains
    - manage application workflow
    - orchestrate semantic processing stages

    Flow:
    raw text
    ↓
    preprocessing pipeline
    ↓
    embedding pipeline
    ↓
    structured embedding result
    """

    @staticmethod
    def process(text: str) -> dict:

        # Step 1 — Run preprocessing pipeline
        preprocessing_result = PreprocessingPipeline.process(text)
        cleaned_text = preprocessing_result["cleaned_text"]
        chucked_result = ChunkingPipeline.process(cleaned_text)
        chunk_texts = [chunk["chunk_text"] for chunk in chucked_result["chunks"]]
        # Placeholder for next stage
        embedding_result = EmbeddingPipeline.generate(chunk_texts)

        return {
            "total_chunks": len(chunk_texts),
            "preprocessing_result": preprocessing_result,
            "processed_text": cleaned_text,
            "embedding_result": embedding_result,
            "chunks": chunk_texts,
            "embedding_dimension": embedding_result.get("embedding_dimension", 0),
        }
