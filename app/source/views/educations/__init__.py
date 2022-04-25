from app.source.views.educations.methods.get import GetView
from app.source.views.educations.methods.patch import UpdateView
from app.source.views.educations.methods.post import CreateView
from app.source.views.educations.methods.delete import DeleteView


class EducationsHandlerView(
    GetView,
    UpdateView,
    CreateView,
    DeleteView
):
    pass
