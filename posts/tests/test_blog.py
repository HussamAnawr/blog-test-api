from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Post

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            name = 'Hussam Ghunaim',
            username = 'hussam',
            email = 'o.hos@hussam.com',
            password = 'hussam123',
        )
        cls.post = Post.objects.create(
            title = 'Perfect title',
            body = 'Nice body content is here.',
            author = cls.user
        )
    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'hussam')
        self.assertEqual(self.post.title , 'Perfect title')
        self.assertEqual(str(self.user.posts.all()[0]), 'Perfect title')