from app.source.views.profiles import ProfilesHandlerView


def setup_routes(app):
    app.router.add_view("/profiles", ProfilesHandlerView)
    
