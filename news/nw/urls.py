from django.urls import path
from .views import home_view, cotegories_view, article_detail, add_star, comment_view, AddComment

urlpatterns = [
    path('', home_view, name='home'),
    path('category/<int:pk>/', cotegories_view, name='category'),
    path('article/<int:pk>/', article_detail, name='article'),
    path('add-star/<int:id_post>/<int:id_user>/<str:ball>/', add_star, name='add_star'),
    path('comment/<int:id_post>/<int:id_user>/', comment_view, name='comment-username'),
    path('comment/<int:id_post>/', AddComment.as_view(), name='comment'),
]

