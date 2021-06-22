"""User Model."""

from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin


class User(Model, SoftDeletesMixin):
    """User Model."""

    __timezone__ = "Asia/Hong_Kong"

    __fillable__ = ["name", "email", "password"]

    __auth__ = "email"
