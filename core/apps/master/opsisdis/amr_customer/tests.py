from django.test import TestCase
from datetime import datetime, timedelta

# Create your tests here.
date = '2022-05-12 15:00'
# replace = (datetime.now().minute // 30) * 30
replace = (datetime.strptime(date, '%Y-%m-%d %H:%M').minute // 30) * 30
date = datetime.strptime(date, '%Y-%m-%d %H:%M').replace(minute=replace)
print(date)