from django.urls import path
from .views import PostList, PostDetail, AuthorList, AuthorDetail, SignInView, LogoutView

urlpatterns = [
    # Endpoints for working with posts
    path('api/posts/', PostList.as_view(), name='post-list'),  # GET (list of all posts), POST (create a new post)
    path('api/posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),  # GET (information about a specific post), PUT (update post), DELETE (delete post)

    # Endpoints for working with authors
    path('api/authors/', AuthorList.as_view(), name='author-list'),  # GET (list of all authors), POST (create a new author)
    path('api/authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),  # GET (information about a specific author), PUT (update author), DELETE (delete author)
    path('signin/', SignInView.as_view(), name='signin'),  # Endpoint for user sign-in
    path('logout/', LogoutView.as_view(), name='logout'),  # Endpoint for user logout
    #path('profile/', UserProfileView.as_view(), name='profile'),  # Endpoint for user profile
    #path('profile/edit/', UserEditProfileView.as_view(), name='profile-edit'),  # Endpoint for user profile editing
]
