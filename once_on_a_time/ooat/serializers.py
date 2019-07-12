from rest_framework import serializers

from .models import Datas

class DatasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Datas
        fields = ('ccbaKdcd','ccbaAsno','ccbaCtcd','ccbaPcd1','ccbaMnm1','ccbaMnm2','ccmaName','ccbaCtcdNm','ccsiName','longitude','latitude','content')