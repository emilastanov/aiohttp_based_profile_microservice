from aiohttp import web


class PostgresAccessor:
    def __init__(self):
        from app.source.models import Skills
        self.skills = Skills
        from app.source.models import Files
        self.files = Files
        from app.source.models import Profiles
        self.profiles = Profiles
        # Make model in /app/source/models.py and append it here.
        # from app.source.models import Model

        # self.model_name = Model

        self.db = None

    def setup(self, application: web.Application) -> None:
        application.on_startup.append(self._on_connect)
        application.on_cleanup.append(self._on_disconnect)

    async def _on_connect(self, application: web.Application):
        from app.store.database.models import db

        self.config = application['config']['postgres']
        await db.set_bind(self.config['database_url'])
        self.db = db

    async def _on_disconnect(self, _) -> None:
        if self.db is not None:
            await self.db.pop_bind().close()

