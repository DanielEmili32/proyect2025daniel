from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer, MyTokenObtainPairSerializer

# Vista protegida
class VistaProtegida(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'message': '¡Acceso autorizado!',
            'user': request.user.username,
            'email': request.user.email
        })
# Registro de usuarios
class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

# Token obtain pair personalizado (añade claims)
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Logout (blacklist del refresh token)
class LogoutViewAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Espera un body JSON con { "refresh": "<refresh_token>" }
        Revoca / blacklist del refresh token.
        """
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"detail": "Refresh token required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logged out successfully."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": "Invalid token or already blacklisted."}, status=status.HTTP_400_BAD_REQUEST)
