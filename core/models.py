from django.db import models
from django.utils import timezone

class Beach(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=[('Safe to Swim', 'Safe to Swim'), ('Unsafe to Swim', 'Unsafe to Swim')])
    description = models.TextField()
    current_temperature = models.FloatField(max_length=100)
    current_rain = models.CharField(max_length=100)
    current_wind_speed = models.FloatField(max_length=100)
    saturday_temperature = models.FloatField(max_length=100)
    saturday_rain = models.CharField(max_length=100)
    saturday_wind_speed = models.FloatField(max_length=100)
    sunday_temperature = models.FloatField(max_length=100)
    sunday_rain = models.CharField(max_length=100)
    sunday_wind_speed = models.FloatField(max_length=100)
    busyness = models.CharField(max_length=100)
    last_updated = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='beach_pictures/')
    fun_facts = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class CommentSection(models.Model):
    beach = models.OneToOneField(Beach, on_delete=models.CASCADE, related_name='comment_section')
    
    def __str__(self):
        return f"Comment Section for {self.beach.name}"  

'''class GeneralCommentSection(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title '''      

class Comment(models.Model):
    beach = models.ForeignKey(Beach, on_delete=models.CASCADE, null=True, blank=True)
    #comment_section = models.ForeignKey(CommentSection, on_delete=models.CASCADE, related_name='comments')
    #general_comment_section = models.ForeignKey(GeneralCommentSection, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    user_name = models.CharField(max_length=100, default='Anonymous')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user_name} on {self.timestamp}"
    
    '''def save(self, *args, **kwargs):
        if self.beach and self.general_comment_section:
            raise ValueError("A comment cannot be linked to both a beach and a general comment section.")
        if not self.beach and not self.general_comment_section:
            raise ValueError("A comment must be linked to either a beach or a general comment section.")
        super().save(*args, **kwargs)'''

class Report(models.Model):
    CROWD_LEVEL_CHOICES = [(i, str(i)) for i in range(1, 11)]  # Choices from 1 to 10

    report_id = models.AutoField(primary_key=True)
    beach = models.ForeignKey('Beach', on_delete=models.CASCADE, related_name='reports')
    detail = models.TextField()  # Description or detail of the report
    source = models.URLField(blank=True, null=True)  # Can be an image URL or a webpage URL
    timestamp = models.DateTimeField(default=timezone.now)
    crowd_level = models.IntegerField(choices=CROWD_LEVEL_CHOICES)  # An integer representing the crowd level, e.g., 1-10 scale
    comment = models.TextField()  # Optional, linked to a comment if applicable

    def __str__(self):
        return f"Report {self.report_id} on {self.beach.name}"    

class Source(models.Model):
    source_id = models.AutoField(primary_key=True)
    beach = models.ForeignKey('Beach', on_delete=models.CASCADE, related_name='sources', null=True, blank=True)
    report = models.ForeignKey('Report', on_delete=models.CASCADE, related_name='sources', null=True, blank=True)

    def __str__(self):
        return f"Source {self.source_id}"
    
class Map(models.Model):
    map_id = models.AutoField(primary_key=True)
    beach = models.ForeignKey('Beach', on_delete=models.CASCADE, related_name='map', null=True, blank=True)
    location = models.CharField(max_length=100)
    coordinateLat = models.FloatField(max_length=100)  
    coordinateLong = models.FloatField(max_length=100)

    def __str__(self):
        return  self.location

 