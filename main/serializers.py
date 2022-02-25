from rest_framework import serializers
from main.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'content', 'create_at', 'update_at')
        # fields = '__all__'






    