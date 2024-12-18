from rest_framework import serializers

from api.models import Test


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['name', 'description', 'created_dt', 'updated_dt']
        extra_kwargs = {
            'created_dt': {'read_only': True},
            'updated_dt': {'read_only': True},
        }
