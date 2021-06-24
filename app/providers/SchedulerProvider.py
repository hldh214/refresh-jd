"""A SchedulerProvider Service Provider."""

from masonite.provider import ServiceProvider

from app.commands.SchedulerCommand import SchedulerCommand


class SchedulerProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        self.app.bind('SchedulerCommand', SchedulerCommand())

    def boot(self):
        """Boots services required by the container."""
        pass
