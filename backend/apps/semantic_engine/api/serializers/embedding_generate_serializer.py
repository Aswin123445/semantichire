from rest_framework import serializers


class EmbeddingGenerateSerializer(serializers.Serializer):

    text = serializers.CharField(required=True, allow_blank=False)
