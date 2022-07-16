from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostList.as_view(),name="list"),
    path('detail/<int:pk>/',views.PostDetail.as_view(),name="detail"),
    path('update/<int:pk>',views.UpdatePost.as_view(),name="update"),
    path('delete/<int:pk>',views.DeletePost.as_view(),name='delete'),
    path('post/',views.PostFormView.as_view(),name="post"),
    path('detail/<int:pk>/comment',views.CommentonPost.as_view(),name="comment")
]