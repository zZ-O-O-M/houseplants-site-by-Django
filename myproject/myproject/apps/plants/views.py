from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Plant, PlantType, WindowType


# ------- USER VIEWS -------

def list(request):
    plants_list = Plant.objects.all()
    return render(request, 'plants/user/list.html', {'plants_list': plants_list})


def plant_detail(request, plant_id):
    try:
        plant_info = Plant.objects.get(id = plant_id)
    except:
        raise Http404("Статья не найдена!")

    return render(request, 'plants/user/plant_detail.html', {'plant_info': plant_info})


# ------- ADMIN VIEWS -------

def admin_list(request):
    plants_list = Plant.objects.all()
    return render(request, 'plants/admin/list.html', {'plants_list': plants_list})


def admin_plant_detail(request, plant_id):
    try:
        plant_info = Plant.objects.get(id = plant_id)
    except:
        raise Http404("Статья не найдена!")

    # Data
    all_plant_types = PlantType.objects.all()
    all_window_types = WindowType.objects.all()

    return render(request, 'plants/admin/plant_detail.html', {'plant_info': plant_info,
                                                              'all_plant_types': all_plant_types,
                                                              'all_window_types': all_window_types})


def admin_save_plant_data(request, plant_id):
    try:
        plant_info = Plant.objects.get(id = plant_id)
    except:
        raise Http404("Статья не найдена!")

    # Set new data
    plant_info.plant_name = request.POST['plant_name']
    plant_info.plant_requirements = request.POST['plant_requirements']
    plant_info.plant_type = PlantType.objects.get(id = int(request.POST['plant_type']))
    plant_info.plant_window_type = WindowType.objects.get(id = int(request.POST['plant_window_type']))

    # Save new data
    plant_info.save()

    return HttpResponseRedirect(reverse('plants:admin_plant_detail', args = (plant_id,)))


def admin_add_plant_page(request):
    return render(request, 'plants/admin/add_plant.html')


def admin_add_plant_action(request):
    plant_info = Plant()

    # Set new data
    plant_info.plant_name = request.POST['plant_name']
    plant_info.plant_requirements = request.POST['plant_requirements']
    plant_info.plant_type = PlantType.objects.get(id = int(request.POST['plant_type']))
    plant_info.plant_window_type = WindowType.objects.get(id = int(request.POST['plant_window_type']))

    # Save new data
    plant_info.save()

    return HttpResponseRedirect(reverse('plants:admin_list'))
