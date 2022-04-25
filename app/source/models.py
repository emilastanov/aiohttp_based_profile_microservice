from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from app.store.database.models import db


class Profiles(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)


class Educations(db.Model):
    __tablename__ = 'educations'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
