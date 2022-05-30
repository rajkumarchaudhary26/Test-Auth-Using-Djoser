from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Award, Profile, User
from staff.models import Language

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name',)

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('id', 'name', 'type', 'year',)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'user_type', 'is_active', 'is_staff', 'is_superuser', 'date_joined',)
        read_only_fields = ("email",)


class ProfileSerializer(WritableNestedModelSerializer):
    award = AwardSerializer(many = True)
    user = UserSerializer()
    language = LanguageSerializer(many = True)
    class Meta:
        model = Profile
        fields = ('id', 'user', 'family_name_in_kanji', 'family_name_in_hiragana', 'first_name_in_hiragana', 'family_name_in_english', 'first_name_in_english', 'date_of_birth', 'gender', 'profile_pic', 'birth_city', 'current_city', 'language', 'company', 'working_as', 'position', 'is_upgraded', 'full_address', 'manager_name', 'phone_number', 'employee', 'bio', 'description', 'award',)

# class StaffSearchSerializer(serializers.ModelSerializer):
#     # award_no = serializers.IntegerField(default=0)
#     # Video has related name "user" for User model
#     # videos = StaffSearchVideoThumbSerializer(many=True, source='user')
#     # videos = serializers.SerializerMethodField()  # Create method field to prefetch
#     # 
#     # def get_videos(self, obj):
#     #     videos = obj.user.all()
#     #     return StaffSearchVideoThumbSerializer(videos, many=True, context=self.context).data

#     class Meta:
#         model = Profile
#         exclude = ['award', 'language', 'user_permissions', 'groups', 'is_superuser', 'user_type', 'verified',
#                    'no_of_login', 'is_upgraded', 'password_changed_date', 'last_login', 'created_date', 'updated_date',
#                    'is_staff', 'is_active', 'date_joined', 'manager_name', 'dob', 'information_agree', 'gender']