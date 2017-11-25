from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tutorial.quickstart.models import Ticket


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('created', 'description', 'severity', 'assignee', 'reporter', 'is_done', 'donedate')