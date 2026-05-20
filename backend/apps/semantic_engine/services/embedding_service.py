from apps.semantic_engine.services.pipelines.embedding_application_pipeline import EmbeddingApplicationPipeline


class EmbeddingService:

    @staticmethod
    def generate_embedding(text: str):
        return EmbeddingApplicationPipeline.process(text)
