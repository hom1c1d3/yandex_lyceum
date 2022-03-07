import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase

association_table = sa.Table("jobs_to_categories", SqlAlchemyBase.metadata,
                             sa.Column("job_id", sa.Integer, sa.ForeignKey("jobs.id")),
                             sa.Column("category.id", sa.Integer, sa.ForeignKey("categories.id")))


class Category(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "categories"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)


class Jobs(SqlAlchemyBase, SerializerMixin):  # SqlAlchemyBase Доступно в задании
    __tablename__ = 'jobs'

    serialize_rules = ("-team_leader", "-categories.jobs")

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    team_leader_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))  # id лидера
    team_leader = orm.relationship("User")
    job = sa.Column(sa.Text)  # описание
    work_size = sa.Column(sa.Integer)  # в часах
    collaborators = sa.Column(sa.String)  # список id
    start_date = sa.Column(sa.Date)
    end_date = sa.Column(sa.Date)
    categories = orm.relationship("Category", secondary=association_table, backref="jobs")
    is_finished = sa.Column(sa.Boolean, default=False)

    def __repr__(self):
        return f"<Jobs {self.id} {self.job} {self.is_finished}>"
