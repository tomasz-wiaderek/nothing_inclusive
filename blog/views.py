from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import Post, Category, Image


def home(request):
    posts = Post.objects.order_by('-date')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/home.html', context={'page_obj': page_obj})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def list_posts_by_author(request, pk):
    user = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(author=user).order_by('-date')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'author': user
    }
    return render(request, 'blog/posts_filtered.html', context=context)


def list_posts_by_category(request, name):
    category = get_object_or_404(Category, name=name)
    posts = Post.objects.filter(category=category).order_by('-date')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'category': category
    }
    return render(request, 'blog/posts_filtered.html', context=context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'intro', 'content', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def post_detail_view(request, pk):
    post = Post.objects.get(pk=pk)
    images = Image.objects.filter(post=post)
    context = {
        'object': post,
        'images': images
    }
    return render(request, template_name='blog/post_detail.html', context=context)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'intro', 'content', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['name', 'image', 'is_header', 'post']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ImageDetailView(DetailView):
    model = Image


class ImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Image
    success_url = reverse_lazy('blog:image-list')
    fields = ['name', 'image', 'is_header', 'post']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        image = self.get_object()
        if self.request.user == image.owner:
            return True
        return False


class ImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Image
    success_url = reverse_lazy('blog:image-list')

    def test_func(self):
        image = self.get_object()
        if self.request.user == image.owner:
            return True
        return False


class ImageListView(LoginRequiredMixin, ListView):
    model = Image
    paginate_by = 10
