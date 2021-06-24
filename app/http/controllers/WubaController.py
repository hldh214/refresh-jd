""" A WubaController Module """

from masonite.auth import Auth
from masonite.view import View
from masonite.controllers import Controller
from masonite.request import Request
from masonite.helpers import compact
from app.models.WubaJob import WubaJob


class WubaController(Controller):
    """Class Docstring Description
    """
    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", WubaController)
        """

        pass

    def index(self, view: View):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", WubaController)
        """

        wuba_jobs = WubaJob.all()

        return view.render('wuba/index', compact(wuba_jobs))

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", WubaController)
        """

        pass

    def store(self):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", WubaController)
        """

        pass

    def edit(self):
        """Show form to edit an existing resource listing
        ex. Get().route("/edit", WubaController)
        """

        pass

    def update(self, job_id, request: Request):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", WubaController)
        """

        WubaJob.find(job_id).update(request.all())

        return {}

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", WubaController)
        """

        pass
