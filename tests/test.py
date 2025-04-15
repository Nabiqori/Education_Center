from django.test import TestCase
from main.models import *

class ModelTestCase(TestCase):

    def setUp(self):
        self.mentor = Mentor.objects.create(
            ism='Ali',
            gender='Erkak',
            phone_number='998901234567',
            profession='Dasturchi',
            KPI=88.5
        )

        self.guruh = Guruh.objects.create(
            nom='Python',
            mentor=self.mentor
        )

        self.student = Student.objects.create(
            ism='Muslima',
            gender='Ayol',
            phone_number='+998909876543',
            age=21,
            guruh=self.guruh,
            aktiv=True
        )

        self.tolov = Tolov.objects.create(
            student=self.student,
            izoh='1-oy uchun to\'lov',
            miqdor=250000.0
        )

    def test_mentor_creation(self):
        self.assertEqual(self.mentor.ism, 'Ali')
        self.assertEqual(self.mentor.gender, 'Erkak')
        self.assertEqual(str(self.mentor), 'Ali')

    def test_guruh_creation(self):
        self.assertEqual(self.guruh.nom, 'Python')
        self.assertEqual(self.guruh.mentor, self.mentor)
        self.assertEqual(str(self.guruh), 'Python')

    def test_student_creation(self):
        self.assertEqual(self.student.ism, 'Muslima')
        self.assertTrue(self.student.aktiv)
        self.assertEqual(self.student.guruh.nom, 'Python')
        self.assertEqual(str(self.student), 'Muslima')

    def test_tolov_creation(self):
        self.assertEqual(self.tolov.miqdor, 250000.0)
        self.assertEqual(self.tolov.student.ism, 'Muslima')
        self.assertEqual(str(self.tolov), 'Muslima')
