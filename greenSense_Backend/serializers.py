from rest_framework import serializers
from greenSense_Backend.models import *
from dj_rest_auth.registration.serializers import RegisterSerializer


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'name', 'nickname', 'school', 'major', 'grade', 'edu_type']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self, request):
        user = User(
            email=self.validated_data['email'],
            name=self.validated_data['name'],
            nickname=self.validated_data['nickname'],
            school=self.validated_data['school'],
            major=self.validated_data['major'],
            grade=self.validated_data['grade'],
            edu_type=self.validated_data['edu_type'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


# class CustomRegisterSerializer(RegisterSerializer):
#     name = serializers.CharField(source="User.name")
#     nickname = serializers.CharField(source="User.nickname")
#     # school = models.CharField(choices=)
#     school = serializers.CharField(source="User.school")
#     major = serializers.CharField(source="User.major")
#     # major = models.CharField(choices=)
#     grade = serializers.IntegerField(source="User.grade")
#     edu_type = serializers.CharField(source="User.edu_type")
#     point = serializers.IntegerField(source="User.point")
#     answers_count = serializers.IntegerField(source="User.answers_count")
#
#     def get_cleaned_data(self):
#         super(CustomRegisterSerializer, self).get_cleaned_data()
#         return {
#             'password1': self.validated_data.get('password1', ''),
#             'password2': self.validated_data.get('password2', ''),
#             'email': self.validated_data.get('email', ''),
#             'name': self.validated_data.get('name', ''),
#             'nickname': self.validated_data.get('nickname', ''),
#             'school': self.validated_data.get('school', ''),
#             'major' : self.validated_data.get('major', ''),
#             'grade': self.validated_data.get('grade', ''),
#             'edu_type': self.validated_data.get('edu_type', ''),
#             'point': self.validated_data.get('point', ''),
#             'answers_count': self.validated_data.get('answers_count', ''),
#         }

# class CustomRegisterSerializer(RegisterSerializer):
#     # 기본 설정 필드: username, password, email
#     # 추가 설정 필드: profile_image
#
#     name = serializers.CharField(source="User.name")
#     nickname = serializers.CharField(source="User.nickname")
#     # school = models.CharField(choices=)
#     school = serializers.CharField(source="User.school")
#     major = serializers.CharField(source="User.major")
#     # major = models.CharField(choices=)
#     grade = serializers.IntegerField(source="User.grade")
#     edu_type = serializers.CharField(source="User.edu_type")
#     point = serializers.IntegerField(source="User.point")
#     answers_count = serializers.IntegerField(source="User.answers_count")
#
#     def get_cleaned_data(self):
#         data = super().get_cleaned_data()
#         data['name'] = self.validated_data.get('name', '')
#         data['nickname'] = self.validated_data.get('nickname', '')
#         data['school'] = self.validated_data.get('school', '')
#         data['major'] = self.validated_data.get('major', '')
#         data['grade'] = self.validated_data.get('grade', '')
#         data['edu_type'] = self.validated_data.get('edu_type', '')
#         data['point'] = self.validated_data.get('point', '')
#         data['answers_count'] = self.validated_data.get('answers_count', '')
#
#         return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
