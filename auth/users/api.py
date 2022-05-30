from django.views import View

from .models import Profile, Award, User
from staff.models import Language
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import AwardSerializer, LanguageSerializer, ProfileSerializer, UserSerializer
from .permissions import IsSuperUserOrReadOnly

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class AwardViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSuperUserOrReadOnly]
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.exclude(user_type='staff')
    serializer_class = UserSerializer

# class StaffViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.filter(user_type = 'staff')
#     serializer_class = 