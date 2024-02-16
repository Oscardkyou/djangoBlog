from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Author
from .serializers import PostSerializer, AuthorSerializer

class PostList(generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        """
        Получение списка всех постов.
        """
        posts = self.get_queryset()
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        Создание нового поста.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        """
        Получение информации о конкретном посте.
        """
        post = self.get_object()
        serializer = self.get_serializer(post)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        """
        Обновление информации о конкретном посте.
        """
        post = self.get_object()
        serializer = self.get_serializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        Удаление конкретного поста.
        """
        post = self.get_object()
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryApiView(generics.ListAPIView):
    #queryset = Category.objects.all()
    #serializer_class = CategorySerializer
    #permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        pass
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategoryRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Category.objects.all()
    #serializer_class = CategorySerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Представление для деталей автора
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer