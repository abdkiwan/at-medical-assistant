
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer

from .voice_to_text import recognize

class FileView(APIView):
  
	parser_classes = (MultiPartParser, FormParser)
	def post(self, request, *args, **kwargs):

		print(type(request.data))

		file_serializer = FileSerializer(data=request.data)
		if file_serializer.is_valid():

			file_serializer.save()

			audio_file_name = '.'+file_serializer.data['file']
			recognized_text = recognize(audio_file_name)
			
			return Response({'recognized_text' : recognized_text}, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)