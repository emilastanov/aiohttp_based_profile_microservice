from app.source.views.driverlicense.methods.get import GetView
from app.source.views.driverlicense.methods.patch import UpdateView
from app.source.views.driverlicense.methods.post import CreateView
from app.source.views.driverlicense.methods.delete import DeleteView


class DriverlicenseHandlerView(
    GetView,
    UpdateView,
    CreateView,
    DeleteView
):
    pass
