from app.source.views.usercv.methods.get import GetView
from app.source.views.usercv.methods.patch import UpdateView
from app.source.views.usercv.methods.post import CreateView
from app.source.views.usercv.methods.delete import DeleteView


class UserCvHandlerView(
    GetView,
    UpdateView,
    CreateView,
    DeleteView
):
    pass
