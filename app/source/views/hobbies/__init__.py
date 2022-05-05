from app.source.views.hobbies.methods.get import GetView
from app.source.views.hobbies.methods.patch import UpdateView
from app.source.views.hobbies.methods.post import CreateView
from app.source.views.hobbies.methods.delete import DeleteView


class HobbiesHandlerView(
    GetView,
    UpdateView,
    CreateView,
    DeleteView
):
    pass
