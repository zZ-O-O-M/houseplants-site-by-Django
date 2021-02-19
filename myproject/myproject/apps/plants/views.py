from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Plant, PlantType, WindowType


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

    plant_image_path = 'images/' + str(plant_id) + '.png'

    return render(request, 'plants/admin/plant_detail.html', {'plant_info': plant_info,
                                                              'plant_image_path': plant_image_path})
