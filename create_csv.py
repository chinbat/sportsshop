import os,sys,csv
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportsshop.settings")
from listing1.models import Post1,Category1
with open('rtoaster.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    posts = Post1.objects.all()
    spamwriter.writerow(['CODE','NAME','GROUPING','CATEGORY','PRICE','COMMENT','URL'])
    for post in posts:
        list=[]
        list.append(str(post.id))
        list.append(post.title.encode('utf_8'))
        list.append('A'.encode('utf_8'))
        list.append(str(Category1.objects.get(sport=post.category).id))
        list.append('0'.encode('utf_8'))
        list.append(post.post_txt.encode('utf_8'))
        list.append("/media/"+post.image.name)
        spamwriter.writerow(list)
