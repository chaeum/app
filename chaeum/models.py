from __future__ import unicode_literals

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
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

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Profile(models.Model):
    APP_TYPE = (
        ('K', 'Kakao'),
        ('N', 'Naver'),
        ('G', 'Google'),
    )
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
    nickname = models.CharField(max_length=150)
    birth = models.IntegerField()
    app_type = models.CharField(max_length=1, choices=APP_TYPE)
    push_tkn = models.CharField(max_length=200)
    push_yn = models.CharField(max_length=1, choices=GET_PUSH)
    device = models.CharField(max_length=1, choices=DEVICE)
    gender = models.CharField(max_length=1, choices=GENDER)
    location = models.CharField(max_length=200)

    class Meta:
        db_table = 'TBPROFILE'

class Magazine(models.Model):
    magazine_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=4000)
    like_cnt = models.IntegerField()
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    mod_date = models.DateTimeField()

    class Meta:
        db_table = 'TBMAGAZINE'

class Brnd(models.Model):
    brnd_id = models.AutoField(primary_key=True)
    brnd_nm = models.CharField(max_length=50)
    like_cnt = models.IntegerField()

    class Meta:
        db_table = 'TBBRND'

class Comp(models.Model):
    GRADE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    )

    comp_id = models.AutoField(primary_key=True)
    comp_hg_nm = models.CharField(max_length=50)
    comp_nm = models.CharField(max_length=50)
    grade = models.CharField(max_length=1, choices=GRADE)

    class Meta:
        db_table = 'TBCOMP'

class CompList(models.Model):
    CATEGORY = (
        ('1', 'HairPrd'),
        ('2', 'NormMed'),
        ('3', 'EtcMed'),
        ('4', 'SpecMed'),
    )
    complist_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=1, choices=CATEGORY)
    comp_id = models.IntegerField()
    hairprd_id = models.IntegerField(null=True)
    normmed_id = models.IntegerField(null=True)
    etcmed_id = models.IntegerField(null=True)
    specmed_id = models.IntegerField(null=True)

class HairPrd(models.Model):
    hairprd_id = models.AutoField(primary_key=True)
    hairprd_nm = models.CharField(max_length=50)
    price = models.IntegerField()
    cap = models.IntegerField()
    like_cnt = models.IntegerField()
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    #brnd = models.ForeignKey(Brnd, related_name='hairprds', on_delete=models.CASCADE)
    brnd_id = models.IntegerField()
    #comp = models.ManyToManyField(Comp, db_table='TBHAIRPRD_COMP')
    #like = models.ManyToManyField(User, db_table='TBHAIRPRD_LIKE')

    class Meta:
        db_table = 'TBHAIRPRD'

# class NormMed(models.Model):
#     med_id = models.AutoField(primary_key=True)
#     med_nm = models.CharField(max_length=200)
#     like_cnt = models.IntegerField()
#     effect = models.CharField(max_length=500)
#     usg_cap = models.CharField(max_length=500)
#     forbid = models.CharField(max_length=500)
#     side_effect = models.CharField(max_length=500)
#     reg_date = models.DateTimeField(auto_now_add=True, blank=True)
#     #brnd = models.ForeignKey(Brnd, related_name='normmeds', on_delete=models.CASCADE)
#     brnd_making_id = models.IntegerField()
#     brnd_sales_id = models.IntegerField()
#     #comp = models.ManyToManyField(Comp, db_table='TBNORMMED_COMP')
#     #like = models.ManyToManyField(User, db_table='TBNORMMED_LIKE')
#
#     class Meta:
#         db_table = 'TBNORMMED'
#
# class EtcMed(models.Model):
#     med_id = models.AutoField(primary_key=True)
#     med_nm = models.CharField(max_length=200)
#     like_cnt = models.IntegerField()
#     effect = models.CharField(max_length=500)
#     usg_cap = models.CharField(max_length=500)
#     forbid = models.CharField(max_length=500)
#     side_effect = models.CharField(max_length=500)
#     reg_date = models.DateTimeField(auto_now_add=True, blank=True)
#     #brnd = models.ForeignKey(Brnd, related_name='normmeds', on_delete=models.CASCADE)
#     brnd_making_id = models.IntegerField()
#     brnd_sales_id = models.IntegerField()
#     #comp = models.ManyToManyField(Comp, db_table='TBNORMMED_COMP')
#     #like = models.ManyToManyField(User, db_table='TBNORMMED_LIKE')
#
#     class Meta:
#         db_table = 'TBETCMED'

