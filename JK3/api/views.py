from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method=='GET':
      json_data=request.body
      stream=io.BytesIO(json_data)
      pythondata=JSONParser().parse(stream)
      id=pythondata.get('id',None)
      if id is not None:
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')  
      stu=Student.objects.all()
      serializer=StudentSerializer(stu,many=True)
      json_data=JSONRenderer().render(serializer.data)
      return HttpResponse(json_data,content_type='application/json')
  
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data is Created.'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        # Complete: Update: --Required All-Data from: Front. End/Client
        # serializer = StudentSerializer(stu, data=pythondata)
        # Partial Update - All Data not required        
        serializer=StudentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data is Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'Data is deleted'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
        #you can use jsonresponse instead of jsonranderer anf httpresponce. like this
        # return JSonResponce(res,safe=true)
    