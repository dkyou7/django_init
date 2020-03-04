from django.urls import path
from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /5/comment/
    path('<int:question_id>/comment/', views.comment, name='comment'),

    path('create/',views.create,name='create'),
]