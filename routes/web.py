"""Web Routes."""

from masonite.routes import Get, Post, Patch, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    RouteGroup([
        Get("/login", "auth.LoginController@show").name("login"),
        Get("/logout", "auth.LoginController@logout").name("logout"),
        Post("/login", "auth.LoginController@store"),
        # Get("/register", "auth.RegisterController@show").name("register"),
        # Post("/register", "auth.RegisterController@store"),
        Get("/home", "auth.HomeController@show").name("home"),
    ]),
    RouteGroup([
        Get("/tasks", "TaskController@index"),
        Patch("/tasks/@job_id", "TaskController@update"),
    ], middleware=('auth',)),
]
