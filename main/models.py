from django.core.validators import MinValueValidator
from django.db import models

GENDER_CHOICES = (
    ('Erkak', 'Erkak'),
    ('Ayol','Ayol')
)
class Basemodel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Mentor(Basemodel):
    ism = models.CharField(max_length=255)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    profession = models.CharField(max_length=255)
    KPI = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.ism

class Guruh(Basemodel):
    nom = models.CharField(max_length=255)
    vaqt = models.TimeField(blank=True, null=True)
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True)
    finshed_at = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.nom

class Student(Basemodel):
    ism = models.CharField(max_length=255)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    age = models.PositiveSmallIntegerField()
    guruh = models.ForeignKey(Guruh, on_delete=models.SET_NULL, null=True)
    aktiv = models.BooleanField(default=True)

    def __str__(self):
        return self.ism

class Tolov(Basemodel):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    izoh = models.TextField(null=True, blank=True)
    miqdor = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.student.ism if self.student else self.izoh