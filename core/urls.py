from django.urls import path
from . import views
from road_report.views import report_road_condition

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('road-report/', report_road_condition, name='report_road'),
]