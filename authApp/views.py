from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from rest_framework.authentication import SessionAuthentication




class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self,request):
        return  



class SignUpUser(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [AllowAny]  

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "status_code": status.HTTP_201_CREATED,
                    "message": "User created successfully",
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                "success": False,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "message": "Signup failed",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    


class LoginUser(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [AllowAny]  

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response(
                {
                    "success": True,
                    "status_code": status.HTTP_200_OK,
                    "message": "Login successful",
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "success": False,
                "status_code": status.HTTP_401_UNAUTHORIZED,
                "message": "Invalid username or password"
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    


class LogoutUser(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)  

        response = Response({
            "success": True,
            "status_code": status.HTTP_200_OK,
            "message": "Logged out successfully"
        }, status=status.HTTP_200_OK)

        response.delete_cookie("sessionid")  
        return response