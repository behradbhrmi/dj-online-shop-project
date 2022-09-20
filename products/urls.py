from django.urls import path

from .views import ProductsListView, ProductDetailView, CommentCreateView

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('comments/<int:pk>/', CommentCreateView.as_view(), name='comment_create'),
]
