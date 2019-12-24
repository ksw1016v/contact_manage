from django.db import models
import datetime


# Create your models here.

class Depts(models.Model):
    dept= model.CharField('부서')
    

class Teams(models.Model):
    team = models.CharField('팀')

class Ranks(models.Model):
    rank = models.CharField('직급')

class Positions(models.Model):
    position = models.CharField('직책')



class Users(models.Model):
    id = models.AutoField()
    time_stamp = models.DateTimeField('등록일', default=datetime.datetime.now(), editable=False)
    user_join_date = models.DateField('입사일')
    user_id = models.CharField('회원아이디')
    user_password = models.CharField('비밀번호')
    user_name = models.CharField('회원이름')
    user_reg_number = models.CharField('주민번호')
    phone_number = models.CharField('전화번호')
    e_mail = models.EmailField('이메일', max_length=254)
    dept = models.ForeignKey(Depts, on_delete=models.SET_NULL, related_name='users')
    team = models.ForeignKey(Teams, on_delete=models.SET_NULL, related_name='users')
    rank = models.ForeignKey(Ranks, on_delete=models.SET_NULL, related_name='users')
    position = models.Foreignkey(Positions, on_delete=models.SET_NULL, related_name='user')
    authent = models.CharField('사용자등급')
    used = models.BooleanField('사용여부')

class Customers(models.Model):
    id = models.AutoField()
    time_stamp = models.DateTimeField('등록일',default=datetime.datetime.now(), editable=False)
    customer_join_date = models.DateField('계약일')
    customer_end_date = models.DateField('해임일')
    customer_ing = models.CharField('계약상태')
    join_category = models.CharField('계약구분')
    customer_category = models.CharField('회원구분')
    company_ing = models.CharField('회원상태')
    company_name = models.CharField('거래처명')
    bizcode = models.CharField('사업자등록번호')
    bizsub1 = models.CharField('업종')
    bizsub2 = models.CharField('종목')
    biz_start_date = models.DateField('개업일')
    biz_end_date = models.DateField('폐업일')
    biz_stop_date = models.DateField('휴업일')
    customer_name = models.CharField('대표자')
    customer_reg_number = models.CharField('주민번호')
    customer_phone = models.CharField('전화번호')    
    company_address = models.CharField('주소')
    company_co_owner = models.CharField('공동대표여부')
    relation_company = models.ManyToManyField(self)
    sales1 = models.CharField('영업자(주)')
    sales2 = models.CharField('영업자(부)')
    sales2_code = models.CharField('영업자(부)구분')
    pay_start_date = models.DateField('결제시작일')
    pay_category = models.CharField('결제방법')
    pay_name = models.CharField('예금주')
    pay_bank_card = models.CharField('결제사')
    pay_number = models.CharField('통장/카드번호')
    card_day = models.CharField('유효기간일')
    card_year = models.CharField('유효기간월')
    year_pay = models.CharField('조정수수료')
    add_document = models.CharField('첨부파일')
    upload = models.FileField(upload_to = None)
    customer_memo = models.CharField('회원메모')
    company_memo = models.CharField('회사메모')
    pay_memo = models.CharField('결제메모')
    memo = models.CharField('비고')
    customer_used = models.BooleanField('사용여부')
    updated = models.DateTimeField('수정일',auto_now = True)




