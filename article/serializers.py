from article.models import Article
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

        fields = ('id', 'title', 'content', 'pub_date')