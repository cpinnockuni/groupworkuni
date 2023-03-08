from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import time 

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username





def postdetails():
    #Username 
    #Mesasage 
    #messagelimit 500 
    #catergory
    #timestamp
    pass 



def indexing():
    pass 