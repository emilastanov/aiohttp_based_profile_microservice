from app.source.views.skills.methods.get import GetView
from app.source.views.skills.methods.patch import UpdateView
from app.source.views.skills.methods.post import CreateView
from app.source.views.skills.methods.delete import DeleteView


class SkillsHandlerView(
    GetView,
    UpdateView,
    CreateView,
    DeleteView
):
    pass
