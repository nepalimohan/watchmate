from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from user_app.api.serializers import RegistrationSerializer

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
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)