import random
from .utils import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

class MpesaApiTest(viewsets.ViewSet):
    
    @action(detail=False, methods=['get'], url_path="access-token")
    def access_token(self, request):
        token = get_access_token()
        return Response({"access_token": token})
    
    @action(detail=False, methods=['post'], url_path="stk-push")
    def stk_push_payment(self, request):
        phone_number = request.data.get("phone_number")
        amount = request.data.get("amount", 1)
        response = stk_push(phone_number, amount)
        return Response(response)
    


