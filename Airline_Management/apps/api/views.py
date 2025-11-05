from ..accounts.models import Account

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from rest_framework import status 
from .serializers import AccountSerializer

class AccountListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    """ def perform_destroy(self, instance):
        if instance.is_active:
            instance.is_active = False
            instance.save() """
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_active:
            instance.is_active = False
            instance.save()
            return Response({"detail": f"{instance.username} deactivated successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": f"{instance.username} is already deactivated."}, status=status.HTTP_400_BAD_REQUEST)
        