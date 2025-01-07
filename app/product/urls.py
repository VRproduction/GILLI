from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('about/', views.AboutPageView.as_view(), name = 'about'),
    path('shop/', views.ShopPageView.as_view(), name = 'shop'),
    path('contact/', views.ContactPageView.as_view(), name = 'contact'),

    path('blogs/', views.BlogPageView.as_view(), name = 'blog'),
    path('blogs/<int:pk>/', views.BlogDetailPageView.as_view(), name='blog-detail'),

    path('products/<int:pk>/', views.ProductDetailPageView.as_view(), name='product-detail'),
    
    path('gallery/', views.GalleryPageView.as_view(), name='gallery'),

]
