from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from api.models import Test, Text


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'name', 'description', 'created_dt', 'updated_dt']
        extra_kwargs = {
            'created_dt': {'read_only': True},
            'updated_dt': {'read_only': True},
        }


class TextSerializer(serializers.ModelSerializer):
    file = serializers.CharField(
        validators=[UniqueValidator(queryset = Text.objects.all(), message="중복되는 이름입니다.")]
    )

    class Meta:
        model = Text
        fields = ['id', 'test', 'file', 'content', 'created_dt', 'updated_dt']
        extra_kwargs = {
            'created_dt': {"read_only": True},
            'updated_dt': {"read_only": True},
        }
