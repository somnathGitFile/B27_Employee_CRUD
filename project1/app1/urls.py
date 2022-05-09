from django.urls import path
from . import views

urlpatterns = [
    path('ev/', views.empformView, name='empform_url'),
    path('se/', views.showempView, name='showemp_url'),
    path('ue/<int:id>/', views.updateEmpView, name='update_url'),
    path('de/<int:id>/', views.deleteEmpView, name='delete_url')
]