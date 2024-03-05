from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Author
from .serializers import PostSerializer, AuthorSerializer
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import ProfileForm

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all() #ListCreateAPIView
    serializer_class = PostSerializer


    # def get(self, request, *args, **kwargs):
    #     """
    #     Получение списка всех постов.
    #     """
    #     posts = self.get_queryset()
    #     serializer = self.get_serializer(posts, many=True)
    #     return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     """
    #     Создание нового поста.
    #     """
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


def LogoutUserView(request):
    logout(request)
    return redirect('/')

def SingUpUserView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.password != request.POST.get('password2'):
                messages.error(request, "Пароли не совпадают!")
                return redirect('/signup')
            else:
                user.set_password(user.password)
                form.save()
                messages.success(request, "Резистрация прошла успенно!")
                return redirect("/")
    else:
        form = UserForm()
    return render(request, "AuthenticateUser/signup.html", {"form": form})


def SignInUserView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            try:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Вы успешно вошли!')
                    return redirect("/")
                else:
                    messages.error(request, 'Неверное имя пользователя или пароль.')
            except Exception:
                messages.error(request, 'Произошла ошибка при аутентификации. Пожалуйста, попробуйте снова.')
        else:
            messages.error(request, 'Пожалуйста, введите имя пользователя и пароль.')

    return render(request, "AuthenticateUser/signin.html")


def UserProfileView(request):
    if request.user.is_authenticated:
        profile = Profile.objects.all()
        return render(request, 'Profile/profile.html', {'profile': profile})
    else:
        return redirect('/signin')


def UserEditProfileView(request):
    if request.user.is_authenticated:
        user = request.user.profile
        if request.method == 'POST':
            email = request.POST.get('email')
            form = ProfileForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, "Редактирование профиля прошло успешно!")
                return redirect('/profile')
        else:
            form = ProfileForm(instance=user)

        context = {
            'form': form,
        }

        return render(request, 'Profile/editprofile.html', context=context)
    else:
        return redirect('/signin')