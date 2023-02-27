from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='products_home'),
    path('products/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
