from django.db import models
#from django.db import xml_models

#targetXML=open("http://www.cha.go.kr/cha/SearchKindOpenapiList.do?pageUnit=10&pageIndex=1",'r')
# Create your models here.
class ByTime(models.Model):
    period =models.IntegerField(default=0)
    year =models.IntegerField(default=0)
    name =models.CharField(max_length=20)
    code =models.IntegerField(default=0)
    clickable =models.BooleanField( null=True)


class Datas(models.Model):
    ccbaKdcd =models.IntegerField(default=0)  #int,지정종목(종목코드)
    ccbaAsno =models.CharField(max_length=20,null=True,blank=True)  #int,지정번호
    ccbaCtcd =models.IntegerField(default=0)  #int,시도코드
    ccbaPcd1 =models.CharField(max_length=3,default=0)  #int,시대
    ccbaMnm1 =models.CharField(max_length=20,null=True,blank=True)     #String,문화재명
    ccbaMnm2 =models.CharField(max_length=20,null=True,blank=True)     #string,문화재명2 
    ccmaName =models.CharField(max_length=20,null=True,blank=True)     #string,문화재유형
    ccbaCtcdNm =models.CharField(max_length=20,null=True,blank=True)   #string,시도명
    ccsiName =models.CharField(max_length=20,null=True,blank=True)     #string,시군구명
    longitude =models.CharField(max_length=30,null=True,blank=True)    #위도
    latitude =models.CharField(max_length=30,null=True,blank=True)     #경도
    ccbaLcad =models.TextField(null=False,default='-')     #string,주소 상세
    content =models.TextField(null=False,default='-')      #string,내용

