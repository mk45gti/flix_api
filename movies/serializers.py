from rest_framework import serializers
from movies.models import Movie

class MovieModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser inferior a 1990.')
        return value
    
    def validate_resume(self, value):
        if len(value) < 100:
            raise serializers.ValidationError('A sinopse deve ter no mínimo 100 caracteres.')
        return value