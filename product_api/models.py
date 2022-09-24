from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='products', blank=True)
    product_type = models.ForeignKey('weather_api.WeatherType', blank=True, null=True, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0, blank=True, null=True)
    added_by = models.ForeignKey('user_api.User', on_delete=models.CASCADE, related_name='added_by')
    edited_by = models.ForeignKey('user_api.User', on_delete=models.CASCADE, blank=True, null=True, related_name='updated_by')
    is_deleted = models.BooleanField(default=False)
    added_date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name) + " - " + str(self.added_by)