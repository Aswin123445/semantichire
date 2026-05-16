class PreprocessingAnalyzeResponseSchema:

    @staticmethod
    def build(original_text: str, cleaned_text: str = None, tokens: list = None):

        return {
            "success": True,
            "message": "Preprocessing analysis completed.",
            "data": {
                "original_text": original_text,
                "cleaned_text": cleaned_text,
                "tokens": tokens or [],
            },
        }