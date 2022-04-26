from app.source.views.files.methods.get import GetView
from app.source.views.files.methods.patch import UpdateView
from app.source.views.files.methods.post import CreateView
from app.source.views.files.methods.delete import DeleteView


class FilesHandlerView(
    GetView,
    UpdateView,
    CreateView,
    DeleteView
):
    pass
