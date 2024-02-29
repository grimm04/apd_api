from django.test import TestCase
from datetime import datetime
# Create your tests here.
datum = '2022-05-12 16:43'
replace = (datetime.strptime(datum, '%Y-%m-%d %H:%M').minute // 30) * 30
new_date = datetime.strptime(datum, '%Y-%m-%d %H:%M').replace(minute=replace)
print(new_date)