from django.db import models


class Date(models.Model):
    date = models.DateField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        parts = []
        if self.date:
            parts.append(self.date.strftime("%Y-%m-%d"))
        if self.year:
            parts.append(str(self.year))
        if self.time:
            parts.append(self.time.strftime("%H:%M:%S"))
        return " ".join(parts) or "No date information"
