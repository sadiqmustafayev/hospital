from rest_framework import serializers
from core.models import Contact, Subscriber


class ContactSerializer(serializers.ModelSerializer):

  class Meta:
    model = Contact
    fields = '__all__'


class SubscriberSerializer(serializers.ModelSerializer):

  class Meta:
    model = Subscriber
    fields = ('email', )
