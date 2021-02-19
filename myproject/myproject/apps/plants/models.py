from django.db import models


class PlantType(models.Model):
    plant_type_name = models.CharField("Наименование типа растения", max_length = 100)


class WindowType(models.Model):
    window_type_name = models.CharField("Наименование типа окна для растнения", max_length = 100)


class Plant(models.Model):
    plant_name = models.CharField('Наименование растения', max_length = 255)
    plant_requirements = models.TextField('Требование по уходу')

    # Foreign Keys
    plant_type = models.ForeignKey(PlantType, on_delete = models.CASCADE)
    plant_window_type = models.ForeignKey(WindowType, on_delete = models.CASCADE)
