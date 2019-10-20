from rest_framework import  serializers


class EmployeeSerializer(serializers.Serializer):

    emp_name = serializers.CharField(
        min_length=8,
        max_length=50
    )
    emp_email = serializers.CharField()
    emp_address = serializers.CharField()
    emp_city = serializers.CharField()
