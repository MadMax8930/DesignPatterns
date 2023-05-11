#Behavioral Pattern

class YoutubeChannel:
   def __init__(self, name):
      self.person = name
      self.subscribers = []
      
   def subscribe(self, sub):
      self.subscribers.append(sub)
      
   def notify(self, event):
      for sub in self.subscribers:
         sub.sendNotification(self.person, event)
         
from abc import ABC, abstractmethod

class YoutubeSubscriber(ABC):
   @abstractmethod
   def sendNotification(self, event):
      pass
   
class YoutubeUser(YoutubeSubscriber):
   def __init__(self, name):
      self.person = name
      
   def sendNotification(self, channel, event):
      print(f"User {self.person} received notification from {channel}: {event}")
      
channel = YoutubeChannel("MadMax8930")

channel.subscribe(YoutubeUser("sub1"))  #User sub1 received notification from MadMax8930: A new video released
channel.subscribe(YoutubeUser("sub2"))  #User sub2 received notification from MadMax8930: A new video released
channel.subscribe(YoutubeUser("sub3"))  #User sub3 received notification from MadMax8930: A new video released

channel.notify("A new video released")