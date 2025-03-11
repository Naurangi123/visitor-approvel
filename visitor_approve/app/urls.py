from django.urls import path
from . import views

app_name = 'visitor_management'

urlpatterns = [
    path('',views.home,name='home'),
    path('request/', views.request_visit, name='request_visit'),
    path('handle_request/<int:request_id>/<str:action>/', views.handle_request, name='handle_request'),
    path('success/', views.success, name='success'),
    path('requests/', views.request_list, name='request_list'),
    
]
