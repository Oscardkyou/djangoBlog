from django.urls import path
from .views import PostList, PostDetail, AuthorList, AuthorDetail

urlpatterns = [
    # Эндпоинты для работы с постами
    path('api/posts/', PostList.as_view(), name='post-list'),  # GET (список всех постов), POST (создание нового поста)
    path('api/posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),  # GET (информация о конкретном посте), PUT (обновление поста), DELETE (удаление поста)

    # Эндпоинты для работы с авторами
    path('api/authors/', AuthorList.as_view(), name='author-list'),  # GET (список всех авторов), POST (создание нового автора)
    path('api/authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),  # GET (информация о конкретном авторе), PUT (обновление автора), DELETE (удаление автора)
]

