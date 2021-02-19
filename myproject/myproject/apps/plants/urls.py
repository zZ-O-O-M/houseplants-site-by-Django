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

    # Pages
    path('admin/<int:plant_id>/', views.admin_plant_detail, name = 'admin_plant_detail'),
    path('admin/add-plant-page/', views.admin_add_plant_page, name = 'admin_add_plant_page'),

    # Actions
    path('admin/<int:plant_id>/save-data-action/', views.admin_save_plant_data, name = 'admin_save_plant_data'),
    path('admin/add-plant-action/', views.admin_add_plant_action, name = 'admin_add_plant_action'),
    path('admin/<int:plant_id>/delete-plant-action/', views.admin_delete_plant_action, name = 'admin_delete_plant_action')
]