# class SpecMed(models.Model):
#     med_id = models.AutoField(primary_key=True)
#     med_nm = models.CharField(max_length=200)
#     like_cnt = models.IntegerField()
#     insur_yn = models.CharField(max_length=1)
#     effect = models.CharField(max_length=500)
#     usg_cap = models.CharField(max_length=500)
#     forbid = models.CharField(max_length=500)
#     careful_med = models.CharField(max_length=500)
#     side_effect = models.CharField(max_length=500)
#     reg_date = models.DateTimeField(auto_now_add=True, blank=True)
#     # brnd = models.ForeignKey(Brnd, related_name='specmeds', on_delete=models.CASCADE)
#     brnd_making_id = models.IntegerField()
#     brnd_sales_id = models.IntegerField()
#     # comp = models.ManyToManyField(Comp, db_table='TBSPECMED_COMP')
#     # like = models.ManyToManyField(User, db_table='TBSPECMED_LIKE')
#
#     class Meta:
#         db_table = 'TBSPECMED'

class Medicine(models.Model):
    CATEGORY = (
        ('1', 'NormMed'),
        ('2', 'EtcMed'),
        ('3', 'SpecMed'),
    )
    DETAIL_CATEGORY = (
        ('1', 'Duta'),
        ('2', 'Fina'),
    )
    INSUR_YN = (
        ('Y', 'Yes'),
        ('N', 'No')
    )

    med_id = models.AutoField(primary_key=True)
    med_nm = models.CharField(max_length=200)
    category = models.CharField(max_length=1, choices=CATEGORY)
    #### special only ####
    detail_category = models.CharField(max_length=1, choices=DETAIL_CATEGORY, null=True)
    like_cnt = models.IntegerField()
    #### special only ####
    insur_yn = models.CharField(max_length=1, choices=INSUR_YN, null=True)
    effect = models.CharField(max_length=500)
    usg_cap = models.CharField(max_length=500)
    forbid = models.CharField(max_length=500)
    #### special only ####
    careful_med = models.CharField(max_length=500, null=True)
    side_effect = models.CharField(max_length=500)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    # brnd = models.ForeignKey(Brnd, related_name='specmeds', on_delete=models.CASCADE)
    brnd_making_id = models.IntegerField()
    brnd_sales_id = models.IntegerField()
    # comp = models.ManyToManyField(Comp, db_table='TBSPECMED_COMP')
    # like = models.ManyToManyField(User, db_table='TBSPECMED_LIKE')

    class Meta:
        db_table = 'TBMEDICINE'

class HairShop(models.Model):
    hairshop_id = models.AutoField(primary_key=True)
    hairshop_nm = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    like_cnt = models.IntegerField()
    phone_num = models.CharField(max_length=11)
    mobile_num = models.CharField(max_length=11)
    kakao_id = models.CharField(max_length=20)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'TBHAIRSHOP'

class HairPrgSet(models.Model):
    prgset_id = models.AutoField(primary_key=True)
    prgset_nm = models.CharField(max_length=200)
    # hairshop = models.ForeignKey(HairShop, related_name='hairprgset_hairshop', on_delete=models.CASCADE)
    hairshop_id = models.IntegerField()

    class Meta:
        db_table = 'TBHAIRSHOP_PRGSET'

