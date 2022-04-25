from aiohttp import web


class PostgresAccessor:
    def __init__(self):
        from app.source.models import Educations
        self.educations = Educations
        from app.source.models import Profiles
        self.profiles = Profiles

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

