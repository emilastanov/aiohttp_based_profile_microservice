from app.source.views.employments.methods.get import GetView
from app.source.views.employments.methods.patch import UpdateView
from app.source.views.employments.methods.post import CreateView
from app.source.views.employments.methods.delete import DeleteView


class EmploymentsHandlerView(
    GetView,
    UpdateView,
    CreateView,
    DeleteView
):
    pass
