from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import User, UserProfile
from .serializer import UserProfileSerializer, UserSerializer


class ListUsersAPIView(APIView):
    permission_classes = [IsAuthenticated]
    

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "User created successfully",
                "data": serializer.data
            }, status=201)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class DetailUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "User updated successfully",
                "data": serializer.data
            })
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response({
            "message": "User and associated profile deleted successfully"
        }, status=HTTP_204_NO_CONTENT)
