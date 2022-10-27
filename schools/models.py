# schools/model
from django.conf import settings
from django.db import models


class Country(models.Model):
    country = models.CharField(max_length=100, blank=True, null=False)
    capital = models.CharField(max_length=100, blank=True, null=True)
    area_sqkm = models.IntegerField(blank=True, null=True)
    num_provinces = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Country'

    def __str__(self):
        return self.country


class Province(models.Model):
    province = models.CharField(max_length=100, blank=True, null=True)
    capital = models.CharField(max_length=100, blank=True, null=True)
    num_districts = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey(
        Country, models.DO_NOTHING, blank=True, null=False)

    # class Meta:
    #     managed = False
    #     db_table = 'Province'

    def __str__(self):
        return self.province


class District(models.Model):
    district = models.CharField(max_length=100, blank=True, null=True)
    province = models.ForeignKey(
        Province, models.DO_NOTHING, blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'District'

    def __str__(self):
        return self.district


class SchoolLevel(models.Model):
    school_level = models.CharField(max_length=100, blank=True, null=False)

    # class Meta:
    #     managed = False
    #     db_table = 'SchoolLevel'

    def __str__(self):
        return self.school_level


class SchoolType(models.Model):
    school_type = models.CharField(max_length=100, blank=True, null=False)

    # class Meta:
    #     managed = False
    #     db_table = 'SchoolType'

    def __str__(self):
        return self.school_type


class School(models.Model):
    name = models.CharField(max_length=255, blank=True, null=False)
    preferred_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    school_level = models.ForeignKey(
        SchoolLevel, models.DO_NOTHING, blank=True, null=False)
    school_type = models.ForeignKey(
        SchoolType, models.DO_NOTHING, blank=True, null=False)
    district = models.ForeignKey(
        District, models.DO_NOTHING, blank=True, null=True)
    province = models.ForeignKey(
        Province, models.DO_NOTHING, blank=True, null=False)
    country = models.ForeignKey(
        Country, models.DO_NOTHING, blank=True, null=False)
    founded = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     managed = False
    #     db_table = 'Schools'

    def __str__(self):
        return self.name
