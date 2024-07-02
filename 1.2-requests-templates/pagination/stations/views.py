from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    csv_file_path = settings.BUS_STATION_CSV
    table = []
    with open(csv_file_path, encoding='utf-8') as csvfile:
        data = csv.DictReader(csvfile, delimiter=",")
        table = list(data)

    paginator = Paginator(table, 10)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)
    context = {
    'page': page,
    'bus_stations': page.object_list
    }

    return render(request, 'stations/index.html', context)
