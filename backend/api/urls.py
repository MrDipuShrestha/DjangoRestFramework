from django.urls import path
from .views import ResponseRawData

urlpatterns = [
    path('', ResponseRawData.as_view())
]
