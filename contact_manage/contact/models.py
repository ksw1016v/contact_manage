from django.db import models
import datetime


# Create your models here.

class users(models.Model):
    time_stamp = models.DateTimeField('등록일', default=datetime.datetime.now(), editable=False)
    join_date = models.DateField('입사일')
    user_id = models.CharField('회원아이디')
    user_password = models.CharField('비밀번호')
    user_name = models.CharField('회원이름')
    user_reg_number = models.CharField('주민번호')
    phone_number = models.CharField('전화번호')
    e_mail = models.CharField('이메일')
    dept = models.ForeignKey(dept, on_delete=models.SET_NULL, related_name='users')
    team = models.ForeignKey(team, on_delete=models.SET_NULL, related_name='users')
    rank = models.ForeignKey(rank, on_delete=models.SET_NULL, related_name='users')
    position = models.Foreignkey(position, on_delete=models.SET_NULL, related_name='user')
    used = models.BooleanField('사용여부')


class dept(models.Moels):
    dept = models.CharField('부서')

class team(models.Model):
    team = models.CharField('팀')


class rank(models.Model):
    rank = models.CharField('직급')


class position(models.Model):
    position = models.CharField('직책')

    
