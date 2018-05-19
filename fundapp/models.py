from django.db import models

# Create your models here.
from django.db import models
import datetime
import uuid
from django.urls import reverse

class FundInfo(models.Model):
    def __str__(self):
        return self.fund_name
    fund_code = models.CharField(max_length=20)
    fund_name = models.CharField(max_length=40)
    fund_type = models.CharField(max_length=2)
    fund_status = models.CharField(max_length=1, default='1')
    fund_total = models.FloatField(default=0)

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('order-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.fund_name

class Trader(models.Model):
    def __str__(self):
        return self.trader_name
    login_account = models.CharField(max_length=20)
    trader_name = models.CharField(max_length=10)
    balance = models.FloatField(default=0)


class Order(models.Model):
    DIRECTIONS = (
        ('1', '买'),
        ('2', '卖'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this Order")
    fund = models.ForeignKey('FundInfo', on_delete=models.CASCADE, null=True)
    trade_ts = models.DateTimeField()
    trade_direction = models.CharField(max_length=1, choices=DIRECTIONS, default='1')
    trader = models.ForeignKey('Trader', null=False, on_delete=models.CASCADE)
    trading_fee = models.FloatField(default=0)
    trading_share = models.IntegerField(default=0)

    def __str__(self):
        return '{0} ({1})'.format(self.id, self.fund.fund_name)




class FundPara(models.Model):
    def __str__(self):
        return self.fund_type
    fund_type = models.CharField(max_length=2)
    redeem_per = models.FloatField(default=0)
    redeem_days = models.IntegerField(default=0)


class FundTrade(models.Model):
    def __str__(self):
        return self.fund_code
    fund_code = models.CharField(max_length=20)
    trade_ts = models.DateTimeField()
    fund_nav = models.DecimalField(max_digits=10, decimal_places=4)


