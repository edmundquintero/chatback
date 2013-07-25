from django.contrib.auth.models import User
from chatback.models import *
from rest_framework.serializers import *

# class StepSerializer(ModelSerializer):
#     class Meta:
#         exclude = ['studentType',]
#         model = Step
#         depth = 0   # Setting the depth to 1 will display the full Type models in the feed.
#                     # Setting the depth to 0 will display the Type ID's in a list instead of the full model.

# class StepOrderSerializer(ModelSerializer):

#     step = StepSerializer()
#     class Meta:
#         exclude = ['studentType',]
#         model = StepOrder
#         depth = 0 

class RoomSerializer(ModelSerializer):

    class Meta:
        model = Room
        depth = 1
                    