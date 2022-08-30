from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# 채팅, 질문 대답

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
    # school = models.CharField(choices=)
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    # major = models.CharField(choices=)
    grade = models.IntegerField()
    type = models.CharField(choices=USER_TYPE, max_length=10)
    point = models.IntegerField(default=100)
    answers_count = models.IntegerField(default=0)

    USERNAME_FIELD = 'username'


class Chat(models.Model):
    lastMessage = models.TextField()
    createdAt = models.DateTimeField(auto_now=True)


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
    end_at = models.DateTimeField()
