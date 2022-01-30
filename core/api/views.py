from .models import Campaign
from .models import Prize
from .models import Raffle
from .models import Ticket
from .serializers import CampaignSerializer
from .serializers import GroupSerializer
from .serializers import PrizeSerializer
from .serializers import RaffleSerializer
from .serializers import TicketSerializer
from .serializers import UserSerializer

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class RaffleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows raffles to be viewed or edited.
    """
    queryset = Raffle.objects.all()
    serializer_class = RaffleSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'], name='get-tickets')
    def tickets(self, request, pk=None):
        raffle = self.get_object()
        tickets = raffle.get_tickets()
        serializer_context = {
            'request': request,
        }

        page = self.paginate_queryset(tickets)
        if page is not None:
            serializer = TicketSerializer(
                page, many=True, context=serializer_context)
            return self.get_paginated_response(serializer.data)

        serializer = TicketSerializer(
            tickets, many=True, context=serializer_context)
        return Response(serializer.data)


class CampaignViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows campaing to be viewed or edited.
    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [permissions.IsAuthenticated]


class TicketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tickets to be viewed or edited.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]


class PrizeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows prizes to be viewed or edited.
    """
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer
    permission_classes = [permissions.IsAuthenticated]
