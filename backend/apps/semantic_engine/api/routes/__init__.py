from django.urls import path
from apps.semantic_engine.api.views.preprocessing_views import PreprocessingAnalyzeAPIView
from apps.semantic_engine.api.views.embedding_generate_API_view import EmbeddingGenerateAPIView

urlpatterns = [
    path("preprocessing/", PreprocessingAnalyzeAPIView.as_view(), name="index"),
    path("embedding/", EmbeddingGenerateAPIView.as_view(), name="embedding"),
]
