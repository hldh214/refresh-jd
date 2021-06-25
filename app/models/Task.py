"""Task Model."""

from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masoniteorm.relationships import has_many

from app.models.TaskLog import TaskLog


class Task(Model, SoftDeletesMixin):
    """Task Model."""
    __timezone__ = "Asia/Hong_Kong"

    __guarded__ = ['id']

    __casts__ = {'data': 'json'}

    STATUS_PAUSED = 'STATUS_PAUSED'
    STATUS_RUNNING = 'STATUS_RUNNING'

    TYPE_WUBA = 'wuba'
    TYPE_ZHAOPIN = 'zhaopin'

    @has_many('task_id', 'id')
    def task_logs(self):
        return TaskLog
