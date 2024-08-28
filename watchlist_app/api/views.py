from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.models import Watchlists, StreamPlatforms
from watchlist_app.api.serializers import WatchlistSerializer, StreamPlatformSerializer


class StreamPlatform(APIView):
    def get(self, request):
        platform= StreamPlatforms.objects.all()
        serializer= StreamPlatformSerializer(platform, many=True)
        # serializer= StreamPlatformSerializer(platform, many=True, context={'request':request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer= StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class StreamPlatformDetailsAV(APIView):
    def get(self, request, pk):
        try:
            movies= StreamPlatforms.objects.get(pk=pk)
        except StreamPlatforms.DoesNotExist:
            return Response({'error': 'StreamPlatform not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer= StreamPlatformSerializer(movies)
        return Response(serializer.data)
    
    def put(self, request, pk):
        streamPlatform= StreamPlatforms.objects.get(pk=pk)
        serializer= StreamPlatformSerializer(streamPlatform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request,pk):
        StreamPlatforms= StreamPlatforms.objects.get(pk=pk)
        StreamPlatforms.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Watchlist(APIView):

    def get(self, request):
        movies= Watchlists.objects.all()
        serializer= WatchlistSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer= WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class WatchlistDetailsAV(APIView):
    def get(self, request, pk):
        try:
            movies= Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'error': 'Watchlist not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer= WatchlistSerializer(movies)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movies= Watchlist.objects.get(pk=pk)
        serializer= WatchlistSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request,pk):
        Watchlist= Watchlist.objects.get(pk=pk)
        Watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
# @api_view(['GET','POST'])
# def Watchlist_list(request):
#     if request.method =='GET':
#         movies= Watchlist.objects.all()
#         serializer= WatchlistSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer= WatchlistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET','PUT','DELETE'])
# def Watchlist_details(request,pk):

#     if request.method =='GET':
#         try:
#             movies= Watchlist.objects.get(pk=pk)
#         except Watchlist.DoesNotExist:
#             return Response({'error': 'Watchlist not found'}, status=status.HTTP_400_BAD_REQUEST)
#         serializer= WatchlistSerializer(movies)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         movies= Watchlist.objects.get(pk=pk)
#         serializer= WatchlistSerializer(movies, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        

#     if request.method == 'DELETE':
#         Watchlist= Watchlist.objects.get(pk=pk)
#         Watchlist.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)