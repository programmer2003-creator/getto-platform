from rest_framework import serializers
from .models import University, Campus


class CampusSerializer(serializers.ModelSerializer):
    university_name = serializers.ReadOnlyField(source='university.name')
    university_image = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Campus
        fields = [
            'id',
            'university',
            'university_name',
            'name',
            'description',
            'latitude',
            'longitude',
            'image',
            'university_image',
        ]

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None

    def get_university_image(self, obj):
        request = self.context.get('request')
        if obj.university.image and not obj.image:
            return request.build_absolute_uri(obj.university.image.url) if request else obj.university.image.url
        return None


class UniversitySerializer(serializers.ModelSerializer):
    campuses = CampusSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = University
        fields = ['id', 'name', 'location_name', 'description', 'image', 'campuses']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None