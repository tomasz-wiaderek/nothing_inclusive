from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from django.contrib.auth.models import User, AnonymousUser
from blog import views
from blog.models import Category, Post, Image

import secrets


class HomeViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse('blog:home'))

    def test_if_given_url_runs_correct_view(self):
        self.assertEqual(self.response.resolver_match.func, views.home)

    def test_if_response_status_is_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_if_view_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'blog/home.html')


class AboutViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse('blog:about'))

    def test_if_given_url_runs_correct_view(self):
        self.assertEqual(self.response.resolver_match.func, views.about)

    def test_if_response_status_is_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_if_view_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'blog/about.html')


class PostsByAuthorViewTests(TestCase):

    def setUp(self):
        username = secrets.token_hex(4)
        email = f'{username}@mail.com'
        password = secrets.token_hex(4)
        author = User.objects.create_user(username=username, email=email, password=password)

        self.client = Client()
        self.response = self.client.get(reverse('blog:posts-by-author', args=[author.pk]))

    def test_if_given_url_runs_correct_view(self):
        self.assertEqual(self.response.resolver_match.func, views.list_posts_by_author)

    def test_if_response_status_is_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_if_view_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'blog/posts_filtered.html')


class PostViewsTests(TestCase):

    def setUp(self):

        username = secrets.token_hex(4)
        email = f'{username}@mail.com'
        password = secrets.token_hex(4)
        self.author = User.objects.create_user(username=username, email=email, password=password)
        self.category = Category.objects.create(name='New test category')
        self.new_post = Post.objects.create(
            title='Lorem Ipsum',
            intro='Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...',
            content='There is no one who loves pain itself, who seeks after it and wants to have it...',
            author=self.author,
            category=self.category
        )
        Image.objects.create(
            name='Random name',
            slug='random-name',
            image='random.jpg',
            is_header=False,
            owner=self.author,
            post=self.new_post
        )

        self.client = Client()
        self.factory = RequestFactory()

    def test_if_given_url_runs_post_detail_view(self):
        response = self.client.get(reverse('blog:post-detail', args=[self.new_post.pk]))
        self.assertEqual(response.resolver_match.func, views.post_detail_view)

    def test_post_detail_view_if_response_status_is_200(self):
        response = self.client.get(reverse('blog:post-detail', args=[self.new_post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_if_uses_correct_template(self):
        response = self.client.get(reverse('blog:post-detail', args=[self.new_post.pk]))
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_detail_view_if_context_object_is_correct(self):
        response = self.client.get(reverse('blog:post-detail', args=[self.new_post.pk]))
        self.assertEqual(response.context['object'], self.new_post)

    def test_post_detail_view_if_context_images_is_correct(self):
        response = self.client.get(reverse('blog:post-detail', args=[self.new_post.pk]))
        posts_images = Image.objects.filter(post=response.context['object'])
        self.assertQuerysetEqual(response.context['images'], posts_images)

    def test_post_create_view_if_adds_new_post(self):
        data = {
            'title': 'Lorem Ipsum2',
            'intro': 'Neque porro quisquam...',
            'content': 'Neque porro quisquam... - There is no...',
            'category': self.category
        }
        request = self.factory.post(reverse('blog:post-create'), data=data)
        request.user = self.author
        response = views.post_create_view(request)

        # p = Post.objects.create(
        #     title=data['title'],
        #     intro=data['intro'],
        #     content=data['content'],
        #     author=self.author,
        #     category=self.category
        # )
        newest_post = Post.objects.order_by('-date').first()
        # print(p, p.date)
        print(newest_post, newest_post.date)
        print(Post.objects.all())
        #
        self.assertEqual(newest_post.title, 'Lorem Ipsum2')
