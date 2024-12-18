from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'content', 'created_dt', 'updated_dt']
        extra_kwargs = {
            'created_dt': {"read_only": True},
            'updated_dt': {"read_only": True},
        }
