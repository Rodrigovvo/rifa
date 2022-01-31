from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import Campaign
from .models import Prize
from .models import Raffle
from .models import Ticket
from core.exceptions import ExceedMaxNumberTicketsInRaffle


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class RaffleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raffle
        fields = [
            'url', 'name', 'max_number', 'raffle_image', 
            'end_date', 'description', 'ticket_price'
        ]


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['url', 'user', 'raffle']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['url', 'number', 'raffle', 'is_active', 'user']

    def validate(self, data):
        if data['number'] > data['raffle'].max_number:
            raise ExceedMaxNumberTicketsInRaffle
        return data


class PrizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = [
            'url', 'prize_name', 'prize_image', 
            'description', 'raffle'
        ]
