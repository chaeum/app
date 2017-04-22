from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

# class User(models.Model):
#     DEVICE = (
#         ('A', 'Android'),
#         ('I', 'IOS'),
#     )
#     GENDER = (
#         ('M', 'Man'),
#         ('W', 'Woman'),
#     )
#     usr_id = models.CharField(max_length=50, primary_key=True)
#     usr_nm = models.CharField(max_length=50)
#     push_tkn = models.CharField(max_length=200)
#     get_push = models.CharField(max_length=1)
#     device = models.CharField(max_length=1, choices=DEVICE)
#     gender = models.CharField(max_length=1, choices=GENDER)
#     region = models.CharField(max_length=200)
#     reg_date = models.DateTimeField(auto_now_add=True, blank=True)
#     mod_date = models.DateTimeField(auto_now_add=True, blank=True)
#
#     class Meta:
#         db_table = 'TBUSER'

class Profile(models.Model):
    GET_PUSH = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    DEVICE = (
        ('A', 'Android'),
        ('I', 'IOS'),
    )
    GENDER = (
        ('M', 'Man'),
        ('W', 'Woman'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=200)
    push_tkn = models.CharField(max_length=200)
    get_push = models.CharField(max_length=1, choices=GET_PUSH)
    device = models.CharField(max_length=1, choices=DEVICE)
    gender = models.CharField(max_length=1, choices=GENDER)
    location = models.CharField(max_length=200)


class Tip(models.Model):
    tip_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    tip_ctnt = models.CharField(max_length=4000)
    img_url = models.CharField(max_length=200)
    inq_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    clip_cnt = models.IntegerField()
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    mod_date = models.DateTimeField(auto_now_add=True, blank=True)
    usr = models.ForeignKey(User, related_name='tips', on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBTIP'

class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=4000)
    img_url = models.CharField(max_length=200)
    inq_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    clip_cnt = models.IntegerField()
    user = models.ForeignKey(User, related_name='boards', on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBBOARD'

class Brnd(models.Model):
    brnd_id = models.AutoField(primary_key=True)
    brnd_nm = models.CharField(max_length=50)
    like_cnt = models.IntegerField()

    class Meta:
        db_table = 'TBBRND'

class Comp(models.Model):
    comp_id = models.AutoField(primary_key=True)
    comp_nm = models.CharField(max_length=50)

    class Meta:
        db_table = 'TBCOMP'

class HairPrd(models.Model):
    hairprd_id = models.AutoField(primary_key=True)
    hairprd_nm = models.CharField(max_length=50)
    price = models.IntegerField()
    cap = models.IntegerField()
    inq_cnt = models.IntegerField()
    clip_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    img_url = models.CharField(max_length=200)
    brnd = models.ForeignKey(Brnd, related_name='hairprds', on_delete=models.CASCADE)
    comp = models.ManyToManyField(Comp)

    class Meta:
        db_table = 'TBHAIRPRD'

class HairPrdReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    good_thing = models.CharField(max_length=500)
    bad_thing = models.CharField(max_length=500)
    tips = models.CharField(max_length=500)
    inq_cnt = models.IntegerField()
    clip_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    img_url = models.CharField(max_length=200)
    reg_date = models.DateTimeField()
    mod_date = models.DateTimeField(auto_now_add=True, blank=True)
    usr = models.ForeignKey(User, related_name='hairprdrv_usr', on_delete=models.CASCADE)
    hairprd = models.ForeignKey(HairPrd, related_name='hairprdrv_hairprd', on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBHAIRPRDREVIEW'

class NormMed(models.Model):
    normmed_id = models.AutoField(primary_key=True)
    normmed_nm = models.CharField(max_length=200)
    inq_cnt = models.IntegerField()
    clip_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    img_url = models.CharField(max_length=200)
    insur_yn = models.CharField(max_length=1)
    effect = models.CharField(max_length=500)
    usg_cap = models.CharField(max_length=500)
    forbid = models.CharField(max_length=500)
    careful_med = models.CharField(max_length=500)
    side_effect = models.CharField(max_length=500)
    brnd = models.ForeignKey(Brnd, related_name='normmeds', on_delete=models.CASCADE)
    comp = models.ManyToManyField(Comp)

    class Meta:
        db_table = 'TBNORMMED'

class NormMedReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    good_thing = models.CharField(max_length=500)
    bad_thing = models.CharField(max_length=500)
    tips = models.CharField(max_length=500)
    inq_cnt = models.IntegerField()
    clip_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    img_url = models.CharField(max_length=200)
    reg_date = models.DateTimeField()
    mod_date = models.DateTimeField(auto_now_add=True, blank=True)
    usr = models.ForeignKey(User, related_name='normmedrv_usr', on_delete=models.CASCADE)
    normmed = models.ForeignKey(NormMed, related_name='normmedrv_normmed', on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBNORMMEDREVIEW'

class SpecMed(models.Model):
    specmed_id = models.AutoField(primary_key=True)
    specmed_nm = models.CharField(max_length=200)
    inq_cnt = models.IntegerField()
    clip_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    img_url = models.CharField(max_length=200)
    insur_yn = models.CharField(max_length=1)
    effect = models.CharField(max_length=500)
    usg_cap = models.CharField(max_length=500)
    forbid = models.CharField(max_length=500)
    careful_med = models.CharField(max_length=500)
    side_effect = models.CharField(max_length=500)
    brnd = models.ForeignKey(Brnd, related_name='specmeds', on_delete=models.CASCADE)
    comp = models.ManyToManyField(Comp)

    class Meta:
        db_table = 'TBSPECMED'

class SpecMedReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    good_thing = models.CharField(max_length=500)
    bad_thing = models.CharField(max_length=500)
    tips = models.CharField(max_length=500)
    inq_cnt = models.IntegerField()
    clip_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    img_url = models.CharField(max_length=200)
    reg_date = models.DateTimeField()
    mod_date = models.DateTimeField(auto_now_add=True, blank=True)
    usr = models.ForeignKey(User, related_name='specmedrv_usr', on_delete=models.CASCADE)
    specmed = models.ForeignKey(SpecMed, related_name='specmedrv_specmed', on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBSPECMEDREVIEW'


class HairShop(models.Model):
    hairshop_id = models.AutoField(primary_key=True)
    hairshop_nm = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    inq_cnt = models.IntegerField()
    clip_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    img_url = models.CharField(max_length=200)
    reg_date = models.DateTimeField()
    mod_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'TBHAIRSHOP'

class HairShopReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    good_thing = models.CharField(max_length=500)
    bad_thing = models.CharField(max_length=500)
    tips = models.CharField(max_length=500)
    inq_cnt = models.IntegerField()
    clip_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    img_url = models.CharField(max_length=200)
    reg_date = models.DateTimeField()
    mod_date = models.DateTimeField(auto_now_add=True, blank=True)
    usr = models.ForeignKey(User, related_name='hairshoprv_usr', on_delete=models.CASCADE)
    hairshop = models.ForeignKey(SpecMed, related_name='hairshoprv_hairshop', on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBHAIRSHOPREVIEW'

class HairPrgSet(models.Model):
    hairprgset_id = models.AutoField(primary_key=True)
    hairprgset_nm = models.CharField(max_length=200)
    hairshop = models.ForeignKey(HairShop, related_name='hairprgset_hairshop', on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBHAIRPRGSET'

class HairPrg(models.Model):
    hairprg_id = models.AutoField(primary_key=True)
    hairprg_nm = models.CharField(max_length=200)
    hairprgset = models.ForeignKey(HairShop, related_name='hairprg_hairprgset', on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBHAIRPRG'

class Surgery(models.Model):
    surgery_id = models.AutoField(primary_key=True)
    surgery_nm = models.CharField(max_length=200)
    inq_cnt = models.IntegerField()
    clip_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    reg_date = models.DateTimeField()
    mod_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'TBSURGERY'

class SurgeryReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    good_thing = models.CharField(max_length=500)
    bad_thing = models.CharField(max_length=500)
    tips = models.CharField(max_length=500)
    inq_cnt = models.IntegerField()
    clip_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    img_url = models.CharField(max_length=200)
    reg_date = models.DateTimeField()
    mod_date = models.DateTimeField(auto_now_add=True, blank=True)
    usr = models.ForeignKey(User, related_name='surgeryrv_usr', on_delete=models.CASCADE)
    surgery = models.ForeignKey(Surgery, related_name='surgeryrv_surgery', on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBSURGERYREVIEW'

class Clinic(models.Model):
    clinic_id = models.AutoField(primary_key=True)
    clinic_nm = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    inq_cnt = models.IntegerField()
    clip_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    img_url = models.CharField(max_length=200)
    reg_date = models.DateTimeField()
    mod_date = models.DateTimeField(auto_now_add=True, blank=True)
    surgeries = models.ManyToManyField(Surgery, through='ClinicSurgery')

    class Meta:
        db_table = 'TBCLINIC'

class ClinicReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    good_thing = models.CharField(max_length=500)
    bad_thing = models.CharField(max_length=500)
    tips = models.CharField(max_length=500)
    inq_cnt = models.IntegerField()
    clip_cnt = models.IntegerField()
    like_cnt = models.IntegerField()
    img_url = models.CharField(max_length=200)
    reg_date = models.DateTimeField()
    mod_date = models.DateTimeField(auto_now_add=True, blank=True)
    usr = models.ForeignKey(User, related_name='clinicrv_usr', on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, related_name='clinicrv_clinic', on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBCLINICREVIEW'

class ClinicSurgery(models.Model):
    clinic = models.ForeignKey('Clinic')
    surgery = models.ForeignKey('Surgery')

    class Meta:
        db_table = 'TBCLINICSURGERY'