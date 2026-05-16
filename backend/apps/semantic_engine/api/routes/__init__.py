from django.urls import path
from apps.semantic_engine.api.views.preprocessing_views import PreprocessingAnalyzeAPIView

urlpatterns = [
    path("preprocessing/",PreprocessingAnalyzeAPIView.as_view() , name="index"),
]
