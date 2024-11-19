from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from.models import Habits
from.serializers import HabitsSerializer
# Create your views here.

class HabitsViewSet(viewsets.ViewSet):
    def create(self,request):
        serializer=HabitsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def list(self, request):
        obj=Habits.objects.all()
        serializer=HabitsSerializer(obj,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self ,request,pk=None):
        obj=get_object_or_404(Habits,id=pk)
        serializer=HabitsSerializer(obj)
        return Response(data=serializer.data)
    
    def update(self,request,pk=None):
        obj=get_object_or_404(Habits,id=pk)
        serializer=HabitsSerializer(instance=obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
        
    def partial_update(self,request,pk=None):
        obj=get_object_or_404(Habits,id=pk)
        serializer=HabitsSerializer(instance=obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def destroy(self,request,pk=None):
        obj=get_object_or_404(Habits,id=pk)
        obj.delete()
        return Response(data={"msg:Data Deleted Successfully"})

        
