from django.contrib.auth.models import User
from chatback.models import *
from rest_framework.serializers import *

class EntrySerializer(ModelSerializer):
    class Meta:
        model = Entry
        depth = 0

class ChatLogSerializer(ModelSerializer):

    entries = EntrySerializer(many=True)
    class Meta:
        model = ChatLog
        depth = 0 

class RoomSerializer(ModelSerializer):

    # Uncomment the next line to display the Step ID's in the Type feed
    # steps = RelatedField(many=True)
    # Uncomment the next line to display the full Step models in the Types feed
    # chatlog = ChatLogSerializer()

    chatlogs = ChatLogSerializer(many=True)

    class Meta:
        model = Room
        depth = 2
                    

class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        depth = 1