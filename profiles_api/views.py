from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Returns a list of APIVIEW features (objects)"""

        an_apiview = [
            'uses HTTP methods as function (get,post,put,patch,delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'is mapped manually to URLs',

        ]
        return Response({'message': 'hello', 'an_apiview': an_apiview})
