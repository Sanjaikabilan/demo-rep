from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_name, name='team_name'),
    path('data/<int:team_id>/', views.data, name='data'),
    path('chart', views.chart, name='chart'),
    path('sensor-data-json/<int:team_id>/', views.sensor_data_json, name='sensor_data_json'),
]
