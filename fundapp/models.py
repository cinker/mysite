from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils import timezone


class Instruction(models.Model):
    def __str__(self):
        return self.fund_code
    fund_code = models.CharField(max_length=20)
    trade_ts = models.DateTimeField()
    trade_direction = models.CharField(max_length=1)
    trader = models.CharField(max_length=20)


class FundInfo(models.Model):
    def __str__(self):
        return self.fund_name
    fund_code = models.CharField(max_length=20)
    fund_name = models.CharField(max_length=40)
    fund_type = models.CharField(max_length=2)


class FundPara(models.Model):
    def __str__(self):
        return self.fund_type
    fund_type = models.CharField(max_length=2)
    redeem_per = models.FloatField()
    redeem_days = models.IntegerField()


class FundTrade(models.Model):
    def __str__(self):
        return self.fund_code
    fund_code = models.CharField(max_length=20)
    trade_ts = models.DateTimeField()
    fund_nav = models.DecimalField(max_digits=10, decimal_places=4)


class Trader(models.Model):
    def __str__(self):
        return self.trader_name
    login_account = models.CharField(max_length=20)
    login_pass = models.CharField(max_length=40)
    trader_name = models.CharField(max_length=10)
    balance = models.FloatField()


class Question(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)