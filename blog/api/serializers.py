from unicodedata import category
from rest_framework import serializers
from blog.models import Article, Category


class ArticleSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField('get_author_name')
    category = serializers.SerializerMethodField('get_category')

    class Meta:
        model = Article
        fields = '__all__'


    def get_author_name(self, blog_post):
        username = blog_post.author.first_name + ' ' +blog_post.author.last_name
        return username

    def get_category(self, blog_post):
        category = blog_post.category.category
        return category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'