from aiohttp import web

from app.middlewares.objects import get_object_by_id, get_objects
from app.middlewares.errors import UnknownObject, NoId
from app.source.data_formats import query_data, UNKNOWN_OBJECT
from app.source.views.usercv.methods.get.document import swagger_extension
from app.source.views.usercv.methods import table_name
from app.source.views.educations_and_cv_link.methods import name as EDUCATIONS_AND_CV_LINK
from app.source.views.achievements_and_cv_link.methods import table_name as ACHIEVEMENTS_AND_CV_LINK
from app.source.views.educations.methods import name as EDUCATIONS
from app.source.views.achievements.methods import name as ACHIEVEMENTS
from app.source.views.driverlicense.methods import name as DRIVER_LICENSE
from app.source.views.driver_licenses_and_cv_link.methods import name as DRIVER_LICENSES_AND_CV_LINK
from app.source.views.skills.methods import name as SKILLS
from app.source.views.skills_and_cv_link.methods import name as SKILLS_AND_CV_LINK
from app.source.views.hobbies.methods import name as HOBBIES
from app.source.views.hobbies_and_cv_link.methods import name as HOBBIES_AND_CV_LINK
from app.source.models import (
    Educations,
    EducationsAndCvLink,
    Achievements,
    AchievementsAndCvLink,
    DriverLicense,
    DriverLicensesAndCvLink,
    Skills,
    SkillsAndCvLink,
    Hobbies,
    HobbiesAndCvLink
)


__all__ = ('Handler',)


async def enrich_data(_object, model_name, model, link_model_name, link_model, field):
    links_data = await get_objects(
        None,
        model_name=link_model_name,  # EDUCATIONS_AND_CV_LINK,
        condition=link_model.cv == _object['id']  # EducationsAndCvLink.cv == _object['id']
    )

    objects = []
    for link in links_data['data']:
        addon = await get_objects(
            None,
            model_name=model_name,
            condition=model.id == link[field]
        )
        objects.append(addon['data'][0])

    _object[model_name.lower()] = objects


class Handler(web.View):

    @swagger_extension
    async def get(self):

        try:
            _object = await get_object_by_id(self.request, table_name)
            await enrich_data(
                _object, EDUCATIONS, Educations, EDUCATIONS_AND_CV_LINK, EducationsAndCvLink, 'education'
            )
            await enrich_data(
                _object, ACHIEVEMENTS, Achievements, ACHIEVEMENTS_AND_CV_LINK, AchievementsAndCvLink, 'achievement'
            )
            await enrich_data(
                _object, DRIVER_LICENSE, DriverLicense, DRIVER_LICENSES_AND_CV_LINK, DriverLicensesAndCvLink, 'driver_license'
            )
            await enrich_data(
                _object, SKILLS, Skills, SKILLS_AND_CV_LINK, SkillsAndCvLink, 'skill'
            )
            await enrich_data(
                _object, HOBBIES, Hobbies, HOBBIES_AND_CV_LINK, HobbiesAndCvLink, 'hobby'
            )

            response = query_data(_object)

        except UnknownObject:
            response = UNKNOWN_OBJECT

        except NoId:
            objects = await get_objects(self.request, table_name)
            response = query_data(**objects)

        return web.json_response(**response)
