#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install gtts


# In[2]:


from gtts import gTTS # We have imported this module 

text = "Hello Naomi. I know your are looking at my red diary. Is your surname Izinyon ? " # text that you want to convert

language = "en" #en is for english language

obj = gTTS (text= text, lang= language, slow=False)

obj.save ('sample.mp3') #to store the audio to a file with name sample


# In[ ]:




