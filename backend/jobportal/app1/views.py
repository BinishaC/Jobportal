from django.shortcuts import render
from rest_framework.views import APIView
from app1.serializers import RecruiterSerializer,UserSerializer,JobPostSerializer,JobApplicationSerializer,SavedJobsSerializer
from app1.models import User,JobPost,JobApplication,SavedJobs
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication,permissions
from rest_framework.decorators import action
# from django.core.mail import send_mail,settings

# Create your views here.

class RecruiterRegisterView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RecruiterSerializer
    def get_queryset(self):
        return User.objects.filter(is_staff=True,is_superuser=False)

class UserRegisterView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def get_queryset(self):
        return User.objects.filter(is_staff=False,is_superuser=False)
    # return Response({'msg':'like added'})
    
class JobPostViewSet(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication] # code for token auth
    permission_classes=[permissions.IsAuthenticated]
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

    def create(self, request, *args, **kwargs):
        user=request.user
        print(user)
        if user.is_staff==1:
            serializer = self.get_serializer(data=request.data,context={"user":self.request.user})
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'msg':"cannot post"})
        
    @action(methods=['post'],detail=True)
    def add_likes(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        user_likes=JobPost.objects.get(id=id)
        user_likes.liked_by.add(request.user)
        return Response({'msg':'like added'})
    
    @action(methods=['post'],detail=True)
    def job_application(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        job_title=JobPost.objects.get(id=id)
        user=request.user
        application=JobApplication.objects.filter(user=user,job_title=job_title)
        print(application)
        if application:
            return Response({'msg':'Already applied'})
        else:
           serializer=JobApplicationSerializer(data=request.data,context={'user':user,'job':job_title})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

 
        #  a="Application submited"+str(application.job_title)+"-"+str(application.job_location)
        #     send_mail("confirmation",a,settings.EMAIL_HOST_USER,[email])


    @action(methods=['post'],detail=True)
    def add_to_saved_jobs(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        job_title=JobPost.objects.get(id=id)
        user=request.user
        saved=SavedJobs.objects.filter(user=user,job_title=job_title)
        print(saved)
        if saved:
            return Response({'msg':'Already added to saved list'})
        else:
            serializer=SavedJobsSerializer(data=request.data,context={'user':user,'job_title':job_title})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class SavedJobListView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication] # code for token auth
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=SavedJobsSerializer
    queryset=JobPost.objects.all()

    def get_queryset(self):
        return SavedJobs.objects.filter(user=self.request.user)

