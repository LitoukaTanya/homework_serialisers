from django.urls import path

from users import views
from users.views import UsersViewSet

app_name = 'users'

urlpatterns = [
    path('v1/api/', UsersViewSet.as_view({'get': 'list', 'post': 'create'})),
]