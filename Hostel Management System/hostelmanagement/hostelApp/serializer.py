from rest_framework import serializers
from .models import BookVacancy
#convert our complex data to frontend readable and convert also deserialization as you have read it already

class VacancyBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookVacancy
        fields ='__all__'
        