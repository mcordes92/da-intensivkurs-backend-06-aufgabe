from django.db import models

# Model definitions for the events application
class EventCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model definition for event locations
class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

# Model definition for events
class Event(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    
    class Meta:
        verbose_name = "Liveact"
        ordering = ["date"]

    def __str__(self):
        return f"{self.title} ({self.date.date()})"