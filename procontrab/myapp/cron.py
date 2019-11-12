from django_cron import CronJobBase, Schedule
from . import models

# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINS = 1 # every 2 hours

#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'nan'    # a unique code

#     def do(self):
#         req = models.Nan(nom='test')
#         req.save()


def nanus ():
    req = models.Nan(nom='test')
    req.save()
   