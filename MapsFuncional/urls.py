
from django.contrib import admin
from django.urls import path
from usuario.views import CustomUserListCreateView
from rest_framework.authtoken.views import obtain_auth_token
from usuario.views import Me


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', obtain_auth_token, name='login'),

    path('cadastro/', CustomUserListCreateView.as_view(), name='create-user'),

    path('me/', Me.as_view(), name='dados-usuario')
]
