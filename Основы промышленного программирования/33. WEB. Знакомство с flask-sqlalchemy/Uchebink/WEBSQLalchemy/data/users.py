import sqlalchemy as sa
from datetime import datetime
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    about = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, nullable=True, unique=True, index=True)
    hashed_password = sa.Column(sa.String, nullable=True)
    create_date = sa.Column(sa.DateTime, default=datetime.now)
    news = orm.relation('News', back_populates="user")

    def __repr__(self):
        return f"<User {self.id} {self.name} {self.email}>"