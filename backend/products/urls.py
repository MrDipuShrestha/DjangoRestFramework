from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductCreatListeAPIView.as_view()),
    path('<int:pk>/', views.ProductDetialAPIView.as_view())
]
