#-*- coding: utf-8 -*-
import itertools
from rest_framework.decorators import detail_route
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.models import User
from chaeum.models import Profile, Magazine, Brnd, Comp, CompList, \
    HairPrd, Medicine, HairShop, HairPrg, HairPrgSet, \
    Clinic, ClinicPrg, Review, Image
from chaeum.serializers import ProfileSerializer, UserSerializer, MagazineSerializer, BrndSerializer, \
    CompSerializer, CompListSerializer, HairPrdSerializer, MedicineSerializer, \
    HairShopSerializer, HairPrgSerializer, HairPrgSetSerializer, ClinicSerializer, ClinicPrgSerializer, ReviewSerializer, \
    NormMedSerializer, EtcMedSerializer, SpecMedSerializer
from rest_framework import viewsets, permissions, authentication
from django_filters import rest_framework as filters
from filter import HairPrdFilter
from pagination import MagazinesResultsSetPagination
from permissions import IsOwnerOrReadOnly, IsOwner

import logging

logger = logging.getLogger(__name__)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    #filter_class = UserFilter

    logger.error('test')

    # @detail_route()
    # # def tips(self, request, pk='usr_id'):
    # def magazines(self, request, pk='id'):
    #     user = self.get_object()
    #     serializer = MagazineSerializer(user.magazines_usr.all(), context={'request': request}, many=True)
    #     return Response(serializer.data)
    #
    # @detail_route()
    # # def specmedreviews(self, request, pk='usr_id'):
    # def specmedreviews(self, request, pk='id'):
    #     user = self.get_object()
    #     serializer = ReviewSerializer(user.specmedrv_usr.all(), context={'request': request}, many=True)
    #     return Response(serializer.data)

class MagazineViewSet(viewsets.ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer

    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    # filter_class = MagazineFilter
    ordering_fields = ('reg_date',)
    permission_classes = (permissions.IsAdminUser,)

    #pagination_class = TipsResultsSetPagination

class BrndViewSet(viewsets.ModelViewSet):
    queryset = Brnd.objects.all()
    serializer_class = BrndSerializer
    permission_classes = (permissions.IsAdminUser,)

    @detail_route()
    def hairprds(self, request, pk='brnd_id'):
        brnd = self.get_object()
        serializer = HairPrdSerializer(brnd.hairprds.all(), context={'request': request}, many=True)
        return Response(serializer.data)

    @detail_route()
    def normmeds(self, request, pk='brnd_id'):
        brnd = self.get_object()
        serializer = NormMedSerializer(brnd.normmeds.all(), context={'request': request}, many=True)
        return Response(serializer.data)

    @detail_route()
    def etcmeds(self, request, pk='brnd_id'):
        brnd = self.get_object()
        serializer = EtcMedSerializer(brnd.etcmeds.all(), context={'request': request}, many=True)
        return Response(serializer.data)

    @detail_route()
    def specmeds(self, request, pk='brnd_id'):
        brnd = self.get_object()
        serializer = SpecMedSerializer(brnd.specmeds.all(), context={'request': request}, many=True)
        return Response(serializer.data)

class CompViewSet(viewsets.ModelViewSet):
    queryset = Comp.objects.all()
    serializer_class = CompSerializer

# comp list all
class CompListViewSet(viewsets.ModelViewSet):
    queryset = CompList.objects.all()
    serializer_class = CompListSerializer

# comp - hairprd
class CompListHairPrdViewSet(viewsets.ModelViewSet):
    queryset = CompList.objects.filter(category="1")

# comp - normmed
class CompListNormMedViewSet(viewsets.ModelViewSet):
    queryset = CompList.objects.filter(category="2")

# comp - etcmed
class CompListEtcMedViewSet(viewsets.ModelViewSet):
    queryset = CompList.objects.filter(category="3")

# comp - specmed
class CompListSpecMedViewSet(viewsets.ModelViewSet):
    queryset = CompList.objects.filter(category="4")

class HairPrdViewSet(viewsets.ModelViewSet):
    queryset = HairPrd.objects.all()
    serializer_class = HairPrdSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('hairprd_nm',)
    # filter_fields = ("hairprd_nm",)
    # filter_class = HairPrdFilter

# class NormMedViewSet(viewsets.ModelViewSet):
#     queryset = NormMed.objects.all()
#     serializer_class = NormMedSerializer
#     filter_backends = (SearchFilter,)
#     search_fields = ('med_nm',)
#
# class EtcMedViewSet(viewsets.ModelViewSet):
#     queryset = EtcMed.objects.all()
#     serializer_class = EtcMedSerializer
#     filter_backends = (SearchFilter,)
#     search_fields = ('med_nm',)
#
# class SpecMedViewSet(viewsets.ModelViewSet):
#     queryset = SpecMed.objects.all()
#     serializer_class = SpecMedSerializer
#     filter_backends = (SearchFilter,)
#     search_fields = ('med_nm',)

class NormMedViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.filter(category="1")
    serializer_class = NormMedSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('med_nm',)

class EtcMedViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.filter(category="2")
    serializer_class = EtcMedSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('med_nm',)

class SpecMedViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.filter(category="3")
    serializer_class = SpecMedSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('med_nm',)

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    filter_backends = (SearchFilter, )
    search_fields = ('med_nm')

# class MedViewSet(viewsets.ModelViewSet):
#     def list(self, request):
#         queryset = list(itertools.chain(NormMed.objects.all(), EtcMed.objects.all(), SpecMed.objects.all()))
#         serializer =

class HairShopViewSet(viewsets.ModelViewSet):
    queryset = HairShop.objects.all()
    serializer_class = HairShopSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('hairshop_nm',)

class HairPrgViewSet(viewsets.ModelViewSet):
    queryset = HairPrg.objects.all()
    serializer_class = HairPrgSerializer

class HairPrgSetViewSet(viewsets.ModelViewSet):
    queryset = HairPrgSet.objects.all()
    serializer_class = HairPrgSetSerializer

class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    filter_fields = ('clinic_id', 'clinic_nm')
    #filter_class = ClinicFIlter

    def get_queryset(self):
        queryset = Clinic.objects.all()
        clinic_ids = self.request.query_params.get('clinic_id')
        if clinic_ids is None:
            return queryset
        clinic_ids = clinic_ids.split(',')
        queryset = queryset.filter(clinic_id__in=clinic_ids)

        return queryset

class ClinicPrgViewSet(viewsets.ModelViewSet):
    queryset = ClinicPrg.objects.all()
    serializer_class = ClinicPrgSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = (permissions.IsAdminUser,)
    logger.error('test')
    permission_classes = (IsOwnerOrReadOnly,)
#
# class ImageViewSet(viewsets.ModelViewSet):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer