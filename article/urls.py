from django.urls import path, include

from article.views import ArticleRetrieveUpdateDestroyAPIView

app_name = 'article'

urlpatterns = [
    path('v1/api/<int:pk>/', ArticleRetrieveUpdateDestroyAPIView.as_view(), name='article-retrieve-update-destroy'),
]
