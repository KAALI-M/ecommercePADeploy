# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from orders.models import Order
from orders.ordersAPI.serializers import OrderSerializer
from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow access if the user is the owner of the order or is a staff member
        return obj.user == request.user or request.user.is_staff
    

# Create Order
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrStaff]

# Read Order List
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Read Order Detail
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
