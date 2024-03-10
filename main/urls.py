from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home_view, register, ListGuitarsView, CreateGuitarView

app_name = 'main'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('guitar_list/', ListGuitarsView.as_view(), name='guitar_list'),
    path('add_guitar/', CreateGuitarView.as_view(), name='add_guitar'),
    path('', home_view, name="homepage"),
]