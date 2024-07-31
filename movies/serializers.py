from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from actors.models import Actor

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    release_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True)
    resume = serializers.CharField()

class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value  
    
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não pode ser maior do que 200 caracteres.')
        return value

class MovieListDetailSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None

class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
