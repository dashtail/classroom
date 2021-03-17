from rest_framework import serializers
from classroom.grid.models import Grid


class GridSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grid
        fields = [
            "id",
            "name",
        ]
