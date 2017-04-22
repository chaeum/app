from django.conf.urls import url, include
from django.shortcuts import render_to_response
from chaeum import views
from rest_framework import routers
#from rest_framework.authtoken import views as auth_token_views
from rest_framework_expiring_authtoken import views as expiring_auth_token_views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'magazines', views.MagazineViewSet)
router.register(r'brnds', views.BrndViewSet)
router.register(r'hairprds', views.HairPrdViewSet)
router.register(r'normmeds', views.NormMedViewSet)
router.register(r'etcmeds', views.EtcMedViewSet)
router.register(r'specmeds', views.SpecMedViewSet)
router.register(r'hairshops', views.HairShopViewSet)
router.register(r'clinics', views.ClinicViewSet)
router.register(r'reviews', views.ReviewViewSet)
#router.register(r'images', views.ImageViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api-token-auth/', auth_token_views.obtain_auth_token)
    url(r'^api-token-auth/', expiring_auth_token_views.obtain_expiring_auth_token)
]
