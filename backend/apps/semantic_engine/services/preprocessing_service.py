from apps.semantic_engine.domain.preprocessing.pipeline import PreprocessingPipeline


class PreprocessingService:

    @staticmethod
    def analyze_text(text: str):
        return PreprocessingPipeline.process(text)
