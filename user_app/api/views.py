from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from user_app.api.serializers import RegistrationSerializer
from user_app import models #for auto token to be created you need to import models.py

# class RegistrationView(APIView):
#     def post(self, request):
#         serializer = RegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return serializers.data
 
@api_view(['POST',])
def registration_view(request):
    if request.method == "POST":
        serializers = RegistrationSerializer(data=request.data)
        
        data = {} #creating own dictionary to store data
        
        if serializers.is_valid():
            account = serializers.save()
            
            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email
            
            token = Token.objects.get(user=account).key
            data['token'] = token
            
            
        else:
            data =  serializers.errors  
        return Response(data)