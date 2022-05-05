from app.source.views.skills_and_cv_link.methods.get import GetView
from app.source.views.skills_and_cv_link.methods.patch import UpdateView
from app.source.views.skills_and_cv_link.methods.post import CreateView
from app.source.views.skills_and_cv_link.methods.delete import DeleteView


class SkillsAndCvLinkHandlerView(
    GetView,
    UpdateView,
    CreateView,
    DeleteView
):
    pass
