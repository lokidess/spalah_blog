from django.db.models import Manager, F, Q


class PostManager(Manager):

    def get_home_posts(self):
        queryset = self.get_queryset()
        queryset = queryset.filter(
            Q(owner=1) & ~Q(owner__username='Loki'),
            title__contains=F('owner__username'),
            is_published=True
        ).order_by(
            '-published_at'
        ).select_related('owner').prefetch_related('tags')
        return queryset
