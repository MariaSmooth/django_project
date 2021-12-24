from django.urls import path
from .views import BlogListView , BlogDetailView , BlogCreateView , BlogUpdateView , BlogDeleteView , ShowListView

urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete'),
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name='edit'),
    path('post/new/', BlogCreateView.as_view(), name='new'),
    path("show/" ,ShowListView.as_view(), name="show" ),
    path("post/<int:pk>/" , BlogDetailView.as_view(), name='detail' ),
    path('', BlogListView.as_view(), name='home'),
]