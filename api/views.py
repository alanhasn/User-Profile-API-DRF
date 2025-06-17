from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from .models import UserProfile
from .serializer import UserProfileSerializer


class ListUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self , request):
        profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(profiles , many=True)
        
        return Response(serializer.data)
    
    def post(self , request):
        serializer = UserProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message":"User profile created Successfully"})
        return Response(serializer.errors , status=HTTP_400_BAD_REQUEST)

class DetailUserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self,pk):
        return get_object_or_404(UserProfile , pk=pk)
    
    def get(self , request , pk):
        obj = self.get_object(pk=pk)
        serializer = UserProfileSerializer(obj)
        return Response(serializer.data)

    def put(self , request , pk):
        obj = self.get_object(pk=pk)
        serializer = UserProfileSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors , status=HTTP_400_BAD_REQUEST)

    def delete(self , request , pk):
        obj = self.get_object(pk=pk)
        obj.delete()
        return Response({"detail":"the Profile Deleted Successfully"})