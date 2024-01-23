from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
from .utils import getNoteList, createNote, getSingleNote, UpdateNote, DeleteNote

# List of how the url should look like

# /notes GET
# /notes POST
# /notes/<id> GET
# /notes/<id> PUT
# /notes/<id> DELETE



@api_view(['GET', 'POST'])
def GetNotes(request):
    if request.method == 'GET':
        return getNoteList(request)
    
    if request.method == 'POST':
        return createNote(request)
    

@api_view(['GET', 'PUT', 'DELETE'])
def GetNote(request, pk):
    if request.method == 'GET':
        return getSingleNote(request, pk)
    
    if request.method == 'PUT':
        return UpdateNote(request, pk)
    
    if request.method == 'DELETE':
        return DeleteNote(request, pk)
    

# Get the list of notes
# @api_view(["GET"])
# def GetNotes(request):
#     notes = Note.objects.all().order_by('-updated')
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)

# Get a single note based on an id
# @api_view(["GET"])
# def GetNote(request, pk):
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)

# Create a new post
# @api_view(["POST"])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(
#         body=data['body']
#     )
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)

# Update the note
# @api_view(['PUT'])
# def UpdateNote(request, pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance=note, data=data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# Delete a note
# @api_view(['DELETE'])
# def DeleteNote(request, pk):
#     note = Note.objects.get(id=pk)
#     note.delete()

#     return Response("Note was successfully deleted!")
