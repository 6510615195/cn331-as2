from django.db import models

# Create your models here.
class Subject(models.Model):
    subjectCode = models.CharField(max_length=10)
    subjectName = models.CharField(max_length=50)
    semester = models.IntegerField()
    year = models.IntegerField()
    seatAvailable = models.IntegerField()
    status = models.CharField(max_length=10)
    def __str__(self):
        return "("+self.subjectCode+")  "+self.subjectName
