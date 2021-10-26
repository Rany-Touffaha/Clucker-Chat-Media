"""Unit tests for the Post Form"""
from django import forms
from django.test import TestCase
from microblogs.forms import PostForm
from microblogs.models import Post


class PostFormTestCase(TestCase):
    """Unit tests for the Sign up Form"""

    def setUp(self):
        self.form_input = {
            'text': 'Yesterday, I had great time celebrating my birthday! '
                    'I\'m glad I was able to see my cousins after all these years!'
        }

    def test_valid_post_form(self):
        form = PostForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_uses_model_validation(self):
        self.form_input['text'] = 'x' * 281
        form = PostForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_post_must_save_correctly(self):
        form = PostForm(data=self.form_input)
        before_count = Post.objects.count()
        form.save()
        after_count = Post.objects.count()
        self.assertEqual(after_count, before_count + 1)
