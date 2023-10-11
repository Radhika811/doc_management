from rest_framework import serializers
from docmanagement.models.tags import Tags

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


