import sqlalchemy as sa
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    surname = sa.Column(sa.String)
    name = sa.Column(sa.String)
    age = sa.Column(sa.Integer)
    position = sa.Column(sa.String)  # должность
    speciality = sa.Column(sa.String)  # профессия
    address = sa.Column(sa.String)
    email = sa.Column(sa.String, unique=True)
    hashed_password = sa.Column(sa.String)
    modified_date = sa.Column(sa.DateTime)

    def __repr__(self):
        return f"<User {self.id} {self.name} {self.email}>"