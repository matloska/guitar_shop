from django.urls import path
from .views import home_view, ListGuitarsView, CreateGuitarView

app_name = 'main'

urlpatterns = [
    path('', home_view, name="homepage"),
    path('guitar_list/', ListGuitarsView.as_view(), name='guitar_list'),
    path('add_guitar/', CreateGuitarView.as_view(), name='add_guitar')
]