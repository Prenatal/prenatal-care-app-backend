from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .renderers import UserJSONRenderer
from .serializers import UserRegistrationSerializer
from rest_framework import generics


class UserRegistrationAPIView(generics.CreateAPIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
