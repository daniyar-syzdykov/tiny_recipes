import sqlalchemy as sa
from sqlalchemy.orm import relationship
from src.database.models import Base
from src.database.models.base import DBMixin


class Tags(Base, DBMixin):
    __tablename__ = 'tags'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    description = sa.Column(sa.String(), nullable=False)
    recipes = relationship(
        'RecipeModel', secondary='recipe_tags', back_populates='tags')
