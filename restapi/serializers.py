from rest_framework import serializers
from restapi.models import Lead
from .custom_serializers import DynamicFieldsModelSerializer


class LeadSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(allow_blank=True, max_length=100, required=True)
    last_name = serializers.CharField(allow_blank=True, max_length=100, required=True)
    mobile = serializers.CharField(max_length=10, required=True)
    email = serializers.CharField(max_length=100, required=True)
    location_type = serializers.CharField(allow_blank=True, max_length=100, required=True)
    location_string = serializers.CharField(allow_blank=True, max_length=200, required=True)
    status = serializers.CharField(allow_blank=True, max_length=50, required=False)
    communication = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Lead
        fields = ['id', 'first_name', 'last_name', 'mobile', 'email', 'location_type', 'location_string', 'status',
                  'communication']

    def create(self, validated_data):
        """
        Create and return a new `Lead` instance, given the validated data.
        """
        return Lead.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Lead` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.email = validated_data.get('email', instance.email)
        instance.location_type = validated_data.get('location_type', instance.location_type)
        instance.location_string = validated_data.get('location_string', instance.location_string)
        instance.status = validated_data.get('status', instance.status)
        instance.communication = validated_data.get('communication', instance.communication)
        instance.save()
        return instance
