class PreprocessingPipeline:

    @staticmethod
    def process(text: str) -> dict:
        """
        Main preprocessing workflow pipeline.

        Flow:
        raw text
        ↓
        normalize
        ↓
        clean
        ↓
        tokenize
        ↓
        return structured preprocessing result
        """

        # Import inside method to avoid circular imports initially
        from .normalizers import TextNormalizer
        from .cleaners import TextCleaner
        from .tokenizers import TextTokenizer

        # Step 1 — Normalize text
        normalized_text = TextNormalizer.normalize(text)

        # Step 2 — Clean text
        cleaned_text = TextCleaner.clean(normalized_text)

        # Step 3 — Tokenize text
        tokens = TextTokenizer.tokenize(cleaned_text)

        # Final structured response
        return {
            "original_text": text,
            "normalized_text": normalized_text,
            "cleaned_text": cleaned_text,
            "tokens": tokens,
            "token_count": len(tokens),
        }
