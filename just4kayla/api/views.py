from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def getRoute(request):
    routes  = [
        {
            'Endpoint': '/notes/date',
            'method': 'GET',
            'body': None,
            'description': 'Returns notes for specific day'
        },
        {
            'Endpoint': '/notes/addnew',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'adds new notes to db'

        },
        {
            'Endpoint': '/notes/id/deletenote',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes current note'
        }
    ]
    return JsonResponse(routes, safe=False)