class HairPrg(models.Model):
    prg_id = models.AutoField(primary_key=True)
    prg_nm = models.CharField(max_length=200)
    # prgset = models.ForeignKey(HairPrgSet, related_name='prg_prgset', on_delete=models.CASCADE)
    prgset_id = models.IntegerField()

    class Meta:
        db_table = 'TBHAIRSHOP_PRG'

class Clinic(models.Model):
    TYPE = (
        ('1', 'Man'),
        ('2', 'Woman'),
        ('3', 'MHead'),
        ('4', 'TopHead'),
    )

    clinic_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=1, choices=TYPE)
    clinic_nm = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    like_cnt = models.IntegerField()
    phone_num = models.CharField(max_length=11)
    mobile_num = models.CharField(max_length=11)
    kakao_id = models.CharField(max_length=20)
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'TBCLINIC'

class ClinicPrg(models.Model):
    prg_id = models.AutoField(primary_key=True)
    prg_nm = models.CharField(max_length=200)
    # prgset = models.ForeignKey(HairPrgSet, related_name='prg_prgset', on_delete=models.CASCADE)
    clinic_id = models.IntegerField()

class Review(models.Model):
    CATEGORY = (
        ('1', 'HairPrd'),
        # ('2', 'NormMed'),
        # ('3', 'EtcMed'),
        # ('4', 'SpecMed'),
        ('2', 'HairShop'),
        ('3', 'Clinic'),
        ('4', 'Medicine'),
    )

    review_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=1, choices=CATEGORY)
    contents = models.CharField(max_length=4000)
    score = models.IntegerField()
    like_cnt = models.IntegerField()
    reg_date = models.DateTimeField(auto_now_add=True, blank=True)
    mod_date = models.DateTimeField(auto_now_add=True, blank=True)
    #owner = models.ForeignKey(User, related_name='hairprdrv_owner', on_delete=models.CASCADE)
    owner_id = models.IntegerField()
    #hairprd = models.ForeignKey(HairPrd, related_name='hairprdrv_hairprd', on_delete=models.CASCADE)
    hairprd_id = models.IntegerField(null=True, blank=True)
    # normmed_id = models.IntegerField(null=True, blank=True)
    # etcmed_id = models.IntegerField(null=True, blank=True)
    # specmed_id = models.IntegerField(null=True, blank=True)
    med_id = models.IntegerField(null=True, blank=True)
    hairshop_id = models.IntegerField(null=True, blank=True)
    clinic_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'TBREVIEW'

class Like(models.Model):
    CATEGORY = (
        ('1', 'HairPrd'),
        # ('2', 'NormMed'),
        # ('3', 'EtcMed'),
        # ('4', 'SpecMed'),
        ('2', 'HairShop'),
        ('3', 'Clinic'),
        ('4', 'Magazine'),
        ('5', 'Brand'),
        ('6', 'Medicine'),
    )
    like_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=1, choices=CATEGORY)
    #owner = models.ForeignKey(User, related_name='hairprdrv_owner', on_delete=models.CASCADE)
    owner = models.IntegerField()
    magazine_id = models.IntegerField()
    #hairprd = models.ForeignKey(HairPrd, related_name='hairprdrv_hairprd', on_delete=models.CASCADE)
    hairprd_id = models.IntegerField(null=True, blank=True)
    # normmed_id = models.IntegerField(null=True, blank=True)
    # etcmed_id = models.IntegerField(null=True, blank=True)
    # specmed_id = models.IntegerField(null=True, blank=True)
    med_id = models.IntegerField(null=True, blank=True)
    hairshop_id = models.IntegerField(null=True, blank=True)
    clinic_id = models.IntegerField(null=True, blank=True)


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Images/', default='Images/None/No-img.jpg')
    owner = models.ForeignKey(User, related_name='image_owner', on_delete=models.CASCADE)

    class Meta:
        db_table = 'TBIMAGE'