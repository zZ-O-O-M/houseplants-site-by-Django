from django.urls import path

from . import views

app_name = 'plants'
urlpatterns = [

    # --------- USER VIEWS ---------
    # Plants list
    path('', views.list, name = 'list'),

    # Plant detail
    path('<int:plant_id>/', views.plant_detail, name = 'plant_detail'),

    # --------- ADMIN VIEWS ---------
    # Plants list
    path('admin', views.admin_list, name = 'admin_list'),

    # Plant detail
    path('admin/<int:plant_id>/', views.admin_plant_detail, name = 'admin_plant_detail'),
]
