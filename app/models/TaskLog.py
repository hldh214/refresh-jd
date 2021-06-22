"""TaskLog Model."""

from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin


class TaskLog(Model, SoftDeletesMixin):
    """TaskLog Model."""
    __timezone__ = "Asia/Hong_Kong"

