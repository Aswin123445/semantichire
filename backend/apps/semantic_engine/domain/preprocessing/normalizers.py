class TextNormalizer:

    @staticmethod
    def normalize(text: str) -> str:

        normalized_text = text.lower().strip()

        normalized_text = " ".join(normalized_text.split())

        return normalized_text
