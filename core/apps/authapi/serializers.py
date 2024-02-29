from enum import unique
from rest_framework import serializers
from apps.users.models import Users
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from apps.histori.users_his_password.models import USER_HIS_PASSWORD
from django.contrib.auth.hashers import check_password,make_password
from rest_framework.response import Response
from rest_framework import status

from apps.users import serializers as user_serializers
User = get_user_model()

class AuthDetailSerializer(serializers.ModelSerializer):
    departemen = user_serializers.GetDepartemen(read_only=True, source='id_departemen')
    jabatan = user_serializers.GetJabatan(read_only=True, source='id_jabatan')
    perusahaan = user_serializers.GetPerusahaan(read_only=True, source='id_perusahaan')
    role = user_serializers.GetRole(read_only=True, source='roleId')
    class Meta:
        model = Users
        fields = '__all__'


class AuthSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True, validators=[
        UniqueValidator(
            queryset=Users.objects.all(),
            message="Email Already Taken",
        )])
    username = serializers.CharField(required=True, min_length=8,validators=[
        UniqueValidator(
            queryset=Users.objects.all(),
            message="Username Already Taken",
        )])
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Users
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('old_password', 'password', 'password_confirmation')

    # password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    # new_password = serializers.CharField(write_only=True, required=True)
    # old_password = serializers.CharField(write_only=True, required=True)

    old_password = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({"password": "Password Tidak Sama."})
        return attrs

    def validate_old_password(self, value):
        user_id = self.context['request'].user.user_id
        user = get_object_or_404(Users, pk=user_id)  
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Password Lama salah."}) 
        return value
    def validate_password(self, value):
        password = value 
        user_id = self.context['request'].user.user_id 
        last_15pass = USER_HIS_PASSWORD.objects.filter(id_user=user_id).order_by('-date_created')[:15].values('password') 
        if last_15pass:
            for l15p in last_15pass: 
                # print(l15p.get('password'))
                if check_password(password, l15p.get('password')):
                    raise serializers.ValidationError({"password": "Password Sudah Pernah Digunakan Sebelumnya!"}) 
        return value

    # def update(self, instance, validated_data): 
    #     user_id = self.context['request'].user.user_id 
    #     # print('tes', password)
    #     if user_id != instance.id_user:
    #         raise serializers.ValidationError({"authorize": "You dont have permission for this user."}) 
    #     password = validated_data['password'] 
    #     last_15pass = USER_HIS_PASSWORD.objects.filter(id_user=instance.id_user).order_by('-date_created')[:15].values('password') 
    #     if last_15pass:
    #         for l15p in last_15pass: 
    #             # print(l15p.get('password'))
    #             if check_password(password, l15p.get('password')):
    #                 raise serializers.ValidationError({"password": "Password Sudah Pernah Digunakan Sebelumnya!"}) 
        
        
    #     instance.set_password(password)
    #     instance.save()
    #     if instance :
    #         user = get_object_or_404(Users, pk=user_id)   
    #         his = USER_HIS_PASSWORD(id_user=user,password=make_password(password))
    #         his.save()  
    #     return instance
