from app.source.views.hobbies_and_cv_link.methods.get import GetView
from app.source.views.hobbies_and_cv_link.methods.patch import UpdateView
from app.source.views.hobbies_and_cv_link.methods.post import CreateView
from app.source.views.hobbies_and_cv_link.methods.delete import DeleteView


class HobbiesAndCvLinkHandlerView(
    GetView,
    UpdateView,
    CreateView,
    DeleteView
):
    pass
