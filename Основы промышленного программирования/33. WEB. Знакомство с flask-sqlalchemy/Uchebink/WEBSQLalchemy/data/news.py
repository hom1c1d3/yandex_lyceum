import sqlalchemy as sa
from datetime import datetime
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class News(SqlAlchemyBase):
    __tablename__ = 'news'
    id = sa.Column(sa.Integer, primary_key=True,
                   autoincrement=True)
    title = sa.Column(sa.String, nullable=True)
    content = sa.Column(sa.String, nullable=True)
    created_date = sa.Column(sa.DateTime,
                             default=datetime.now)
    is_private = sa.Column(sa.Boolean, default=True)
    user_id = sa.Column(sa.Integer,
                        sa.ForeignKey("users.id"))
    user = orm.relation('User')

    def __repr__(self):
        return f'<News> {self.title} {self.content} {self.user}'