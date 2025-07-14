
from rest_framework import serializers
from .models import WheelForm, WheelField

class WheelFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelField
        exclude = ['id', 'form']

class WheelFormSerializer(serializers.ModelSerializer):
    fields = WheelFieldSerializer()

    class Meta:
        model = WheelForm
        fields = ['formNumber', 'submittedBy', 'submittedDate', 'fields']

    def create(self, validated_data):
        fields_data = validated_data.pop('fields')
        form = WheelForm.objects.create(**validated_data)
        WheelField.objects.create(form=form, **fields_data)
        return form
