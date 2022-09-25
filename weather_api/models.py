from django.db import models


class WeatherType(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    lowest_temp = models.FloatField(default=0.0, blank=True, null=True)
    hightest_temp = models.FloatField(default=0.0, blank=True, null=True)
    added_by = models.ForeignKey('user_api.User', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    added_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name) + " - " + str(self.lowest_temp) + " - " + str(self.hightest_temp) + " - " + str(self.is_deleted)