from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(  #get_user_model used to create a user instance and mock a logged in user
            username = "testuser",
            email = "test@email.com",
            password = "Password"
            )
        
        cls.post = Post.objects.create(
            author=cls.user,
            title="A good title",
            body="Nice body content"
            )
        
    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser") #<- checks the relation between the two models/tables as defined in models.py
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")