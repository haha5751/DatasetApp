from django import forms
from .models import AirPollution

class myForm(forms.Form):
    result = [('aqivalue', 'AQI Value'), ('coaqivalue', 'CO AQI Value'), ('ozoneaqivalue', 'Ozone AQI Value'), ('notwoaqivalue', 'NO2 AQI Value'), ('pmtwodotfivevalue', 'PM2.5 Value')]
    selection = forms.CharField(label = "Enter a Country", max_length = 100)
    # filterSelection = forms.CharField(label = 'Select a Field', widget = forms.Select(choices = result))
    filterSelection = forms.ChoiceField(choices = result, label = 'Select a Field', widget = forms.Select(attrs = {'class': 'transparent-dropdown'}))
    

