from sqlalchemy.dialects.postgresql import UUID

from app.store.database.models import db


class Files(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime)
    description = db.Column(db.String)


class Skills(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    meta_title = db.Column(db.String, nullable=False)
    course_id = db.Column(db.Integer)


class Profiles(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    middle_name = db.Column(db.String, nullable=False)
    registered_at = db.Column(db.DateTime)
    location = db.Column(db.String, nullable=False)
    available_for_offers = db.Column(db.Boolean, default="false")
    date_of_birthday = db.Column(db.Date)
    sex = db.Column(db.String)
    guid = db.Column(UUID, nullable=False, unique=True)


class UserCv(db.Model):
    __tablename__ = 'user_cv'
    id = db.Column(db.Integer, primary_key=True)
    about_me = db.Column(db.String)
    employments = db.Column(db.String,  default="full")
    avatar = db.Column(db.Integer, db.ForeignKey('files.id', ondelete='CASCADE'))
    wish_position = db.Column(db.String)
    possibility_of_moving = db.Column(db.Boolean, default="false")
    military_duty = db.Column(db.String)
    work_format = db.Column(db.String)
    wish_salary = db.Column(db.Integer)
    marital_status = db.Column(db.String)
    profile = db.Column(db.Integer, db.ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False)


class Achievements(db.Model):
    __tablename__ = 'achievements'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    file = db.Column(db.Integer, db.ForeignKey('files.id', ondelete='CASCADE'))


class DriverLicense(db.Model):
    __tablename__ = 'driver_license'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)


class Hobbies(db.Model):
    __tablename__ = 'hobbies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)


class Educations(db.Model):
    __tablename__ = 'educations'
    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String, nullable=False)
    type_of_education = db.Column(db.String, nullable=False)
    degree = db.Column(db.String)
    specialization = db.Column(db.String)
    file = db.Column(db.Integer, db.ForeignKey('files.id', ondelete='CASCADE'))
    description = db.Column(db.String)
    finished_at = db.Column(db.Date, nullable=False)


class AchievementsAndCvLink(db.Model):
    __tablename__ = 'achievements_and_cv_link'
    id = db.Column(db.Integer, primary_key=True)
    achievement = db.Column(db.Integer, db.ForeignKey('achievements.id', ondelete='CASCADE'), nullable=False)
    cv = db.Column(db.Integer, db.ForeignKey('user_cv.id', ondelete='CASCADE'), nullable=False)


class EducationsAndCvLink(db.Model):
    __tablename__ = 'educations_and_cv_link'
    id = db.Column(db.Integer, primary_key=True)
    education = db.Column(db.Integer, db.ForeignKey('educations.id', ondelete='CASCADE'), nullable=False)
    cv = db.Column(db.Integer, db.ForeignKey('user_cv.id', ondelete='CASCADE'), nullable=False)


class DriverLicensesAndCvLink(db.Model):
    __tablename__ = 'driver_licenses_and_cv_link'
    id = db.Column(db.Integer, primary_key=True)
    driver_license = db.Column(db.Integer, db.ForeignKey('driver_license.id', ondelete='CASCADE'), nullable=False)
    cv = db.Column(db.Integer, db.ForeignKey('user_cv.id', ondelete='CASCADE'), nullable=False)


class SkillsAndCvLink(db.Model):
    __tablename__ = 'skills_and_cv_link'
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.Integer, db.ForeignKey('skills.id', ondelete='CASCADE'), nullable=False)
    cv = db.Column(db.Integer, db.ForeignKey('user_cv.id', ondelete='CASCADE'), nullable=False)


class HobbiesAndCvLink(db.Model):
    __tablename__ = 'hobbies_and_cv_link'
    id = db.Column(db.Integer, primary_key=True)
    hobby = db.Column(db.Integer, db.ForeignKey('hobbies.id', ondelete='CASCADE'), nullable=False)
    cv = db.Column(db.Integer, db.ForeignKey('user_cv.id', ondelete='CASCADE'), nullable=False)


class Employments(db.Model):
    __tablename__ = 'employments'
    id = db.Column(db.Integer, primary_key=True)
    started_at = db.Column(db.Date, nullable=False)
    finished_at = db.Column(db.Date)
    until_now = db.Column(db.Boolean, default='false')
    title = db.Column(db.String, nullable=False)
    region = db.Column(db.String)
    position = db.Column(db.String, nullable=False)
    specialization_of_company = db.Column(db.String, nullable=False)
    web_site = db.Column(db.String)
    description = db.Column(db.String, nullable=False)
    reason_for_dismissal = db.Column(db.String)


class EmploymentsAndCvLink(db.Model):
    __tablename__ = 'employments_and_cv_link'
    id = db.Column(db.Integer, primary_key=True)
    employment = db.Column(db.Integer, db.ForeignKey('employments.id', ondelete='CASCADE'), nullable=False)
    cv = db.Column(db.Integer, db.ForeignKey('user_cv.id', ondelete='CASCADE'), nullable=False)
