from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.semantic_engine.api.schema.preprocessing_schema import (
    PreprocessingAnalyzeResponseSchema,
)
from apps.semantic_engine.services.preprocessing_service import PreprocessingService

from ..serializers.preprocessing_serializer import PreprocessingAnalyzeSerializer


class PreprocessingAnalyzeAPIView(APIView):

    def post(self, request):

        serializer = PreprocessingAnalyzeSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data["text"]
        processed_data = PreprocessingService.analyze_text(text)

        response_data = PreprocessingAnalyzeResponseSchema.build(
            original_text=text,
            cleaned_text=processed_data["cleaned_text"],
            tokens=processed_data["tokens"],
        )

        return Response(response_data, status=status.HTTP_200_OK)
