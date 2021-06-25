"""Web Routes."""

from masonite.routes import Get, Post, Patch, RouteGroup

ROUTES = [
    RouteGroup([
        Get("/tasks", "TaskController@index"),
        Patch("/tasks/@job_id", "TaskController@update"),
    ], prefix='/4f78e969-6d98-4496-8105-0de48edddae6'),
]
