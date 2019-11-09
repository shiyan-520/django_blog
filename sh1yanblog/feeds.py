from django.contrib.syndication.views import Feed
from django.urls import reverse
from index.models import Index_Body

class BlogRssFeed(Feed):
    title = "shiyan 'blog"
    link = "/rss/"
    def items(self):
        return Index_Body.objects.all()
    def item_title(self, item):
        return item.blog_body_name
    def item_description(self, item):
        return item.blog_body_context
    def item_link(self, item):
        return reverse('blog_Article', args=[item.id,])
