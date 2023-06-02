from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class AirPollution (models.Model):
    country = models.CharField(_("Country"), max_length = 60)
    city = models.CharField(_("City"), max_length = 90)
    aqivalue = models.IntegerField(_("AQI Value"))
    aqicategory = models.CharField(_("AQI Category"), max_length = 60)
    coaqivalue = models.IntegerField(_("CO AQI Value"))
    coaqicategory = models.CharField(_("CO AQI Category"), max_length = 60)
    ozoneaqivalue = models.IntegerField(_("Ozone AQI Value"))
    ozoneaqicategory = models.CharField(_("Ozone AQI Category"), max_length = 60)
    notwoaqivalue = models.IntegerField(_("NO2 AQI Value"))
    notwoaqicategory = models.CharField(_("NO2 AQI Category"), max_length = 60)
    pmtwodotfivevalue = models.IntegerField(_("PM2.5 AQI Value"))
    pmtwodotfivecategory = models.CharField(_("PM2.5 AQI Category"), max_length = 60)
    lat = models.FloatField(_("lat"))
    lng = models.FloatField(_("lng"))
    
    @classmethod
    def get_field_names(cls):
        return [f.name for f in cls._meta.fields]