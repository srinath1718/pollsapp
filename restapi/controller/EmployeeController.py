from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from utils.EmployeeUtil import Employee

from restapi.serializer.Employee import EmployeeSerializer


class EmployeeDetails(APIView):

    def post(self,request):

        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():

            empUtil = Employee()
            empModel = empUtil.setEmployeeModelObject(serializer.data)
            empModel.save()

            return Response({'Success':True,'message':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):

        empUtil = Employee()

        result = empUtil.findAll()
        result = list(result)

        # result = EmployeeModel.objects.values()
        # result = list(result)
        return Response ({"success":True, "data":result},status=status.HTTP_200_OK)

class EmployeeSearch(APIView):

    def get(self,request, id):

        empUtil = Employee()
        result = empUtil.findEmployeeById(id).values()
        result = list(result)

        # result = EmployeeModel.objects.filter(id=id).values()
        # result = list(result)
        return  Response({"Success":True,"data":result},status.HTTP_200_OK)


    # def get(self,request,emp_email):
    #
    #     empUtil = Employee()
    #     result = empUtil.findEmployeeByEmail(emp_email)
    #     result = list (result)
    #
    #     return ({'Message':True,"data":result},status.HTTP_200_OK)

    def delete(self,request,id):

        empUtil = Employee()
        result = empUtil.findEmployeeById(id)
        result.delete()

        # result = EmployeeModel.objects.get(id=id)
        # result.delete()
        return Response({"Success":True},status.HTTP_200_OK)

    def put(self,request,id):

        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():

            # empModel = EmployeeModel.objects.get(id=id)
            # empModel.emp_name = serializer.data['emp_name']
            # empModel.emp_email = serializer.data['emp_email']
            # empModel.emp_address = serializer.data['emp_address']
            # empModel.emp_city = serializer.data['emp_city']
            # empModel.save()

            empUtil = Employee()
            empObject = empUtil.getEmployeById(id)
            empModel = empUtil.setEmployeeModelObject(serializer.data,empObject)
            empModel.save()

            return Response({'Success': True, 'message': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


