from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    website = models.URLField(blank=True)

    def _str_(self):
        return self.user.username

class Experiment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    id = models.IntegerField(blank=True, verbose_name='Experiment ID',primary_key=True)
    csv_file1 = models.FileField(upload_to='csv/', null=True, blank=True)
    csv_file2 = models.FileField(upload_to='csv/', null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)                                          
    result = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)


    def _str_(self):
        return str(self.id)