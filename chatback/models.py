from django.db import models


class User(models.Model):
    screenName = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
            return self.screenName

class Room(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    users = models.ManyToManyField(User)
    def __unicode__(self):
            return self.title

class ChatLog(models.Model):
    dateStarted = models.DateTimeField(auto_now=True)
    room = models.ForeignKey(Room, related_name='chatlogs')
    def __unicode__(self):
                return "Room: "+str(self.room)+" for "+str(self.dateStarted)

class Entry(models.Model):
    message = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, related_name='user')
    chatlog = models.ForeignKey(ChatLog, related_name='entries')
    def __unicode__(self):
                return "log: "+str(self.chatlog)+" by: "+str(self.user)+" - "+self.message

