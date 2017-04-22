#from models import User, Tip, Board, Brnd, Comp, HairPrd, \
from django.contrib.auth.models import User
from chaeum.models import Profile, Tip, Board, Brnd, Comp, HairPrd, \
    HairPrdReview, NormMed, NormMedReview, SpecMed, SpecMedReview, \
    Clinic, ClinicReview, Surgery, SurgeryReview, ClinicSurgery
from rest_framework import serializers

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('token', 'push_tkn', 'get_push', 'device', 'gender', 'location')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(required=True)
    tips = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='tip-detail',
    )
    boards = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='board-detail',
    )
    link = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='pk', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'tips', 'boards', 'link', 'profile',)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

class TipSerializer(serializers.HyperlinkedModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='tip-detail', lookup_field='pk')

    class Meta:
        model = Tip
        fields = ('tip_id', 'title', 'tip_ctnt', 'img_url', 'inq_cnt',
                  'like_cnt', 'clip_cnt', 'link')

class BoardSeriaizer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ChoiceField(choices=User.objects.values_list('pk', 'id'))
    link = serializers.HyperlinkedIdentityField(view_name='board-detail', lookup_field='pk')

    class Meta:
        model = Board
        fields = ('board_id', 'title', 'contents', 'img_url',
                  'inq_cnt', 'like_cnt', 'clip_cnt', 'user_id', 'link')

class BrndSerializer(serializers.HyperlinkedModelSerializer):
    hairprds = serializers.HyperlinkedIdentityField(view_name='brnd-hairprds')
    normmeds = serializers.HyperlinkedIdentityField(view_name='brnd-normmeds')
    specmeds = serializers.HyperlinkedIdentityField(view_name='brnd-specmeds')
    link = serializers.HyperlinkedIdentityField(view_name='brnd-detail', lookup_field='pk')

    class Meta:
        model = Brnd
        fields = ('brnd_id', 'brnd_nm', 'like_cnt', 'hairprds', 'normmeds', 'specmeds', 'link')

class CompSerializer(serializers.HyperlinkedModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='comp-detail', lookup_field='pk')

    class Meta:
        model = Comp
        fields = ('comp_id', 'comp_nm', 'link')

class HairPrdSerializer(serializers.HyperlinkedModelSerializer):
    comps = CompSerializer(many=True, read_only=True)
    brnd_id = serializers.ChoiceField(choices=Brnd.objects.values_list('pk', 'brnd_id'))
    reviews = serializers.HyperlinkedIdentityField(view_name='hairprd-hairprdreviews')
    link = serializers.HyperlinkedIdentityField(view_name='hairprd-detail', lookup_field='pk')

    class Meta:
        model = HairPrd
        fields = ('hairprd_id', 'hairprd_nm', 'price', 'cap', 'inq_cnt',
                  'clip_cnt', 'like_cnt', 'img_url', 'brnd_id', 'reviews', 'comps', 'link')

class HairPrdReviewSerializer(serializers.HyperlinkedModelSerializer):
    hairprd_id = serializers.ChoiceField(choices=HairPrd.objects.values_list('pk', 'hairprd_id'))
    user_id = serializers.ChoiceField(choices=User.objects.values_list('pk', 'id'))
    link = serializers.HyperlinkedIdentityField(view_name='hairprdreview-detail', lookup_field='pk')

    class Meta:
        model = HairPrdReview
        fields = ('review_id', 'score', 'good_thing', 'bad_thing', 'tips', 'inq_cnt',
                  'clip_cnt', 'like_cnt', 'img_url', 'reg_date', 'mod_date', 'hairprd_id', 'user_id', 'link')

class NormMedSerializer(serializers.HyperlinkedModelSerializer):
    comps = CompSerializer(many=True, read_only=True)
    brnd_id = serializers.ChoiceField(choices=Brnd.objects.values_list('pk', 'brnd_id'))
    reviews = serializers.HyperlinkedIdentityField(view_name='normmed-normmedreviews')
    link = serializers.HyperlinkedIdentityField(view_name='normmed-detail', lookup_field='pk')

    class Meta:
        model = NormMed
        fields = ('normmed_id', 'normmed_nm', 'inq_cnt', 'clip_cnt', 'like_cnt', 'img_url',
                  'insur_yn', 'effect', 'usg_cap', 'forbid', 'careful_med', 'side_effect', 'brnd_id', 'reviews', 'comps', 'link')

