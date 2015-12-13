from django.db import models

# Create your models here.

class users(models.Model):
	pid = models.AutoField(primary_key=True)

class factories(models.Model):
	fid = models.AutoField(primary_key=True)
	fcode = models.CharField(max_length=100)

class retailers(models.Model):
	rid = models.AutoField(primary_key=True)
	rcode = models.CharField(max_length=100)

class factory_order(models.Model):
	ord_id = models.AutoField(primary_key = True)
	fid = models.ForeignKey(factories)
	turn = models.IntegerField()
	quantity = models.IntegerField()

class factory_retailer(models.Model):
	frid = models.AutoField(primary_key = True)
	fid = models.ForeignKey(factories)
	rid = models.ForeignKey(retailers)

class fac_ret_demand(models.Model):
	did = models.AutoField(primary_key=True)
	frid = models.ForeignKey(factory_retailer)
	turn = models.IntegerField()
	quantity = models.IntegerField()

class fac_ret_supply(models.Model):
	sid = models.AutoField(primary_key=True)
	frid = models.ForeignKey(factory_retailer)
	turn = models.IntegerField()
	quantity = models.IntegerField()

class factory_factory(models.Model):
	mid = models.AutoField(primary_key=True)
	fac1 = models.ForeignKey(factories, related_name="his_factory")
	fac2 = models.ForeignKey(factories, related_name="opponent")

