from app.source.views.hobbies_and_cv_link import HobbiesAndCvLinkHandlerView
from app.source.views.skills_and_cv_link import SkillsAndCvLinkHandlerView
from app.source.views.driver_licenses_and_cv_link import DriverLicensesAndCvLinkHandlerView
from app.source.views.educations_and_cv_link import EduactionsAndCvLinkHandlerView
from app.source.views.achievements_and_cv_link import AchievementsAndCVLinkHandlerView
from app.source.views.hobbies import HobbiesHandlerView
from app.source.views.driverlicense import DriverlicenseHandlerView
from app.source.views.achievements import AchievmentsHandlerView
from app.source.views.usercv import UserCvHandlerView
from app.source.views.educations import EducationsHandlerView
from app.source.views.profiles import ProfilesHandlerView
from app.source.views.skills import SkillsHandlerView
from app.source.views.files import FilesHandlerView


def setup_routes(app):
    app.router.add_view("/hobbies_and_cv_link", HobbiesAndCvLinkHandlerView)
    app.router.add_view("/skills_and_cv_link", SkillsAndCvLinkHandlerView)
    app.router.add_view("/driver_licenses_and_cv_link", DriverLicensesAndCvLinkHandlerView)
    app.router.add_view("/educations_and_cv_link", EduactionsAndCvLinkHandlerView)
    app.router.add_view("/achievements_and_cv_link", AchievementsAndCVLinkHandlerView)
    app.router.add_view("/hobbies", HobbiesHandlerView)
    app.router.add_view("/driver_licenses", DriverlicenseHandlerView)
    app.router.add_view("/achievements", AchievmentsHandlerView)
    app.router.add_view("/cv", UserCvHandlerView)
    app.router.add_view("/educations", EducationsHandlerView)
    app.router.add_view("/profiles", ProfilesHandlerView)
    app.router.add_view("/skills", SkillsHandlerView)
    app.router.add_view("/files", FilesHandlerView)

