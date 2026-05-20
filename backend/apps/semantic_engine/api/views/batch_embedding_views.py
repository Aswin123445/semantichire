from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.semantic_engine.api.schema.batch_embedding_schema import BatchEmbeddingGenerateResponseSchema
from apps.semantic_engine.api.serializers.batch_embedding_serializer import BatchEmbeddingGenerateSerializer
from apps.semantic_engine.services.batch_embedding_service import BatchEmbeddingService


class BatchEmbeddingGenerateAPIView(APIView):

    def post(self, request):

        serializer = BatchEmbeddingGenerateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data["text"]

        data = BatchEmbeddingService.generate_embedding(text)

        response_data = BatchEmbeddingGenerateResponseSchema.build(
            original_text=text, chunks=data.get("chunks",[]), embedding_dimension=data.get("embedding_dimension", 0), total_chunks=data.get("total_chunks", 0),
        )

        return Response(response_data, status=status.HTTP_200_OK)
