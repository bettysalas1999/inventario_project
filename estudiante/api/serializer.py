from rest_framework import serializers
from estudiante.models import Estudiante


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__' 