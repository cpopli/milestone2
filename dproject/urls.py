from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^', include('dapp.urls')),
]
