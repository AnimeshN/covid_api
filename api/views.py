from django.shortcuts import render
from django.http import JsonResponse, Http404

from rest_framework.decorators import api_view, authentication_classes, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from .serializers import Hospbedserializer
from .models import Hospbeds

from django.core.exceptions import ValidationError

from rest_framework import status


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def apiOverview(request):
    api_urls = {
        'List': '/hospital_list/',
        'Detail': '/hospital_details/<str:pk>/',
        'Add': '/hospital_add/',
        'Update': '/hospital_update/<str:pk>/',
        'Delete': '/hospital_delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def HospitalList(request):
    hospitals = Hospbeds.objects.all()
    serializer = Hospbedserializer(hospitals, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def HospitalDetails(request, pk):
    try:
        hospital = Hospbeds.objects.get(id=pk)
        serializer = Hospbedserializer(hospital, many=False)
        return Response(serializer.data)
    except Hospbeds.DoesNotExist:
        raise Http404


@api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def HospitalAdd(request):
    serialize = Hospbedserializer(data=request.data)
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data, status=status.HTTP_201_CREATED)
    return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def HospitalUpdate(request, pk):
    try:
        hospital = Hospbeds.objects.get(id=pk)
        serialize = Hospbedserializer(
            instance=hospital, data=request.data)
        if serialize.is_valid():
            serialize.save()
        return Response(serialize.data)
    except Hospbeds.DoesNotExist:
        raise Http404


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def HospitalDelete(request, pk):
    try:
        hospital = Hospbeds.objects.get(id=pk)
        hospital.delete()
        return Response("deleted item")
    except Hospbeds.DoesNotExist:
        raise Http404