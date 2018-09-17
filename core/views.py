from datetime import timedelta

from django.contrib.auth.models import User
from django.db.models import Count, Q, F
from django.db.models.functions import datetime
from django.utils import timezone
from django.views.generic import TemplateView, FormView

from core.forms import AddPostForm, FilterForm
from core.models import Post, Tags
# from blog.settings import SOME_MY_SETTING
from django.conf import settings

from core.tasks import test_task


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        post = Post.objects.all().order_by('-created_at').first()
        post.tags.add(Tags.objects.get(id=4))
        context['posts'] = Post.objects.get_home_posts()
        # test_task.apply_async(eta=timezone.now() + timedelta(seconds=10))
        # test_task.apply_async(countdown=10)
        # posts_counts = User.objects.all().annotate(Count('post'))
        # import pprint
        # pprint.pprint(
        #     [
        #         {'name': x.username, 'post_count': x.post__count}
        #         for x in posts_counts
        #     ]
        # )
        if 'view_count' not in self.request.session:
            self.request.session['view_count'] = 0
        self.request.session['view_count'] += 1
        self.request.session.save()
        context.update({
            'some_list': [1, 2, 3],
            'my_setting': settings.SOME_MY_SETTING,
            'view_count': self.request.session['view_count']
        })
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['some'] = 'value'
        return self.render_to_response(context)

    def post(self, request):
        import stripe
        stripe.api_key = "sk_test_W2nPa0MJ6XqaI0gvvcpwIKOc"

        stripe.Charge.create(
            amount=10000,
            currency="usd",
            source=request.POST['stripeToken'],  # obtained with Stripe.js
            description="Test payment",
            application_fee=100,
            capture=False
        )
        return self.render_to_response(
            self.get_context_data()
        )


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


class FilterView(FormView):
    template_name = "filters.html"
    form_class = FilterForm
