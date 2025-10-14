from rest_framework import serializers
from .models import students


class studentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = students
        fields = ('name', 'surname', 'university', 'age',)