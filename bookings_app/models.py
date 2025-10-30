from django.db import models
from events_app.models import Event

# Model definitions for the bookings application
class Participant(models.Model):
    first_name = models.CharField(max_length=100 , help_text="Der Vorname ist erforderlich!")
    last_name = models.CharField(max_length=100 , help_text="Der Nachname ist erforderlich!")
    email = models.EmailField(unique=True , help_text="Die Email-Adresse ist erforderlich!")
    full_name = models.CharField(blank =True)

    def __str__(self):
          return self.full_name or f"{self.first_name} {self.last_name}"

# Model definition for bookings
class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.participant} → {self.event.title}"