from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer
from rest_framework import status

from songs import serializers


@api_view(['GET', 'POST'])
def song_list(request):

    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
def song_detail(request, pk):

    song = get_object_or_404(Song, pk=pk)  #look for the pk of this car table and give us one that's equal to that

    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':

        serializer = SongSerializer(song, data=request.data) # finds song found, updates to data from PUT
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)