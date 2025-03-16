from rest_framework.serializers import ModelSerializer
from .models import *

class MentorSerializer(ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'

class GuruhSerializer(ModelSerializer):
    mentor = MentorSerializer(read_only=True)
    class Meta:
        model = Guruh
        fields = '__all__'

class GuruhPostSerializer(ModelSerializer):
    class Meta:
        model = Guruh
        fields = '__all__'

class StudentSerializer(ModelSerializer):
    mentor = MentorSerializer(read_only=True)
    class Meta:
        model = Student
        fields = '__all__'

class StudentPostSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'