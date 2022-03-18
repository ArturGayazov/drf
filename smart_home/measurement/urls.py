from django.urls import path
from .views import *
urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorViewCU.as_view()),
    path('sensors/<pk>/', SensorViewCU.as_view()),
    path('measurements/', MeasurementsViewCU.as_view()),
]
