from django.urls import path
from .views import CreateMeasurementView, LCRUSensorsView

urlpatterns = [
    path('sensors/<pk>/', LCRUSensorsView.as_view()),
    path('sensors/', LCRUSensorsView.as_view()),
    path('measurements/', CreateMeasurementView.as_view()),
]
