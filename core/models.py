from django.db import models
from django.utils import timezone

class Beach(models.Model):
    name = models.CharField(max_length=100)
    urlName = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=[('Safe to Swim', 'Safe to Swim'), ('Unsafe to Swim', 'Unsafe to Swim')])
    description = models.TextField()
    current_temperature = models.FloatField()
    current_rain = models.CharField(max_length=100)
    current_wind_speed = models.FloatField()
    saturday_temperature = models.FloatField(max_length=100)
    saturday_rain = models.CharField(max_length=100)
    saturday_wind_speed = models.FloatField()
    sunday_temperature = models.FloatField()
    sunday_rain = models.CharField(max_length=100)
    sunday_wind_speed = models.FloatField()
    picture = models.ImageField(upload_to='beach_pictures/')
    funFacts = models.TextField(blank=True)
    average_rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    beach = models.ForeignKey(Beach, on_delete=models.CASCADE, null=True, blank=True)
    user_name = models.CharField(max_length=100, default='Anonymous')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField()

    def __str__(self):
        return f"Comment by {self.user_name} on {self.timestamp}"
    

class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    beach = models.ForeignKey('Beach', on_delete=models.CASCADE, related_name='reports')
    detail = models.TextField()  
    source = models.URLField(blank=True, null=True)  
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Report {self.report_id} on {self.beach.name}"    
    
class Map(models.Model):
    map_id = models.AutoField(primary_key=True)
    beach = models.ForeignKey('Beach', on_delete=models.CASCADE, related_name='map', null=True, blank=True)
    location = models.CharField(max_length=100)
    coordinateLat = models.FloatField()  
    coordinateLong = models.FloatField()

    def __str__(self):
        return  self.location

class EducationalContent(models.Model):
    EducationalContent_id = models.AutoField(primary_key=True)
    title1 = models.CharField(max_length=100)
    detail1 = models.TextField()  
    title2 = models.CharField(max_length=100)
    detail2 = models.TextField() 
    source = models.URLField(blank=True, null=True)  
 
    def __str__(self):
        return  self.title1