from app.source.views.profiles import ProfilesHandlerView
from app.source.views.skills import SkillsHandlerView
from app.source.views.files import FilesHandlerView


def setup_routes(app):
    app.router.add_view("/profiles", ProfilesHandlerView)
    app.router.add_view("/skills", SkillsHandlerView)
    app.router.add_view("/files", FilesHandlerView)

