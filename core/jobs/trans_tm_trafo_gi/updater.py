from datetime import datetime
from django.conf import settings
 
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone
from .jobs import schedule_api
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger

def start():  
	scheduler   = BackgroundScheduler(timezone=settings.TIME_ZONE)
	scheduler.add_job(schedule_api,  'cron', day_of_week='*', hour=19, minute=20)
	scheduler.start()



