from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.semantic_engine.api.schema.embedding_generate_response_schema import EmbeddingGenerateResponseSchema
from apps.semantic_engine.api.serializers.embedding_generate_serializer import EmbeddingGenerateSerializer
from apps.semantic_engine.services.embedding_service import EmbeddingService

class EmbeddingGenerateAPIView(APIView):

    def post(self, request):

        serializer = EmbeddingGenerateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data["text"]

        embedding_result = EmbeddingService.generate_embedding(text)
        results = embedding_result.get("embedding_result", 0)
        response_data = EmbeddingGenerateResponseSchema.build(
            text=embedding_result["processed_text"],
            embedding_dimension=results.get("embedding_dimension", 0),
            embedding=results.get("embedding", []),
        )

        return Response(response_data, status=status.HTTP_200_OK)
