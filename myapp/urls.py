from rest_framework.routers import DefaultRouter

from myapp.views import CustomUserViewSet

router = DefaultRouter()    #声明一个默认的路由注册器
router.register(r'users', CustomUserViewSet, basename='user')   #注册好的接口视图

urlpatterns = router.urls