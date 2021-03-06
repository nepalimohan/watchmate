from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
# from rest_framework import mixins
from rest_framework import generics
from django.shortcuts import render
from watchlist_app.models import Watchlist, StreamPlatform, Reviews
from watchlist_app.api.serializers import WatchlistSerializer, StreamPlatformSerializer, ReviewSerializer
from django.http import JsonResponse
from watchlist_app.api.permissions import IsAdminorReadOnly, IsReviewUserOrReadOnly
from watchlist_app.api.throttling import ReviewCreateThrottle, ReviewListThrottle, ReviewDetailThrottle
from watchlist_app.api.pagination import WatchlistPagination, WatchlistLimitOffsetPAgination, WatchlistCursorPagination 

class UserReview(generics.ListAPIView):
     # queryset = Reviews.objects.all() this statement is being overridden by get_queryset below
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [ReviewListThrottle]
    
    # def get_queryset(self): 
    #     username = self.kwargs['username']
    #     return Reviews.objects.filter(review_user__username=username)
    
    def get_queryset(self): 
        username = self.request.query_params.get('username')
        return Reviews.objects.filter(review_user__username=username)
    
    
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewCreateThrottle]
    
    def get_queryset(self): #assertion error came when queryset was not overridden
        return Reviews.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = Watchlist.objects.get(pk=pk)
        
        review_user = self.request.user
        review_queryset = Reviews.objects.filter(watchlist=watchlist, review_user=review_user)
        
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2
        
        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()
        
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this watchlist.")
        
        serializer.save(watchlist=watchlist, review_user=review_user)

class ReviewList(generics.ListAPIView):
    # queryset = Reviews.objects.all() this statement is being overridden by get_queryset below
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewListThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_user__username', 'active']
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Reviews.objects.filter(watchlist=pk) #this watchlist came from line 16 models.py
    
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review-datail'
    

# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Reviews.objects.all()
#     serializer_class =  ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    

# class StreamPlatformVS(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def destroy(self, request, pk):
#         platform = StreamPlatform.objects.get(pk=pk)
#         platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class StreamPlatformAV(APIView):
    permission_classes = [IsAdminorReadOnly]
    
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StreamPlatformDetailsAV(APIView):
    permission_classes = [IsAdminorReadOnly]
    
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error': 'Platform Details not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class WatchListGV(generics.ListAPIView):
    queryset = Watchlist.objects.all() #this statement is being overridden by get_queryset below
    serializer_class = WatchlistSerializer
    pagination_class = WatchlistCursorPagination
    
    filter_backends = [filters.SearchFilter]
    # filterset_fields = ['title', 'platform__name']
    search_fields = ['title', 'platform__name']
    ordering_fields = ['avg_rating'] 

class WatchListAV(APIView):
    permission_classes = [IsAdminorReadOnly]
    #only admin can access Watchlist others can read only
    
    def get(self, request):
        movies = Watchlist.objects.all()
        serializer = WatchlistSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatchllistDetailsAV(APIView):
    permission_classes = [IsAdminorReadOnly]
    #only admin can access watchlist and edit
    
    def get(self, request, pk):
        try:
            movies = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'Error': 'Watchlist not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchlistSerializer(movies)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        movies = Watchlist.objects.get(pk=pk)
        # in order to update u need to pass the id so respective value is updated
        serializer = WatchlistSerializer(movies, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk ):
        movies = Watchlist.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

    
    
    
    
    
    
    
# @api_view(['GET','POST'])
# def Watchlists_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     if request.method == 'POST':
#         # movies = Movie.objects.all()
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

# @api_view(['GET','PUT','DELETE'])
# def movies_details(request, pk):
#     if request.method == 'GET':
#         try:
#             movies = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error': 'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieSerializer(movies)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     if request.method == 'PUT':
#         movies = Movie.objects.get(pk=pk)
#         # in order to update u need to pass the id so respective value is updated
#         serializer = MovieSerializer(movies, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
#     if request.method == 'DELETE':
#         movies = Movie.objects.get(pk=pk)
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)