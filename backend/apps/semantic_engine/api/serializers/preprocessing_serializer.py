from rest_framework import serializers
class PreprocessingAnalyzeSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, allow_blank=False)
