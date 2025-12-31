from rest_framework import serializers
from a_accounts.models import *

class AcademicQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicQualification
        fields = "__all__"
        
class RegistersListSerializer(serializers.ModelSerializer):
    qualifications = AcademicQualificationSerializer(many=True, read_only=True)
    class Meta:
        model = Register
        fields = "__all__"
        
