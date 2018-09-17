from rest_framework import viewsets
from api.serializers import PostSerializer
from core.models import Post


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.none()

    def get_queryset(self):
        if 'owner_id' in self.request.GET:
            return Post.objects.filter(
                owner__id=self.request.GET['owner_id']
            ).select_related().prefetch_related('tags')
        return Post.objects.all().select_related().prefetch_related('tags')
