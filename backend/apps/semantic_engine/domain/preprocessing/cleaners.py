import re


class TextCleaner:
    """
    Handles safe and minimal text cleaning.

    Modern NLP systems usually avoid aggressive cleaning
    because transformers already understand natural language well.

    Goal:
    - preserve semantic meaning
    - remove only harmful or excessive noise
    """

    @staticmethod
    def clean(text: str) -> str:
        """
        Apply light cleaning operations.

        Current cleaning:
        - normalize repeated whitespace
        - remove excessive repeated punctuation
        """

        # Normalize multiple spaces into single space
        text = re.sub(r"\s+", " ", text)

        # Reduce repeated punctuation
        text = re.sub(r"([!?.]){2,}", r"\1", text)

        return text.strip()
