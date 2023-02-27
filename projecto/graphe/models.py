from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SensorData(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    data = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.team} - {self.timestamp}'
