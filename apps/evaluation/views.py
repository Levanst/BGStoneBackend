from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
# from core.models import User

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny, ])
def BasicServiceEvaluation(request):
    try:
        data = request.data.get('value', None)
        
    except Exception as e:
        res = {'msg': 'Something went wrong', 'error': str(e)}
        return Response(res, status=status.HTTP_400_BAD_REQUEST)
