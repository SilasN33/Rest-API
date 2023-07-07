from rest_framework import serializers
from .models import Movie, Series

class MovieSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Movie
        fields = '__all__'

class SeriesSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Series
        fields = '__all__'
        
