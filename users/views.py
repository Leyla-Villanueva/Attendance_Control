from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import PasswordRecoverySerializer
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .serializers import PasswordRecoverySerializer
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    renderer_classes = [JSONRenderer]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return [IsAuthenticated()]
        return []


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class PasswordRecoveryView(APIView):
    def post(self, request):
        serializer = PasswordRecoverySerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]

            # Crear el contenido del correo en HTML
            html_message = render_to_string(
                "emails/password_recovery.html", {"username": username}
            )
            plain_message = strip_tags(html_message)  # Convertir el HTML a texto plano

            # Enviar correo al administrador
            send_mail(
                subject="Solicitud de cambio de contraseña",
                message=plain_message,  # Mensaje en texto plano
                from_email="no-reply@attendancecontrol.com",
                recipient_list=["20223tn046@utez.edu.mx"],
                html_message=html_message,  # Mensaje en HTML
            )
            return Response(
                {"message": "Solicitud enviada correctamente."},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordUpdateView(APIView):
    def post(self, request):
        serializer = PasswordUpdateSerializer(data=request.data)
        if serializer.is_valid():
            # Actualizar la contraseña y reactivar al usuario
            new_password = serializer.update_password()
            return Response(
                {
                    "message": "Contraseña actualizada correctamente.",
                    "new_password": new_password,  # Incluir la nueva contraseña en la respuesta
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlockUserView(APIView):
    def post(self, request):
        serializer = UserBlockSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.block_user()
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
