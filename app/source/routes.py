from app.source.views.educations import EducationsHandlerView
from app.source.views.profiles import ProfilesHandlerView


def setup_routes(app):
    app.router.add_view("/educations", EducationsHandlerView)
    app.router.add_view("/profiles", ProfilesHandlerView)
    
