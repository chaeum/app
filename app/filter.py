import django_filters
# from models import User, Tip, Board, Brnd, Comp, HairPrd, \
from django.contrib.auth.models import User
from app.models import Magazine, Brnd, Comp, HairPrd, \
    Clinic

# class UserFilter(django_filters.rest_framework.FilterSet):
#     # usr_id = django_filters.CharFilter(name="usr_id", lookup_expr='exact')
#     usr_id = django_filters.CharFilter(name="id", lookup_expr='exact')
#
#     class Meta:
#         model = User
#         #fields = ['usr_id']
#         fields = ['id']
#
# class MagazineFilter(django_filters.rest_framework.FilterSet):
#     magazine_id = django_filters.NumberFilter(name="magazine_id", lookup_expr='exact')
#     title = django_filters.CharFilter(name="title", lookup_expr='contains')
#     contents = django_filters.CharFilter(name="contents", lookup_expr='contains')
#
#     class Meta:
#         model = Magazine
#         fields = ['magazine_id', 'title', 'contents']
#

class HairPrdFilter(django_filters.rest_framework.FilterSet):
    hairprd_nm = django_filters.CharFilter(name="hairprd_nm", lookup_expr='contains')
    class Meta:
        model = HairPrd
        fields = ("hairprd_nm",)

class MedFIlter(django_filters.rest_framework.FilterSet):
    hairprd_id = django_filters.NumberFilter(name="hairprd_id", lookup_expr='exact')
    hairprd_nm = django_filters.CharFilter(name="hairprd_nm", lookup_expr='contains')

# class ClinicFIlter(django_filters.rest_framework.FilterSet):
#     surgeries = django_filters.CharFilter(name="surgeries__surgery_nm", lookup_expr='contains')
#
#     class Meta:
#         model = Clinic
#         fields = ('clinic_nm', 'surgeries')
#
# class M2MFilter(django_filters.Filter):
#     def filter(self, qs, value):
#         if not value:
#             return qs
#
#         values = value.split(',')
#         for v in values:
#             print v
#             qs = qs.filter(surgery_id=v)
#
#         return qs
#
# class SurgeryFilter(django_filters.FilterSet):
#     surgery_id = M2MFilter(name='surgery_id')
#
#     class Meta:
#         model = Surgery
#         fields = ('surgery_id',)