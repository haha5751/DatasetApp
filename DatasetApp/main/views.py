from django.shortcuts import render
from .models import AirPollution
from .forms import myForm
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt
import matplotlib

def get_stats(x, y):
    data = [0] * 6
    array = np.array(y)
    data[0] = x[int(np.argmax(array))]
    data[1] = np.max(y)
    data[2] = x[int(np.argmin(array))]
    data[3] = np.min(y)
    data[4] = round(np.mean(y), 2)
    data[5] = round(np.std(y), 2)
    return data

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
    return data, filterSelection

def home(request):
    return render(request, "main/home.html")

def output(request):
    form = myForm
    context = {'form' : form}
    if request.method == 'POST':
        try:
            input = AirPollution.objects.values_list('country', flat = True).distinct().filter(country__icontains = str(request.POST.get('selection')))[0]
            inputTwo = str(request.POST.get('filterSelection')).lower()
            x = AirPollution.objects.values_list('city', flat = True).filter(country = input)
            y = AirPollution.objects.values_list(inputTwo, flat = True).filter(country = input)
            if len(x) == 0 or len(y) == 0:
                context = {'error' : 'The text entered is not a country within the data set, please try again.', 'form' : form}
                return render(request, 'main/output.html', context)
        except:
            context = {'error' : 'The text entered is not a country within the data set, please try again.', 'form' : form}
            return render(request, 'main/output.html', context)
        graphic, selection = return_graph(x, y, input, inputTwo)
        stats = get_stats(x, y)
        context = {'graphic' : graphic, 'form' : form, 'stats' : stats, 'selection' : selection}
        return render(request, 'main/output.html', context) 
    return render(request, 'main/output.html', context)