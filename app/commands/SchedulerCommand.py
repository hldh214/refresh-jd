"""A SchedulerCommand Command."""
import time

import pendulum
import requests
import schedule
from cleo import Command

from app.models.Task import Task
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
        tasks = Task.where('type', Task.TYPE_WUBA) \
            .where('status', Task.STATUS_RUNNING) \
            .get()

        for task in tasks:
            zp_id = task.data.get('zp_id')
            res = requests.post(
                f'https://zppost.58.com/zhaopin/update/{zp_id}/submit',
                task.data.get('zp_post_data'),
                headers={
                    'cookie': task.data.get('cookie'),
                    'content-type': 'application/x-www-form-urlencoded'
                }
            ).text
            TaskLog.create({'task_id': task.id, 'response': res})
            task.last_run = pendulum.now()
            task.save()

    def zhaopin(self):
        tasks = Task.where('type', Task.TYPE_ZHAOPIN) \
            .where('status', Task.STATUS_RUNNING) \
            .get()

        for task in tasks:
            res = requests.post(
                'https://rd.zhaopin.com/api/app/v2/job',
                task.data.get('data').encode(),
                headers={
                    'user-agent': 'One(Android/10) (com.zhaopin.ihr/8.2.2) Weex/0.28.0 1080x1920',
                    'x-zp-at': 'fed15c44a571483889eb4ca14175d0ec',
                    'x-zp-business-system': '23',
                    'x-zp-channel': 'tengxun',
                    'x-zp-client-id': '00000000-4b77-6398-ffff-ffffef05ac4a',
                    'x-zp-client-type': 'a',
                    'x-zp-departmentid': '310895831',
                    'x-zp-device-id': '00000000-4b77-6398-ffff-ffffef05ac4a',
                    'x-zp-rt': 'b37d49dd36894b2ab7b8f51d59a1b222',
                    'x-zp-user-agent': '',
                    'x-zp-user-role': 'ENTERPRISE',
                    'x-zp-utm-client-version': 'u',
                    'x-zp-version': '8.2.2',
                    'Content-Type': 'application/json',
                    'wToken': task.data.get('w_token')
                }
            ).text
            TaskLog.create({'task_id': task.id, 'response': res})
            task.last_run = pendulum.now()
            task.save()
