from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Vedio,Rating
from django.contrib.auth.models import User

class VedioSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Vedio
		fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']		

    def  save(self):
    	user = User(
    				email = self.validated_data['email'],
    				username = self.validated_data['username'],
    		) 
    	password = self.validated_data['password']

    	user.set_password(password)	
    	user.save()
    	return user
 
# class RatingSerializer(serializer.ModelsSerializer):
# 	class Meta:
# 		model = Rating
# 		fields = ('id','stars','user','video','comment')
		
# class UserSerializer(serializer.ModelsSerializer):		
# 	class Meta:
# 		model = User
# 		fields = ('id','username','password')
# 		extra_kwargs = {'password':{'password':True,'write_only':True }}

# 		def create(self,validated_data):
# 			user = User.objects.creater_user(**validated_data)
# 			Token.objects.create(user = user)
# 			return user