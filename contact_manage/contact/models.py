from django.db import models
import datetime

class Depts(models.Model):
    dept = models.CharField('부서', max_length=50)
    
class Teams(models.Model):
    team = models.CharField('팀', max_length=50)

class Ranks(models.Model):
    rank = models.CharField('직급', max_length=50)

class Positions(models.Model):
    position = models.CharField('직책', max_length=50)

class Users(models.Model):

    time_stamp = models.DateTimeField('등록일', default=datetime.datetime.now(), editable=False)
    user_join_date = models.DateField('입사일')
    user_id = models.CharField('회원아이디', max_length=50)
    user_password = models.CharField('비밀번호', max_length=50)
    user_name = models.CharField('회원이름', max_length=50)
    user_reg_number = models.CharField('주민번호', max_length=50)
    phone_number = models.CharField('전화번호', max_length=50)
    e_mail = models.EmailField('이메일', max_length=254)
    dept = models.ForeignKey(Depts, on_delete=models.SET_NULL, related_name='users',null=True)
    team = models.ForeignKey(Teams, on_delete=models.SET_NULL, related_name='users',null=True)
    rank = models.ForeignKey(Ranks, on_delete=models.SET_NULL, related_name='users',null=True)
    position = models.ForeignKey(Positions, on_delete=models.SET_NULL, related_name='user',null=True)
    authent = models.CharField('사용자등급', max_length=50)
    used = models.BooleanField('사용여부', max_length=50)

class Customers(models.Model):

    time_stamp = models.DateTimeField('등록일',default=datetime.datetime.now(), editable=False)
    customer_join_date = models.DateField('계약일')
    customer_end_date = models.DateField('해임일')
    customer_ing = models.CharField('계약상태', max_length=50)
    join_category = models.CharField('계약구분', max_length=50)
    customer_category = models.CharField('회원구분', max_length=50)
    company_ing = models.CharField('회원상태', max_length=50)
    company_name = models.CharField('거래처명', max_length=50)
    bizcode = models.CharField('사업자등록번호', max_length=50)
    bizsub1 = models.CharField('업종', max_length=50)
    bizsub2 = models.CharField('종목', max_length=50)
    biz_start_date = models.DateField('개업일')
    biz_end_date = models.DateField('폐업일')
    biz_stop_date = models.DateField('휴업일')
    customer_name = models.CharField('대표자', max_length=50)
    customer_reg_number = models.CharField('주민번호', max_length=50)
    customer_phone = models.CharField('전화번호', max_length=50)
    company_address = models.CharField('주소', max_length=50)
    company_co_owner = models.BooleanField('공동대표여부')
    relation_company = models.ManyToManyField('self')
    sales1 = models.CharField('영업자(주)', max_length=50)
    sales2 = models.CharField('영업자(부)', max_length=50)
    sales2_code = models.CharField('영업자(부)구분', max_length=50)
    pay_start_date = models.DateField('결제시작일')
    pay_category = models.CharField('결제방법', max_length=50)
    pay_name = models.CharField('예금주', max_length=50)
    pay_bank_card = models.CharField('결제사', max_length=50)
    pay_number = models.CharField('통장/카드번호', max_length=50)
    card_day = models.CharField('유효기간일', max_length=50)
    card_year = models.CharField('유효기간월', max_length=50)
    month_pay = models.IntegerField('월수수료')
    year_pay = models.CharField('조정수수료', max_length=50)
    add_document = models.CharField('첨부파일', max_length=50)
    upload = models.FileField(upload_to = None)
    customer_memo = models.CharField('회원메모', max_length=50)
    company_memo = models.CharField('회사메모', max_length=50)
    pay_memo = models.CharField('결제메모', max_length=50)
    memo = models.TextField('비고', max_length=50)
    upload_paysite = models.BooleanField('결제등록여부')
    customer_used = models.BooleanField('사용여부')
    updated = models.DateTimeField('수정일',auto_now = True)

class Co_owners(models.Model):

    time_stamp = models.DateTimeField('등록일',default=datetime.datetime.now(), editable=False)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='co_owners')
    co_owner_name = models.CharField('이름', max_length=50)
    co_owner_reg_number = models.CharField('주민번호', max_length=50)
    co_owner_phone = models.CharField('전화번호', max_length=50)
    share_per = models.DecimalField('지분율', decimal_places=2,max_digits=50)
    co_owner_rank = models.CharField('순위', max_length=50)
    co_owner_memo = models.TextField('공동사업자메모', max_length=50)
    updated = models.DateTimeField('수정일', auto_now = True)

class Payinformations(models.Model):

    time_stamp = models.DateTimeField('등록일',default=datetime.datetime.now(), editable=False)
    member_num = models.CharField('회원번호', max_length=50)
    pay_start_date = models.DateField('결제시작일')
    pay_end_date = models.DateField('결제종료일')
    join_date = models.DateField('가입일')
    payinfo_used = models.BooleanField('사용여부')
    pay_day = models.CharField('결제일', max_length=50)
    pay_category = models.CharField('결제방법', max_length=50)
    pay_account_holder = models.CharField('예금주', max_length=50)
    pay_company = models.CharField('결제사', max_length=50)
    pay_number = models.CharField('결제번호', max_length=50)
    card_limited_day = models.CharField('카드유효기간', max_length=50)
    payment_month = models.IntegerField('월수수료')
    pay_memo = models.TextField('결제메모', max_length=50)
    updated = models.DateTimeField('수정일',auto_now = True)
    customer = models.ForeignKey(Customers, on_delete=models.SET_NULL, related_name='payinformations',null=True)

class pay_results(models.Model):

    time_stamp = models.DateTimeField('등록일', default=datetime.datetime.now(), editable =False)
    pay_date = models.DateField('결제일')
    payment = models.IntegerField('결제수수료')
    pay_memo = models.CharField('결제메모', max_length=50)
    pay_category = models.CharField('결제구분', max_length=50)
    payinformation = models.ForeignKey(Payinformations, on_delete=models.SET_NULL, related_name='pay_results',null=True)

