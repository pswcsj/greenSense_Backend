from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# 채팅, 질문 대답

USER_TYPE = ['Under', 'Master', 'Doctor']


class User(AbstractBaseUser):
    name = models.CharField()
    nickname = models.CharField()
    # school = models.CharField(choices=)
    school = models.CharField()
    major = models.CharField()
    # major = models.CharField(choices=)
    grade = models.IntegerChoices()
    type = models.CharField(choices=USER_TYPE)
    point = models.IntegerField()
    answers_count = models.IntegerField()


class Chat(models.Model):
    lastMessage = models.TextField()
    createdAt = models.DateTimeField()


ATTACHMENT_TYPE = ['Image', 'Video', 'None']


class Message(models.Model):
    chat = models.ForeignKey(Chat)
    from_user = models.ForeignKey(User)
    to_user = models.ForeignKey(User)
    text = models.TextField()
    attachment = models.FileField(upload_to='message')
    attachment_type = models.CharField(choices=ATTACHMENT_TYPE, default='None')
    created_at = models.DateTimeField()
    is_read = models.BooleanField(default=False)


class Question(models.Model):
    questioner = models.ForeignKey(User)
    teacher = models.ForeignKey(User)
    # subject = models.CharField(choices=)
    subject = models.CharField()
    # theme = models.CharField(choices=)
    theme = models.CharField()
    book = models.CharField()
    # book = models.CharField(choices=)

    # tags
    # review
    # star
    point = models.IntegerField()
    attachment = models.FileField(upload_to='question')
    text = models.TextField()
    chat = models.ForeignKey(Chat)
    is_end = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    end_at = models.DateTimeField()
