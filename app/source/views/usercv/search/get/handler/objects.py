from app.store.database.models import db


async def filter_cv(params: dict, limit=100, offset=0):

    conditions = []

    if params.get('skills'):
        conditions.append('s.skill = ANY(:skills)')
    if params.get('hobbies'):
        conditions.append('h.hobby = ANY(:hobbies)')
    if params.get('driver_licenses'):
        conditions.append('d.driver_license = ANY(:driver_licenses)')
    if params.get('educations'):
        conditions.append('e.education = ANY(:educations)')
    if params.get('employments'):
        conditions.append('em.employment = ANY(:employments)')
    if params.get('min_salary'):
        conditions.append('cv.wish_salary >= :min_salary')
    if params.get('wish_salary'):
        conditions.append('cv.wish_salary <= :wish_salary')
    if params.get('military_duty'):
        conditions.append('cv.military_duty = :military_duty')
    if params.get('possibility_of_moving'):
        conditions.append('cv.possibility_of_moving = :possibility_of_moving')
    if params.get('work_format'):
        conditions.append('cv.work_format = :work_format')
    if params.get('marital_status'):
        conditions.append('cv.marital_status = :marital_status')
    if params.get('wish_position'):
        conditions.append('cv.wish_position = :wish_position')

    query_text = (
        "SELECT\n"
        "       cv.id,\n"
        "       cv.wish_position,\n"
        "       cv.military_duty,\n"
        "       cv.possibility_of_moving,\n"
        "       cv.marital_status,\n"
        "       f.link,\n"
        "       cv.wish_salary,\n"
        "       p.first_name,\n"
        "       p.last_name,\n"
        "       p.date_of_birthday\n"
        "FROM user_cv as cv\n"
        f"{'INNER JOIN skills_and_cv_link as s ON cv.id = s.cv ' if params.get('skills') else ''}"
        f"{'INNER JOIN achievements_and_cv_link as a ON cv.id = a.cv ' if params.get('achievements') else ''}"
        f"{'INNER JOIN hobbies_and_cv_link as h ON cv.id = h.cv ' if params.get('hobbies') else ''}"
        f"{'INNER JOIN driver_licenses_and_cv_link as d ON cv.id = d.cv ' if params.get('driver_licenses') else ''}"
        f"{'INNER JOIN educations_and_cv_link as e ON cv.id = e.cv ' if params.get('educations') else ''}"
        f"{'INNER JOIN employments_and_cv_link as em ON cv.id = em.cv ' if params.get('employments') else ''}"
        "INNER JOIN profiles p on cv.profile = p.id\n"
        "INNER JOIN files f on cv.avatar = f.id\n"
        f"{'WHERE ' if params else ''}\n" +
        ' and '.join(conditions) +
        " GROUP BY cv.id, p.id, f.link\n"
        f"LIMIT {limit} "
        f"OFFSET {offset}"
    )

    count_query_text = (
        "SELECT sum(T.cnt) FROM (SELECT\n"
        "       count(cv.id) as cnt\n"
        "FROM user_cv as cv\n"
        f"{'INNER JOIN skills_and_cv_link as s ON cv.id = s.cv ' if params.get('skills') else ''}"
        f"{'INNER JOIN achievements_and_cv_link as a ON cv.id = a.cv ' if params.get('achievements') else ''}"
        f"{'INNER JOIN hobbies_and_cv_link as h ON cv.id = h.cv ' if params.get('hobbies') else ''}"
        f"{'INNER JOIN driver_licenses_and_cv_link as d ON cv.id = d.cv ' if params.get('driver_licenses') else ''}"
        f"{'INNER JOIN educations_and_cv_link as e ON cv.id = e.cv ' if params.get('educations') else ''}"
        f"{'INNER JOIN employments_and_cv_link as em ON cv.id = em.cv ' if params.get('employments') else ''}"
        "INNER JOIN profiles p on cv.profile = p.id\n"
        f"{'WHERE ' if params else ''} " +
        ' and '.join(conditions) +
        " GROUP BY cv.id\n) AS T"
    )
    data = await db.all(db.text(query_text), **params)
    count = await db.scalar(db.text(count_query_text), **params)
    return limit, offset, count, data
