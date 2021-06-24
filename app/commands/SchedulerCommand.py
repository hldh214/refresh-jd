"""A SchedulerCommand Command."""
import time

import pendulum
import requests
import schedule
from cleo import Command

from app.models.WubaJob import WubaJob
from app.models.TaskLog import TaskLog


class SchedulerCommand(Command):
    """
    schedule.run_pending()

    scheduler:run
    """

    def handle(self):
        schedule.every(60).to(70).minutes.do(self.zppost58)
        schedule.every(60).to(70).minutes.do(self.zhaopin)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def zppost58(self):
        wuba_jobs = WubaJob.where('status', WubaJob.STATUS_RUNNING).get()

        for wuba_job in wuba_jobs:
            zp_id = wuba_job.zp_id
            res = requests.post(
                f'https://zppost.58.com/zhaopin/update/{zp_id}/submit',
                wuba_job.zp_post_data,
                headers={
                    'cookie': wuba_job.cookie,
                    'content-type': 'application/x-www-form-urlencoded'
                }
            ).text
            TaskLog.create({'task_type': 'wuba', 'task_id': wuba_job.id, 'response': res})
            wuba_job.last_run = pendulum.now()
            wuba_job.save()

    def zhaopin(self):
        pass
