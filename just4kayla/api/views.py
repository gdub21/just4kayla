from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def getRoute(request):

    return JsonResponse('our api', safe=False)