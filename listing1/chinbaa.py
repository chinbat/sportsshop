import datetime

from django.utils import timezone


pub_date = timezone.now()-datetime.timedelta(days=1)

print(str(pub_date))
