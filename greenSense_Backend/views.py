from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from greenSense_Backend.models import Article
from greenSense_Backend.api.serializers import ArticleSerializer


# api_view 데코레이터 인자로 아무것도 입력하지 않으면 기본값 'GET'
@api_view(["GET", "PUT", "DELETE"])
def article_detail_api_view(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response({"error": {
            "code": 404,
            "message": "Article not found"
        }}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
