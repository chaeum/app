#from models import User, Tip, Board, Brnd, Comp, HairPrd, \
from django.contrib.auth.models import User
from chaeum.models import Profile, Magazine, Brnd, Comp, CompList, HairPrd, \
    Medicine, HairShop, HairPrgSet, HairPrg, \
    Clinic, ClinicPrg, Review, Like, Image
from rest_framework import serializers

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('nickname', 'birth', 'app_type', 'push_tkn', 'push_yn', 'device', 'gender', 'location')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(required=True)
    # magazines = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='magazine-detail',
    # )
    # boards = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='board-detail',
    # )
    link = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='pk', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'link', 'profile')
        # fields = ('id', 'username', 'magazines', 'boards', 'link', 'profile',)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

class MagazineSerializer(serializers.HyperlinkedModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='magazine-detail', lookup_field='pk')

    class Meta:
        model = Magazine
        fields = ('magazine_id', 'title', 'contents', 'like_cnt',
                  'reg_date', 'mod_date', 'link')

class BrndSerializer(serializers.HyperlinkedModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='brnd-detail', lookup_field='pk')

    class Meta:
        model = Brnd
        fields = ('brnd_id', 'brnd_nm', 'like_cnt', 'link')

class CompSerializer(serializers.HyperlinkedModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='comp-detail', lookup_field='pk')

    class Meta:
        model = Comp
        fields = ('comp_id', 'comp_hg_nm', 'comp_nm', 'grade', 'link')

class CompListSerializer(serializers.HyperlinkedModelSerializer):
    comp_id = serializers.ChoiceField(choices=Comp.objects.values_list('comp_id', 'comp_nm'), required=True)
    hairprd_id = serializers.ChoiceField(choices=HairPrd.objects.values_list('hairprd_id', 'hairprd_nm'), allow_blank=True)
    med_id = serializers.ChoiceField(choices=Medicine.objects.values_list('med_id', 'med_nm'), allow_blank=True)
    # normmed_id = serializers.ChoiceField(choices=NormMed.objects.values_list('med_id', 'med_nm'), allow_blank=True)
    # etcmed_id = serializers.ChoiceField(choices=EtcMed.objects.values_list('med_id', 'med_nm'), allow_blank=True)
    # specmed_id = serializers.ChoiceField(choices=SpecMed.objects.values_list('med_id', 'med_nm'), allow_blank=True)
    class Meta:
        model = CompList
        fields = ('complist_id', 'category', 'comp_id', 'hairprd_id', 'med_id')
                  #'normmed_id', 'etcmed_id', 'specmed_id')

class HairPrdSerializer(serializers.HyperlinkedModelSerializer):
    brnd_id = serializers.ChoiceField(choices=Brnd.objects.values_list('brnd_id', 'brnd_nm'))
    link = serializers.HyperlinkedIdentityField(view_name='hairprd-detail', lookup_field='pk')

    class Meta:
        model = HairPrd
        fields = ('hairprd_id', 'hairprd_nm', 'price', 'cap',
                  'like_cnt', 'reg_date', 'brnd_id', 'link')

class NormMedSerializer(serializers.HyperlinkedModelSerializer):
    #brnd_id = serializers.ChoiceField(choices=Brnd.objects.values_list('pk', 'brnd_id'))
    brnd_making_id = serializers.ChoiceField(choices=Brnd.objects.values_list('brnd_id', 'brnd_nm'))
    brnd_sales_id = serializers.ChoiceField(choices=Brnd.objects.values_list('brnd_id', 'brnd_nm'))
    #link = serializers.HyperlinkedIdentityField(view_name='normmed-detail', lookup_field='pk')

    class Meta:
        #model = NormMed
        model = Medicine(category='1')
        fields = ('med_id', 'med_nm', 'like_cnt', 'effect', 'usg_cap', 'forbid', 'side_effect',
                  'reg_date', 'brnd_making_id', 'brnd_sales_id')

class EtcMedSerializer(serializers.HyperlinkedModelSerializer):
    #brnd_id = serializers.ChoiceField(choices=Brnd.objects.values_list('pk', 'brnd_id'))
    brnd_making_id = serializers.ChoiceField(choices=Brnd.objects.values_list('brnd_id', 'brnd_nm'))
    brnd_sales_id = serializers.ChoiceField(choices=Brnd.objects.values_list('brnd_id', 'brnd_nm'))
    #link = serializers.HyperlinkedIdentityField(view_name='etcmed-detail', lookup_field='pk')

    class Meta:
        model = Medicine(category='2')
        fields = ('med_id', 'med_nm', 'like_cnt', 'effect', 'usg_cap', 'forbid', 'side_effect',
                  #'insur_yn', 'effect', 'usg_cap', 'forbid', 'careful_med', 'side_effect', 'brnd_id', 'reviews', 'comps', 'link')
                  'reg_date', 'brnd_making_id', 'brnd_sales_id')

