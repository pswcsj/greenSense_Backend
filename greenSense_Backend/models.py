from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


# 채팅, 질문 대답


class UserManager(BaseUserManager):
    def create_user(self, username, name, nickname, email, school, major, grade, edu_type, password=None):
        if not email:
            raise ValueError("Users Must Have an email address")
        user = self.model(
            email=self.normalize_email(email),  # 이메일의 도메인 파트를 소문자로 바꿔줌
            username=username,
            name=name,
            nickname=nickname,
            school=school,
            major=major,
            grade=grade,
            edu_type=edu_type
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        if not email:
            raise ValueError("Users Must Have an email address")
        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(username, 'admin', 'admin', email, 'SNU', 'admin', 4, 'M', password)
        user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        user.save()

        return user


USER_TYPE = [('U', 'Under'), ('M', 'Master'), ('D', 'Doctor')]


class User(AbstractBaseUser):
    class Grade(models.IntegerChoices):
        FRESHMAN = 1
        SOPHOMORE = 2
        JUNIOR = 3
        SENIOR = 4

    username = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    # school = models.CharField(choices=)
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    # major = models.CharField(choices=)
    grade = models.IntegerField(choices=Grade.choices)
    edu_type = models.CharField(choices=USER_TYPE, max_length=10)
    point = models.IntegerField(default=100)
    answers_count = models.IntegerField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def has_perm(perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Chat(models.Model):
    lastMessage = models.TextField()
    createdAt = models.DateTimeField(auto_now=True)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='answer_chat')
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='question_chat')

    def __str__(self):
        return f'teacher: {self.teacher}, student: {self.student}'


ATTACHMENT_TYPE = [('IMG', 'Image'), ('VID', 'Video'), ('NONE', 'None')]


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='+')
    from_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='sent_message')
    to_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='received_message')
    text = models.TextField()
    attachment = models.FileField(upload_to='message')
    attachment_type = models.CharField(choices=ATTACHMENT_TYPE, default='None', max_length=5)
    created_at = models.DateTimeField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Question(models.Model):
    questioner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='question')
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_answered_question')
    # subject = models.CharField(choices=)
    subject = models.CharField(max_length=100)
    # theme = models.CharField(choices=)
    theme = models.CharField(max_length=100)
    book = models.CharField(max_length=150)
    # book = models.CharField(choices=)

    # tags
    # review
    # star
    point = models.IntegerField()
    attachment = models.FileField(upload_to='question')
    text = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='question')
    is_end = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    end_at = models.DateTimeField(null=True)
