from rest_framework import serializers
from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField('get_author_name')
    category = serializers.SerializerMethodField('get_category')
    date = serializers.SerializerMethodField('get_date')

    class Meta:
        model = Article
        exclude = ['created_on', 'updated_on', 'visibility']


    def get_author_name(self, blog_post):
        username = blog_post.author.first_name + ' ' +blog_post.author.last_name
        return username

    def get_category(self, blog_post):
        category = blog_post.category.category
        return category

    def get_date(self, blog_post):
        return blog_post.updated_on.strftime("%d-%m-%Y")