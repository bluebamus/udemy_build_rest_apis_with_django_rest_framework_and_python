from django.urls import path, include
from watchlist_app.api.views import (
    WatchListAV,
    WatchDetailAV,
    StreamPlatformAV,
    StreamPlatformDetailAV,
)


urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>/", WatchDetailAV.as_view(), name="movie-details"),
    path("steam/", StreamPlatformAV.as_view(), name="steam"),
    path("steam/<int:pk>/", StreamPlatformDetailAV.as_view(), name="steam-detail"),
]
