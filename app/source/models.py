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
    registered_at = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String, nullable=False)
    available_for_offers = db.Column(db.Boolean, default="false")
    date_of_birthday = db.Column(db.Date)
    sex = db.Column(db.String)
    guid = db.Column(UUID, nullable=False, unique=True)

