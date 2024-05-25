from rest_framework import serializers
from app1.models import User,JobPost,JobApplication,SavedJobs

class RecruiterSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=['id','first_name','last_name','username','password','email','phone','city','state','pincode','image','user_file']

    def create(self,validated_data):
        return User.objects.create_user(**validated_data,is_staff=True)

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=['id','first_name','last_name','username','password','email','phone','city','state','pincode','image','user_file']
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
        
class JobPostSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    likes=serializers.CharField(read_only=True)
    class Meta:
        model = JobPost
        fields = ['id','user','job_title','job_location','job_package','job_logo','qualification',
                  'experience','job_description','is_active']
        
    def create(self, validated_data):
        user=self.context.get("user")
        return JobPost.objects.create(user=user,**validated_data)

class JobApplicationSerializer(serializers.ModelSerializer):
     id=serializers.CharField(read_only=True)
     job_title=serializers.CharField(read_only=True)
     user=serializers.CharField(read_only=True)
     class Meta:
        model = JobApplication
        fields=['id','job_title','user','full_name','phone','cv','experince','email']
     def create(self, validated_data):
        user=self.context.get("user")
        job=self.context.get("job")
        return JobApplication.objects.create(user=user,job_title=job,**validated_data)
    
class SavedJobsSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    job_title=serializers.CharField(read_only=True)

    class Meta:
        model=SavedJobs
        fields="__all__"

    def create(self, validated_data):
        user=self.context.get('user')
        job=self.context.get('job')
        return SavedJobs.objects.create(user=user,job_title=job,**validated_data)
