from django.utils import timezone
from django.views.generic import TemplateView, FormView

from core.forms import AddPostForm
from core.models import Post


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(
            is_published=True
        ).order_by('-published_at')[:10]

        context.update({
            'some_list': [1, 2, 3],
            'some_dict': {'var1': 1, 'var2': 2},
            'some_str': "<b>Some text here</b>"
        })
        return context


class AddNewPostView(FormView):
    template_name = 'add_form.html'
    form_class = AddPostForm
    success_url = '/'

    def get_form_kwargs(self):
        form_kwargs = super(AddNewPostView, self).get_form_kwargs()
        if 'pk' in self.kwargs:
            form_kwargs['instance'] = Post.objects.get(id=self.kwargs['pk'])
        return form_kwargs

    def form_valid(self, form):
        post = form.save(commit=False)
        post.owner = self.request.user
        if post.is_published:
            post.published_at = timezone.now()
        post.save()
        return super(AddNewPostView, self).form_valid(form)


class Profile(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        user_posts = Post.objects.filter(
            owner=self.request.user
        )
        context['published'] = user_posts.filter(
            is_published=True)
        context['not_published'] = user_posts.filter(
            is_published=False
        )
        return context
