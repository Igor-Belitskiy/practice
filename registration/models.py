from django.db import models


class Login(models.Model):
    log = models.ForeignKey(verbose_name='Логин', db_index=True, max_length=64)
    password = models.CharField(verbose_name='Пароль', db_index=True, max_length=64)


class Registration(models.Model):

    name = log = models.CharField(verbose_name='Имя', db_index=True,  max_length=64)
    surname = log = models.CharField(verbose_name='Фамилия', db_index=True, max_length=64)
    log = models.CharField(verbose_name='Логин', db_index=True, unique=True, max_length=64)
    password = models.CharField(verbose_name='Пароль', db_index=True, max_length=64)
    password_replay = models.CharField(verbose_name='Повторите пароль ', db_index=True, max_length=64)
