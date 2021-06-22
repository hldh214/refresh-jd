"""WubaJob Model."""

from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masoniteorm.relationships import has_many

from app.models.TaskLog import TaskLog


class WubaJob(Model, SoftDeletesMixin):
    """WubaJob Model."""
    __timezone__ = "Asia/Hong_Kong"

    @has_many('task_id', 'id')
    def task_logs(self):
        return TaskLog
