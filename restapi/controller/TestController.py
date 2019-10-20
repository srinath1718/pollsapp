from rest_framework.views import  APIView
from rest_framework.response import  Response
from rest_framework import status
from restapi.serializer.TestSerializer import TestSerializer


class TestAPI(APIView):

    def get(self,request):

        return Response({"message":"success"},status.HTTP_200_OK)


    def post(self,request):

        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"success":True,"message":serializer.data},status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)