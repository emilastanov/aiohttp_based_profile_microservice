from app.source.views.achievements.methods.get import GetView
from app.source.views.achievements.methods.patch import UpdateView
from app.source.views.achievements.methods.post import CreateView
from app.source.views.achievements.methods.delete import DeleteView


class AchievmentsHandlerView(
    GetView,
    UpdateView,
    CreateView,
    DeleteView
):
    pass
