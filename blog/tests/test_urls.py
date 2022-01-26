from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog import views


class TestBlogUrls(SimpleTestCase):

    def test_home_url_runs_correct_view(self):
        url = '/'
        view_func = resolve(url).func
        self.assertEqual(view_func, views.home)

    def test_home_url_name_runs_correct_view(self):
        url = reverse('blog:home')
        view_func = resolve(url).func
        self.assertEqual(view_func, views.home)

    def test_about_url_runs_correct_view(self):
        url = '/about/'
        view_func = resolve(url).func
        self.assertEqual(view_func, views.about)

    def test_about_url_name_runs_correct_view(self):
        url = reverse('blog:about')
        view_func = resolve(url).func
        self.assertEqual(view_func, views.about)

    def test_author_url_runs_correct_view(self):
        url = '/author/1/'
        view_func = resolve(url).func
        self.assertEqual(view_func, views.list_posts_by_author)

    def test_author_url_name_runs_correct_view(self):
        url = reverse('blog:posts-by-author', args=[1])
        view_func = resolve(url).func
        self.assertEqual(view_func, views.list_posts_by_author)

    def test_category_url_runs_correct_view(self):
        url = '/category/some_category/'
        view_func = resolve(url).func
        self.assertEqual(view_func, views.list_posts_by_category)

    def test_category_url_name_runs_correct_view(self):
        url = reverse('blog:posts-by-category', args=['some_category'])
        view_func = resolve(url).func
        self.assertEqual(view_func, views.list_posts_by_category)

    def test_post_new_url_runs_correct_view(self):
        url = '/post/new/'
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, views.PostCreateView)

    def test_post_new_url_name_runs_correct_view(self):
        url = reverse('blog:post-create')
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, views.PostCreateView)

    def test_post_detail_url_runs_correct_view(self):
        url = '/post/1/'
        view_func = resolve(url).func
        self.assertEqual(view_func, views.post_detail_view)

    def test_post_detail_url_name_runs_correct_view(self):
        url = reverse('blog:post-detail', args=[1])
        view_func = resolve(url).func
        self.assertEqual(view_func, views.post_detail_view)

    def test_post_update_url_runs_correct_view(self):
        url = '/post/1/update/'
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, views.PostUpdateView)

    def test_post_update_url_name_runs_correct_view(self):
        url = reverse('blog:post-update', args=[1])
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, views.PostUpdateView)

    def test_post_delete_url_runs_correct_view(self):
        url = '/post/1/delete/'
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, views.PostDeleteView)

    def test_post_delete_url_name_runs_correct_view(self):
        url = reverse('blog:post-delete', args=[1])
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, views.PostDeleteView)

    def test_image_url_runs_correct_view(self):
        url = '/image/'
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, views.ImageListView)

    def test_image_url_name_runs_correct_view(self):
        url = reverse('blog:image-list')
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, views.ImageListView)

    def test_image_new_url_runs_correct_view(self):
        url = '/image/new/'
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, views.ImageCreateView)

    def test_image_new_url_name_runs_correct_view(self):
        url = reverse('blog:image-create')
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, views.ImageCreateView)

    def test_image_detail_url_runs_correct_view(self):
        url = '/image/some_slug/'
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, views.ImageDetailView)

    def test_image_detail_url_name_runs_correct_view(self):
        url = reverse('blog:image-detail', args=['some_slug'])
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, views.ImageDetailView)

    def test_image_update_url_runs_correct_view(self):
        url = '/image/some_slug/update/'
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, views.ImageUpdateView)

    def test_image_update_url_name_runs_correct_view(self):
        url = reverse('blog:image-update', args=['some_slug'])
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, views.ImageUpdateView)

    def test_image_delete_url_runs_correct_view(self):
        url = '/image/some_slug/delete/'
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, views.ImageDeleteView)

    def test_image_delete_url_name_runs_correct_view(self):
        url = reverse('blog:image-delete', args=['some_slug'])
        view_func = resolve(url).func.view_class
        self.assertEqual(view_func, views.ImageDeleteView)
