# from django.http import HttpResponse
from django.shortcuts import render
from .models import AirPollution
from .forms import myForm
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt
import matplotlib


def return_graph(x, y, countryName, filterSelection):
    match filterSelection:
        case 'aqivalue':
            filterSelection = "AQI Value"
        case 'coaqivalue':
            filterSelection = "CO AQI Value"
        case 'ozoneaqivalue':
            filterSelection = "Ozone AQI Value"
        case 'notwoaqivalue':
            filterSelection = "NO2 AQI Value"
        case _:
            filterSelection = "PM2.5 Value"
    matplotlib.use('agg')
    fig = plt.figure()
    plt.rcParams["figure.figsize"] = [8, 8]
    COLOR = '#AAA694'
    plt.rcParams['text.color'] = COLOR
    plt.rcParams['axes.labelcolor'] = COLOR
    plt.rcParams['xtick.color'] = COLOR
    plt.rcParams['ytick.color'] = COLOR
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Tahoma']
    plt.scatter(x, y, color = COLOR)
    plt.title(countryName)
    plt.xlabel("City")
    plt.ylabel(filterSelection)
    plt.xticks(fontsize = np.ceil(abs(-0.5 * len(x) + 14))) # use an exponential decay function to set the size
    plt.gca().spines["top"].set_color(COLOR)
    plt.gca().spines["bottom"].set_color(COLOR)
    plt.gca().spines["left"].set_color(COLOR)
    plt.gca().spines["right"].set_color(COLOR)
    if len(x) > 22:
        plt.gca().axes.get_xaxis().set_ticks([])
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg', transparent=True)
    imgdata.seek(0)
    plt.close()
    data = imgdata.getvalue()
    return data

def home(request):
    temp = 0
    context = {"temp" : temp,}
    return render(request, "main/home.html", context)

def output(request):
    form = myForm
    context = {'form' : form}
    if request.method == 'POST':
        try:
            input = str(request.POST.get('selection')).lower().title()
            inputTwo = str(request.POST.get('filterSelection')).lower()
            x = AirPollution.objects.values_list('city', flat = True).filter(country = input)
            y = AirPollution.objects.values_list(inputTwo, flat = True).filter(country = input)
            if len(x) == 0 or len(y) == 0:
                context = {'error' : 'The text entered is not a country within the data set, please try again.', 'form' : form}
                return render(request, 'main/output.html', context)
        except:
            context = {'error' : 'The text entered is not a country within the data set, please try again.', 'form' : form}
            return render(request, 'main/output.html', context)
        graphic = return_graph(x, y, input, inputTwo)
        context = {'graphic' : graphic, 'form' : form}
        return render(request, 'main/output.html', context) 
    return render(request, 'main/output.html', context)