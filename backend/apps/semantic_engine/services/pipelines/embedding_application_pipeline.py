from apps.semantic_engine.domain.preprocessing.pipeline import PreprocessingPipeline
from apps.semantic_engine.domain.embeddings.pipelines import EmbeddingPipeline
class EmbeddingApplicationPipeline:
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

        # Placeholder for next stage
        embedding_result = EmbeddingPipeline.generate(cleaned_text)

        return {
            "preprocessing_result": preprocessing_result,
            "processed_text": cleaned_text,
            "embedding_result": embedding_result,
        }
