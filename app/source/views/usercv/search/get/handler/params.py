

async def make_conditions(request):
    skills = request.query.get('skills')
    hobbies = request.query.get('hobbies')
    salary = request.query.get('salary')
    wish_position = request.query.get('wish_position')
    driver_license = request.query.get('driver_licenses')
    achievements = request.query.get('achievements')
    educations = request.query.get('educations')
    military_duty = request.query.get('military_duty')
    possibility_of_moving = request.query.get('possibility_of_moving')
    work_format = request.query.get('work_format')
    marital_status = request.query.get('marital_status')
    employments = request.query.get('employments')

    conditions = {}

    if skills:
        conditions['skills'] = list(map(int, skills.split(',')))
    if hobbies:
        conditions['hobbies'] = list(map(int, hobbies.split(',')))
    if driver_license:
        conditions['driver_license'] = list(map(int, driver_license.split(',')))
    if achievements:
        conditions['achievements'] = list(map(int, achievements.split(',')))
    if educations:
        conditions['educations'] = list(map(int, educations.split(',')))
    if employments:
        conditions['employments'] = list(map(int, employments.split(',')))
    if salary:
        conditions['salary'] = salary
    if wish_position:
        conditions['wish_position'] = wish_position
    if military_duty:
        conditions['military_duty'] = military_duty
    if possibility_of_moving:
        conditions['possibility_of_moving'] = possibility_of_moving
    if work_format:
        conditions['work_format'] = work_format
    if marital_status:
        conditions['marital_status'] = marital_status

    return conditions
