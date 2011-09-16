from mongoengine import *

connect('tumblelog')

class Post(Document):
    title = StringField(max_length=120, required=True)
    author = StringField(max_length=20)

class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
    link_url = StringField()

  