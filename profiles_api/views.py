from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status


class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIVIEW features (objects)"""

        an_apiview = [
            'uses HTTP methods as function (get,post,put,patch,delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'is mapped manually to URLs',

        ]
        return Response({'message': 'hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handling updating object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handling a partial update of an object """
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method': 'DELETE'})
