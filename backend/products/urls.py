from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductCreatListeAPIView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),
    path('<int:pk>/', views.ProductDetialAPIView.as_view()),
]
 