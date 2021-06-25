""" A TaskController Module """

from masonite.controllers import Controller
from masonite.request import Request
from masonite.helpers import compact
from app.models.Task import Task


class TaskController(Controller):
    """Class Docstring Description
    """

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", TaskController)
        """

        pass

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", TaskController)
        """
        tasks = Task.get(['id', 'type', 'name', 'status', 'last_run', 'created_at']).to_json()

        return tasks

    def store(self):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", TaskController)
        """

        pass

    def update(self, job_id, request: Request):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", TaskController)
        """

        Task.find(job_id).update(request.all())

        return {}

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", TaskController)
        """

        pass
