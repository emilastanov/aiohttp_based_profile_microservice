from aiohttp import web


class PostgresAccessor:
    def __init__(self):
        from app.source.models import EmploymentsAndCvLink
        self.employments_and_cv_link = EmploymentsAndCvLink
        from app.source.models import Employments
        self.employments = Employments
        from app.source.models import HobbiesAndCvLink
        self.hobbies_and_cv_link = HobbiesAndCvLink
        from app.source.models import SkillsAndCvLink
        self.skills_and_cv_link = SkillsAndCvLink
        from app.source.models import DriverLicensesAndCvLink
        self.driver_licenses_and_cv_link = DriverLicensesAndCvLink
        from app.source.models import EducationsAndCvLink
        self.educations_and_cv_link = EducationsAndCvLink
        from app.source.models import AchievementsAndCvLink
        self.achievements_and_cv_link = AchievementsAndCvLink
        from app.source.models import Hobbies
        self.hobbies = Hobbies
        from app.source.models import DriverLicense
        self.driver_license = DriverLicense
        from app.source.models import Achievements
        self.achievements = Achievements
        from app.source.models import UserCv
        self.user_cv = UserCv
        from app.source.models import Educations
        self.educations = Educations
        from app.source.models import Profiles
        self.profiles = Profiles
        from app.source.models import Skills
        self.skills = Skills
        from app.source.models import Files
        self.files = Files

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

