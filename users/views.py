# users/views.py

import string
import random
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.hashers import check_password
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Generate a random token
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        
        # Update user activation_link and activation_status
        user = serializer.instance
        user.activation_link = token
        user.activation_status = False
        user.save()

        # Send activation email
        current_site = get_current_site(request)
        activation_link = f"http://{current_site.domain}/api/users/activate/{token}/"
        message = f"Hi {user.email},\n\nPlease click the following link to activate your account:\n{activation_link}"
        send_mail(
            subject='Activate Your Account',
            message=message,
            from_email='Patima App <ict2020067@as.rjt.ac.lk>',
            recipient_list=[user.email],
            fail_silently=False,
        )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

@api_view(['GET'])
def activate_user(request, token):
    try:
        user = User.objects.get(activation_link=token)
        user.activation_status = True
        user.save()
        return Response({'message': 'Account activated successfully'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'Invalid activation token'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def login_user(request, email,password,activation_status):
    try:
        user = User.objects.get(email=email,password=password,activation_status=activation_status)
        return Response({'message': 'OK'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'NOOOOO'}, status=status.HTTP_404_NOT_FOUND)


