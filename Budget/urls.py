from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createDepense', views.CreateDepense, name='createDepense'),
    path('depenseUser', views.ReadDepense, name='depenseUser'),
    path('createRevenue', views.CreateRevenue, name="createRevenue"),
    path('revenueUser', views.ReadRevenue, name="revenueUser"),
    path('gap', views.gap_view, name="gap"),
    path('updateD/<int:id>/', views.updateDepense, name='updateD'), 
    path('delete/<int:id>/', views.deleteDepense, name='delete'),
    path('updateR/<int:id>/', views.updateRevenue, name='updateR'),
    path('deleteR/<int:id>/', views.deleteReveneu, name='deleteR')
]
