from django.urls import path
from apps.semantic_engine.api.views.preprocessing_views import PreprocessingAnalyzeAPIView
from apps.semantic_engine.api.views.embedding_generate_API_view import EmbeddingGenerateAPIView
from apps.semantic_engine.api.views.batch_embedding_views import BatchEmbeddingGenerateAPIView

urlpatterns = [
    path("preprocessing/", PreprocessingAnalyzeAPIView.as_view(), name="index"),
    path("embedding/", EmbeddingGenerateAPIView.as_view(), name="embedding"),
    path("batch-generate/", BatchEmbeddingGenerateAPIView.as_view(), name="batch-generate"),
]
