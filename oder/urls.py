from django.urls import path, include
from rest_framework import permissions

from oder import views
from rest_framework.urlpatterns import format_suffix_patterns
# 使用rest框架自带的路由器生成路由列表
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(  # 文档视图
    openapi.Info(
        title='SQTP API DOC',
        default_version='v1',
        description='SQTP接口文档',
        terms_of_service='',
        contact=openapi.Contact(email='', url=''),
        license=openapi.License(name='')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

router = DefaultRouter()
urlpatterns = [
    # path('requests/',views.RequestList.as_view()), #视图类需要调用as_view转化
    # path('requests/<int:pk>',views.RequestDetail.as_view()),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),
    # 注册
    path('register/', views.register),
]
# urlpatterns = format_suffix_patterns(urlpatterns) #重写路由