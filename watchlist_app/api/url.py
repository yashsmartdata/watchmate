from django.urls import path
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchlistDetailsAV, Watchlist, StreamPlatform, StreamPlatformDetailsAV

urlpatterns = [
    # path('list/', movie_list, name= 'movie-list'),
    # path('<int:pk>', movie_details, name= 'movie-details'),
    path('list/', Watchlist.as_view(), name= 'movie-list'),
    path('<int:pk>', WatchlistDetailsAV.as_view(), name= 'movie-details'),
    path('stream/', StreamPlatform.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name='stream')
]