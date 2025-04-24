from django.db import models

class RoadReport(models.Model):
    CONDITION_CHOICES = [
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('hazard', 'Hazard'),
        ('construction', 'Construction'),
    ]

    LOCATION_TYPE_CHOICES = [
        ('coordinates', 'Coordinates'),
        ('url', 'Location URL'),
        ('manual', 'Manual Entry'),
    ]

    location_type = models.CharField(max_length=20, choices=LOCATION_TYPE_CHOICES, default='manual')
    # Coordinates
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    # URL
    location_url = models.URLField(blank=True, null=True)
    # Manual address
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.location_type == 'coordinates':
            return f"Coords: {self.latitude}, {self.longitude} - {self.get_condition_display()}"
        elif self.location_type == 'url':
            return f"URL: {self.location_url} - {self.get_condition_display()}"
        else:
            return f"{self.street}, {self.city}, {self.state}, {self.country} - {self.get_condition_display()}"
