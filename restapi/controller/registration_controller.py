from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from restapi.models import Registration

class RegistrationDetails(APIView):

    def post(self,request,regform=None):
            # print(request.data)
            if regform is None:
                    regform = Registration()
            regform.username = request.data['username']
            regform.email = request.data['email']
            regform.mobile_number= request.data['mobile']
            regform.country= request.data['country']
            regform.save()
            return Response({'Message':True,"data":request.data},status.HTTP_201_CREATED)
            return Response(status.HTTP_400_BAD_REQUEST)

    def get(self, request):
            result = Registration.objects.values()
            print(result)
            result = list(result)
            return Response({'Message':"Success","data":result})    



class RegisterList(APIView):

        def get(self, request, id):
                result = Registration.objects.filter(id=id).values()
                return Response(list(result))

        def put (self,request,id):

            regform = Registration.objects.get(id=id)
            regform.username = request.data['username']
            regform.email = request.data['email']
            regform.mobile_number = request.data['mobile']
            regform.country = request.data['country']
            regform.save()
            result = Registration.objects.filter(id=id).values()
            return Response({'Message':'success',"data":list(result)},status.HTTP_200_OK)

        def delete(self,request,id):

            result = Registration.objects.get(id=id)
            result.delete()
            return  Response({'Message:success'})

class ValidEmail(APIView):

        def get(self,request, email):

               # email = request.GET['email']
                result = Registration.objects.filter(email=email).values()
                temp = list(result)
                print(temp)
                if len(temp)>0:
                        return Response(True)
                return Response(False)











