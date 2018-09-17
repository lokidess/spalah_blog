from rest_framework import serializers

from core.models import Post, Tags


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    owner_full_name = serializers.SerializerMethodField()
    tags = TagsSerializer(many=True, read_only=True)
    owner_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Post
        fields = ('title', 'body', 'published_at', 'tags',
                  'owner_full_name', 'owner_id')

    def get_owner_full_name(self, obj):
        return f"{obj.owner.first_name} {obj.owner.last_name}"