class SpecMedSerializer(serializers.HyperlinkedModelSerializer):
    brnd_making_id = serializers.ChoiceField(choices=Brnd.objects.values_list('brnd_id', 'brnd_nm'))
    brnd_sales_id = serializers.ChoiceField(choices=Brnd.objects.values_list('brnd_id', 'brnd_nm'))
    #link = serializers.HyperlinkedIdentityField(view_name='specmed-detail', lookup_field='pk')

    class Meta:
        model = Medicine(category='3')
        fields = ('med_id', 'med_nm', 'like_cnt', 'insur_yn', 'effect', 'usg_cap', 'forbid',
                  'careful_med', 'side_effect', 'brnd_making_id', 'brnd_sales_id')

class MedicineSerializer(serializers.HyperlinkedModelSerializer):
    brnd_making_id = serializers.ChoiceField(choices=Brnd.objects.values_list('brnd_id', 'brnd_nm'))
    brnd_sales_id = serializers.ChoiceField(choices=Brnd.objects.values_list('brnd_id', 'brnd_nm'))
    link = serializers.HyperlinkedIdentityField(view_name='medicine-detail', lookup_field='pk')

    class Meta:
        model = Medicine
        fields = ('med_id', 'med_nm', 'category', 'detail_category', 'like_cnt', 'insur_yn', 'effect', 'usg_cap',
                  'forbid', 'careful_med', 'side_effect', 'brnd_making_id', 'brnd_sales_id', 'link')

class HairShopSerializer(serializers.HyperlinkedModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='hairshop-detail', lookup_field='pk')

    class Meta:
        model = HairShop
        fields = ('hairshop_id', 'hairshop_nm', 'region', 'address', 'like_cnt',
                  'phone_num', 'mobile_num', 'kakao_id', 'reg_date', 'link')

class HairPrgSetSerializer(serializers.HyperlinkedModelSerializer):
    hairshop_id = serializers.ChoiceField(choices=HairShop.objects.values_list('hairshop_id', 'hairshop_nm'))
    link = serializers.HyperlinkedIdentityField(view_name='hairprgset-detail', lookup_field='pk')

    class Meta:
        model = HairPrgSet
        fields = ('prgset_id', 'prgset_nm', 'hairshop_id', 'link')

class HairPrgSerializer(serializers.HyperlinkedModelSerializer):
    prgset_id = serializers.ChoiceField(choices=HairPrgSet.objects.values_list('prgset_id', 'prgset_nm'))
    link = serializers.HyperlinkedIdentityField(view_name='hairprg-detail', lookup_field='pk')

    class Meta:
        model = HairPrg
        fields = ('prg_id', 'prg_nm', 'prgset_id', 'link')

class ClinicSerializer(serializers.HyperlinkedModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='clinic-detail', lookup_field='pk')

    class Meta:
        model = Clinic
        fields = ('clinic_id', 'clinic_nm', 'region', 'address', 'type', 'like_cnt',
                  'phone_num', 'mobile_num', 'kakao_id', 'reg_date', 'link')

class ClinicPrgSerializer(serializers.HyperlinkedModelSerializer):
    clinic_id = serializers.ChoiceField(choices=Clinic.objects.values_list('clinic_id', 'clinic_nm'))
    link = serializers.HyperlinkedIdentityField(view_name='clinicprg-detail', lookup_field='pk')

    class Meta:
        model = ClinicPrg
        fields = ('prg_id', 'prg_nm', 'link')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    owner_id = serializers.ChoiceField(choices=User.objects.values_list('pk', 'username'))
    hairprd_id = serializers.ChoiceField(choices=HairPrd.objects.values_list('hairprd_id', 'hairprd_nm'), allow_null=True)
    med_id = serializers.ChoiceField(choices=Medicine.objects.values_list('med_id', 'med_nm'), allow_null=True)
    # normmed_id = serializers.ChoiceField(choices=NormMed.objects.values_list('med_id', 'med_nm'), allow_null=True)
    # etcmed_id = serializers.ChoiceField(choices=EtcMed.objects.values_list('med_id', 'med_nm'), allow_null=True)
    # specmed_id = serializers.ChoiceField(choices=SpecMed.objects.values_list('med_id', 'med_nm'), allow_null=True)
    hairshop_id = serializers.ChoiceField(choices=HairShop.objects.values_list('hairshop_id', 'hairshop_nm'), allow_null=True)
    clinic_id = serializers.ChoiceField(choices=Clinic.objects.values_list('clinic_id', 'clinic_nm'), allow_null=True)
    link = serializers.HyperlinkedIdentityField(view_name='review-detail', lookup_field='pk')

    class Meta:
        model = Review
        fields = ('review_id', 'category', 'contents', 'score', 'like_cnt', 'reg_date', 'mod_date',
                  'owner_id', 'hairprd_id', 'med_id', 'hairshop_id', 'clinic_id', 'link')
                  #'owner_id', 'hairprd_id', 'normmed_id', 'etcmed_id', 'specmed_id', 'hairshop_id', 'clinic_id', 'link')

# class ImageSerializer(serializers.HyperlinkedModelSerializer):
#
#     image = serializers.ImageField(max_length=None, use_url=True)
#
#     class Meta:
#         model = Image
#         fields = ('id', 'name', 'image', 'owner')