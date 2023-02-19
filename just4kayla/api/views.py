from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
@api_view(['GET','POST'])
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
    return Response(routes)
  
@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getNotes(request, pk):
    notes = Note.objects.get(id = pk)
    serializer = NoteSerializer(notes, many = False)
    return Response(serializer.data)