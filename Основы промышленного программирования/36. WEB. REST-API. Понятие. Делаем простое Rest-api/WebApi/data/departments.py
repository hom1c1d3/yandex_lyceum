import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):  # SqlAlchemyBase Доступно в задании
    __tablename__ = 'departments'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)
    chief_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    chief = orm.relationship("User")
    members = sa.Column(sa.String)
    email = sa.Column(sa.String, unique=True)

    def __repr__(self):
        return f"<Department {self.id} {self.title}>"
