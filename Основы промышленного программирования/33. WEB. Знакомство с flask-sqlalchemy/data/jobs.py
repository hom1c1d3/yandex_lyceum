import sqlalchemy as sa
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):  # SqlAlchemyBase Доступно в задании
    __tablename__ = 'jobs'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    team_leader = sa.Column(sa.Integer, sa.ForeignKey('users.id'))  # id лидера
    job = sa.Column(sa.Text)  # описание
    work_size = sa.Column(sa.Integer)  # в часах
    collaborators = sa.Column(sa.String)  # список id
    start_date = sa.Column(sa.Date)
    send_date = sa.Column(sa.Date)

    def __repr__(self):
        return f"<Jobs {self.id} {self.name} {self.email}>"