class NormMedReviewSerializer(serializers.HyperlinkedModelSerializer):
    normmed_id = serializers.ChoiceField(choices=NormMed.objects.values_list('pk', 'normmed_id'))
    user_id = serializers.ChoiceField(choices=User.objects.values_list('pk', 'id'))
    link = serializers.HyperlinkedIdentityField(view_name='normmedreview-detail', lookup_field='pk')

    class Meta:
        model = NormMedReview
        fields = ('review_id', 'score', 'good_thing', 'bad_thing', 'tips', 'inq_cnt',
                  'clip_cnt', 'like_cnt', 'img_url', 'reg_date', 'mod_date', 'normmed_id', 'user_id', 'link')

class SpecMedSerializer(serializers.HyperlinkedModelSerializer):
    comps = CompSerializer(many=True, read_only=True)
    brnd_id = serializers.ChoiceField(choices=Brnd.objects.values_list('pk', 'brnd_id'))
    reviews = serializers.HyperlinkedIdentityField(view_name='specmed-specmedreviews')
    link = serializers.HyperlinkedIdentityField(view_name='specmed-detail', lookup_field='pk')

    class Meta:
        model = SpecMed
        fields = ('specmed_id', 'specmed_nm', 'inq_cnt', 'clip_cnt', 'like_cnt', 'img_url',
                  'insur_yn', 'effect', 'usg_cap', 'forbid', 'careful_med', 'side_effect', 'brnd_id', 'reviews', 'comps', 'link')

class SpecMedReviewSerializer(serializers.HyperlinkedModelSerializer):
    specmed_id = serializers.ChoiceField(choices=SpecMed.objects.values_list('pk', 'specmed_id'))
    user_id = serializers.ChoiceField(choices=User.objects.values_list('pk', 'id'))
    link = serializers.HyperlinkedIdentityField(view_name='specmedreview-detail', lookup_field='pk')

    class Meta:
        model = SpecMedReview
        fields = ('review_id', 'score', 'good_thing', 'bad_thing', 'tips', 'inq_cnt',
                  'clip_cnt', 'like_cnt', 'img_url', 'reg_date', 'mod_date', 'specmed_id', 'user_id', 'link')

class SurgerySerializer(serializers.HyperlinkedModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='surgery-detail', lookup_field='pk')

    class Meta:
        model = Surgery
        fields = ('surgery_id', 'surgery_nm', 'inq_cnt', 'clip_cnt', 'like_cnt', 'reg_date', 'mod_date', 'link')

class SurgeryReviewSerializer(serializers.HyperlinkedModelSerializer):
    surgery_id = serializers.ChoiceField(choices=Surgery.objects.values_list('pk', 'surgery_id'))
    user_id = serializers.ChoiceField(choices=User.objects.values_list('pk', 'id'))
    link = serializers.HyperlinkedIdentityField(view_name='surgeryreview-detail', lookup_field='pk')

    class Meta:
        model = SurgeryReview
        fields = ('review_id', 'score', 'good_thing', 'bad_thing', 'tips', 'inq_cnt',
                  'clip_cnt', 'like_cnt', 'img_url', 'reg_date', 'mod_date', 'surgery_id', 'user_id', 'link')

class ClinicSerializer(serializers.HyperlinkedModelSerializer):
    surgeries = SurgerySerializer(many=True, read_only=True)
    link = serializers.HyperlinkedIdentityField(view_name='clinic-detail', lookup_field='pk')

    class Meta:
        model = Clinic
        fields = ('clinic_id', 'clinic_nm', 'region', 'address', 'phone_number', 'inq_cnt', 'clip_cnt', 'like_cnt',
                  'img_url', 'reg_date', 'mod_date', 'surgeries', 'link')

class ClinicReviewSerializer(serializers.HyperlinkedModelSerializer):
    clinic_id = serializers.ChoiceField(choices=Clinic.objects.values_list('pk', 'clinic_id'))
    user_id = serializers.ChoiceField(choices=User.objects.values_list('pk', 'id'))
    link = serializers.HyperlinkedIdentityField(view_name='clinicreview-detail', lookup_field='pk')

    class Meta:
        model = ClinicReview
        fields = ('review_id', 'score', 'good_thing', 'bad_thing', 'tips', 'inq_cnt',
                  'clip_cnt', 'like_cnt', 'img_url', 'reg_date', 'mod_date', 'clinic_id', 'user_id', 'link')

class ClinicSurgerySerializer(serializers.HyperlinkedModelSerializer):
    clinic_id = serializers.IntegerField()
    surgery_id = serializers.IntegerField()

    class Meta:
        model = ClinicSurgery
        fields = ('clinic_id', 'surgery_id')