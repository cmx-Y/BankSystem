from rest_framework import serializers

from testapp.models import Subbank


class SubbankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subbank
        fields = '__all__'