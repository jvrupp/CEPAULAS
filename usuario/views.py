from .models import Usuario
# Create your views here.
from rest_framework.response import Response

from rest_framework import generics


from .serializers import RegistroSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class CustomUserListCreateView(generics.ListCreateAPIView):#GET e POST
    queryset = Usuario.objects.all()
    serializer_class = RegistroSerializer

class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):#GET, PUT e DELETE
    queryset = Usuario.objects.all()
    serializer_class = RegistroSerializer


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        custom_user = Usuario.objects.filter(id=user.id).first()
        if custom_user:
            id = custom_user.pk
            email = custom_user.email
            username = custom_user.username

            response_data = {
                "id": id,
                "email": email,
                "username": username
            }
            return Response(response_data, status=200)
        else:
            return Response({"error": "Usuário não encontrado."}, status=404)

