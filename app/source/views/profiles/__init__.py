from app.source.views.profiles.methods.get import GetView
from app.source.views.profiles.methods.patch import UpdateView
from app.source.views.profiles.methods.post import CreateView
from app.source.views.profiles.methods.delete import DeleteView


class ProfilesHandlerView(
    GetView,
    UpdateView,
    CreateView,
    DeleteView
):
    pass
