#Importing serializers to turn queryset to json
from rest_framework import serializers
from schedule.models import Schedule

#creating serializer from model
class scheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__' #to include all fields
