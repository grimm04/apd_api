 
from django.conf import settings

from apscheduler.schedulers.background import BackgroundScheduler 
from .jobs import schedule_api 

def start():  
	scheduler   = BackgroundScheduler(timezone=settings.TIME_ZONE)
	scheduler.add_job(schedule_api,  'cron', day_of_week='*', hour=0, minute=5)
	scheduler.start()



