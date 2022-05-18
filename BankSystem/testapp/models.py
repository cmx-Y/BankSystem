# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Subbank(models.Model):
    bankname = models.CharField(db_column='BankName', primary_key=True, max_length=20)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    asset = models.DecimalField(db_column='Asset', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubBank'
