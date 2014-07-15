import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import resolve,reverse
from listing1.models import Post1

class PostMethodTest(TestCase):
    def test_return_the_title_true(self):
        post = Post1(title="This is TITLE")
        self.assertEqual(post.__unicode__(),"This is TITLE")
    def test_return_the_title_false(self):
        post = Post1(title="This is TITLE")
        self.assertEqual(post.__unicode__(),"This is TITLE")



def create_post(set,before):
    return Post1.objects.create(category_id=1,posted_by_id=1,title=set,pub_date=datetime.datetime.now()-datetime.timedelta(days=before),deleted=False)

class PostViewTests(TestCase):
    def test_index_status(self):
        create_post("Post1",before=4)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_content(self):
        create_post("Post1",before=4)
        response = self.client.get(reverse('index'))
        self.assertContains(response,"Post1")

    def test_index_order(self):
        create_post(set="Post4", before=4)
        create_post(set="Post3", before=3)
        create_post(set="Oldest", before=10)
        create_post(set="Newest", before=1)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(response.context['posts'],['<Post1: Newest>','<Post1: Post3>','<Post1: Post4>','<Post1: Oldest>'])











