 
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment
from user.models import Profile

class PostTestClass(TestCase):
    """test class for Post model"""

    def setUp(self):

        self.user = User.objects.create_user("testuser", "secret")

        self.new_profile = Profile(profile_pics="https://cdn.statically.io/img/wallpaperaccess.com/full/819472.jpg", owner=self.user)
        self.new_profile.save()

        self.new_image = Image(pic="https://cdn.statically.io/img/wallpaperaccess.com/full/819472.jpg",
                               caption="image", profile=self.new_profile)

    def test_instance_true(self):
        self.new_image.save()
        self.assertTrue(isinstance(self.new_post, Post))

    def test_save_image_method(self):
        self.new_post.save_post()
        images = Post.objects.all()
        self.assertTrue(len(posts) == 1)

    def tearDown(self):
        Post.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()

class CommentTestClass(TestCase):
    
    """Test class for Comment Model"""

    def setUp(self):
        self.new_user = User.objects.create_user("testuser", "secret")

        self.new_profile = Profile(profile_pics='https://ucarecdn.com/620ac26e-19f7-4c0a-86d1-2b4e4b195fa8/-/crop/610x452/15,0/-/preview/',
                                     bio="this is a test bio",
                                     owner=self.new_user)
        self.new_profile.save()

        self.new_image = Image(pic='https://ucarecdn.com/620ac26e-19f7-4c0a-86d1-2b4e4b195fa8/-/crop/610x452/15,0/-/preview/',
                               caption="this is a test image", profile='',profile_details=self.new_user)
        self.new_image.save()

        self.new_comment = Comment(
            image=self.new_image, comment_owner=self.new_profile, comment="this is a comment on a post")

    def test_instance_true(self):
        self.new_comment.save()
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        self.new_comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()
        Comment.objects.all().delete()
