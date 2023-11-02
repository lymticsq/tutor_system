from rest_framework import serializers
from myapp.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    #声明数据
    class Meta:
        model = CustomUser  #进行接口序列化的模型
        fields = '__all__'  #序列化要返回的字段
