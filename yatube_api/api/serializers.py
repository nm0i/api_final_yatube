from posts.models import Comment, Follow, Group, Post, User
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import (CurrentUserDefault, ModelSerializer,
                                        ValidationError)
from rest_framework.validators import UniqueTogetherValidator


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = (
            "id",
            "author",
            "text",
            "pub_date",
            "image",
            "group",
        )
        model = Post


class GroupSerializer(ModelSerializer):
    class Meta:
        fields = ("id", "slug", "description", "title")
        model = Group


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        fields = ("id", "author", "text", "created", "post")
        read_only_fields = (
            "post",
            "author",
        )
        model = Comment


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=CurrentUserDefault(),
    )
    following = SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = ('following', 'user',)
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('following', 'user',),
                message='Already subscribed.'
            )
        ]

    def validate_following(self, value):
        user = self.context.get('request').user
        if user == value:
            raise ValidationError("Self subscriptions aren't allowed.")
        return value
