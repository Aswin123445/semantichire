from rest_framework import serializers


class BatchEmbeddingGenerateSerializer(serializers.Serializer):

    text = serializers.CharField(required=True, allow_blank=False)
