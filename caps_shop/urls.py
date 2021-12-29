from django.contrib import admin
from django.urls import path, include
from main import views as product_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/products/', product_view.ProductListAPIView.as_view()),
    path('api/v1/products/<int:id>/', product_view.ProductDetailAPIView.as_view()),
]
