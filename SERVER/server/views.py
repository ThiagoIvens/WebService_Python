
from .models import Weather
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WeatherSerializer

# Create your views here.
@api_view(['GET'])
def weatherList(request):
    queryset = Weather.objects.all()
    serializer = WeatherSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def weatherDetail(request, pk):
    queryset = Weather.objects.get(id=pk)
    serializer = WeatherSerializer(queryset, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def weatherDetailH(request, hora):
    queryset = Weather.objects.get(hora=hora)
    serializer = WeatherSerializer(queryset, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def weatherCreate(request):
    serializer = WeatherSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def weatherUpdate(request, pk):
    queryset = Weather.objects.get(id=pk)
    serializer = WeatherSerializer(instance=queryset, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def weatherDelete(request, pk):
    queryset = Weather.objects.get(id=pk)
    queryset.delete()

    return Response("Weather deleted")