from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from app.store.database.models import db


class Profiles(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)


class Educations(db.Model):
    __tablename__ = 'educations'
    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String, nullable=False)
    type_of_education = db.Column(db.String, nullable=False)
    degree = db.Column(db.String)
    specialization = db.Column(db.String)
    file = db.Column(db.String)
    description = db.Column(db.String)
    finished_at = db.Column(db.Date, nullable=False)
