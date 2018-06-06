from django.urls import path
from .views import persons_list
from .views import person_new
from .views import person_update

urlpatterns = [
    path('list/', persons_list, name="person_list"),
    path('new/', person_new, name="person_new"),
    path('update/<int:id>/', person_update, name="person_update"),
]
