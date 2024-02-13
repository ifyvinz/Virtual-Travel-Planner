from django.test import TestCase, Client
from .models import User, Post, Trip, Comment

# Create your tests here.

class CommentModelTest(TestCase):
    def setUp(self):
        # Create a user and a post for testing
        user = User.objects.create(username='testuser', email='test@gmail.com', password='testpassword')
        post = Post.objects.create(author = user,  title='Test Post', body='Test content', location= 'Budapest, Hungary')

    def test_valid_comment(self):
        user =User.objects.get(username='testuser')
        post =Post.objects.get(author=user)
        # Create a valid comment
        comment = Comment.objects.create(
            user=user,
            post=post,
            content='This is a valid comment',
        )

        # Check if the comment was created successfully
        self.assertEqual(comment.user, user)
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.content, 'This is a valid comment')
        

        # Check if the timestamp is set
        self.assertIsNotNone(comment.timestamp)

        # Check if the parent field is optional and can be None
        self.assertIsNone(comment.parent)

    