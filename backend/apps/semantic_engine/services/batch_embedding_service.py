
from apps.semantic_engine.services.pipelines.batch_embedding_application_pipeline import BatchEmbeddingApplicationPipeline


class BatchEmbeddingService:

    @staticmethod
    def generate_embedding(text: str):
        return BatchEmbeddingApplicationPipeline.process(text)
