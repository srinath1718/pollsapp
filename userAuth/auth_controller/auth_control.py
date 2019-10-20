from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from userAuth.models import UserProfile
from rest_framework.parsers import MultiPartParser
from django.conf import os
from django.conf import settings


class UserSignUp(APIView):

    def post(self,request):
        user = User()
        user.username = request.data['username']
        user.set_password(request.data['password1'])
        user.save()
        return Response({"Message":True},status.HTTP_201_CREATED)
    # return Response(status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    def post(self,request):
        user = authenticate(
            username = request.data['username'],
            password = request.data['password']
        )
        if user is None:
            return Response({"Message": "Invalid User"},status.HTTP_404_NOT_FOUND)
        else:

            try:
                resultSet = Token.objects.get(user_id=user.id)
                # print(resultSet)
                # resultSet = Token.objects.get_or_create(user_id=user.id)
                resultSet.delete()
            except:
                pass

            token = Token.objects.create(user=user)
            return Response({
                "token": token.key,
                "userId": user.id,
                "success": True
            }, status.HTTP_200_OK)

        # return Response(generateTokenSeri.errors, status.HTTP_400_BAD_REQUEST)

class TokenInfo(APIView):

    # permission_classes = IsAuthenticated

    def get(self,request):

        return Response("success", status.HTTP_200_OK)

class ProfileCreation(APIView):

    def post(self,request,id):

        try:
            user = UserProfile.objects.get(user_id=id)
            user.mobile = request.data['mobile']
            user.city = request.data['city']
            user.save()
            #updated = UserProfile.objects.filter(user_id=id).values()
            #result = list(updated)
            return Response({'Message': True}, status.HTTP_200_OK)

        except UserProfile.DoesNotExist:

            user = UserProfile()
            user.user_id = id
            user.mobile = request.data['mobile']
            user.city = request.data['city']
            user.save()
            return Response({"Message": "Profile Created Successfully"}, status.HTTP_200_OK)

        # result = UserProfile.objects.filter(user_id=id).values()
        # temp = list(result)
        # if len(temp)>0:
        #     user = UserProfile.objects.get(user_id=id)
        #     user.mobile=request.data['mobile']
        #     user.city=request.data['city']
        #     user.save()
        #     updated = UserProfile.objects.filter(user_id=id).values()
        #     result=list(updated)
        #     return Response({'Message': True,"data":result},status.HTTP_200_OK)
        # else:
        #     user=UserProfile()
        #     user.user_id = id
        #     user.mobile = request.data['mobile']
        #     user.city = request.data['city']
        #     user.save()
        #     return Response({"Message":"Profile Created Successfully"}, status.HTTP_200_OK)

    def get(self,request,id):
        result = UserProfile.objects.filter(user_id=id).values()
        data = list(result)
        return Response({'data':data},status.HTTP_200_OK)

class UploadProfilePhoto(APIView):

    parser_class=(MultiPartParser, )

    def put (self,request,id):
        response={}
        try:
            up_file = request.FILES['file']
            relativePath='/media/users/'+str(id)+'/'
            fileSaveDir = settings.BASE_DIR+relativePath
            if not os.path.exists(fileSaveDir):
                os.makedirs(fileSaveDir)
                # removeFile(fileSaveDir)
            imagePath=fileSaveDir+up_file.name
            with open(imagePath,'wb+') as destination:
                for chunk in up_file.chunks():
                        destination.write(chunk)
            imgpath=UserProfile.objects.get(user_id=id)
            imgpath.photo=relativePath + up_file.name
            imgpath.save()
            return Response({'Message':'Image uploaded successfully'})
        except:
            return Response('file upload failed')
# class ProfileDelete(APIView):
#
#     def delete(self,request,id):
#         result = UserProfile.objects.filter(id=id).values()
#         result.delete()
#         return Response({"Profile Deleted Successfully"})


