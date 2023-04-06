from rest_framework import serializers
from .models import Student


# validators
def start_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError('Name should be start with R.')        

class StudentSerializer(serializers.Serializer):
    
    name=serializers.CharField(max_length=100,validators=[start_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    

    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        print(instance.name) # before update data
        instance.name=validated_data.get('name',instance.name)
        print(instance.name)# after update data
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    def validate_roll(self,value) :
     if value>=200:
      raise serializers.ValidationError('Seat Full')
     return value
   
    
    def validate(self, data):
        nm=data.get('name')
        ct=data.get('city')
        
        if nm.lower()=='raj' and ct.lower()!='rajshthan':
            raise serializers.ValidationError('City Must be Rajsthan.')
        return data
       
    
  