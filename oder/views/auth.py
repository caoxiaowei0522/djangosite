from django.contrib import auth
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

#注册用户
from oder.serializers import RegisterSerializer


@api_view(['POST'])
def register(request):
    # 获取序列化器
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(): #根据序列器和模型字段综合检查数据是否合法
        user = serializer.register() #创建用户数据
        auth.login(request,user) # 完成用户登录状态设置
        return Response(data={'msg':'register success','is_admin':user.is_superuser,'retcode':status.HTTP_201_CREATED},status=status.HTTP_201_CREATED)
    return Response(data={'msg':'error','retcode':status.HTTP_400_BAD_REQUEST,'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)