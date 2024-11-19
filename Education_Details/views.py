from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from.models import Education
from.serializers import EducationSerializer
# Create your views here.

class EduDetailsViewSet(viewsets.ViewSet):
    def create(self,request):
        serializer=EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def list(self, request):
        obj=Education.objects.all()
        serializer=EducationSerializer(obj,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self ,request,pk=None):
        obj=get_object_or_404(Education,id=pk)
        serializer=EducationSerializer(obj)
        return Response(data=serializer.data)
    
    def update(self,request,pk=None):
        obj=get_object_or_404(Education,id=pk)
        serializer=EducationSerializer(instance=obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
        
    def partial_update(self,request,pk=None):
        obj=get_object_or_404(Education,id=pk)
        serializer=EducationSerializer(instance=obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def destroy(self,request,pk=None):
        obj=get_object_or_404(Education,id=pk)
        obj.delete()
        return Response(data={"msg:Data Deleted Successfully"})

        
