from django.db import models


class Student(models.Model):
    number = models.IntegerField(verbose_name="number")
    name = models.CharField(verbose_name="name", max_length=100)
    age = models.IntegerField(verbose_name="age")
    grade = models.FloatField(verbose_name="grade")

    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"
        ordering = ['name']

    def __str__(self):
        return self.name
