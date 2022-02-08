from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from user_app.api.serializers import RegistrationSerializer
# from user_app import models #this model is used for creating token automatically
#for auto token to be created you need to import models.py

# class RegistrationView(APIView):
#     def post(self, request):
#         serializer = RegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return serializers.data

class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
 
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
            
            # token = Token.objects.get(user=account).key
            # data['token'] = token
            
            refresh = RefreshToken.for_user(account)
            
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            
            
        else:
            data =  serializers.errors  
        return Response(data)