from django.urls import path, include
from product import views


urlpatterns = [
  path('latest-products/', views.LatestProductsList.as_view()),
  path('products/<slug:category_slug>/<slug:product_slug>/',
       views.ProductDetail.as_view()),
  path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
  # do not add '/'  at the end of the url in search href
  # if you add '/' it will cause the 405 error due to CORS
  path('products/search', views.search)
]
