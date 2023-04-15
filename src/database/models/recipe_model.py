import sqlalchemy as sa
from src.database.models import Base
from sqlalchemy.orm import relationship
from src.database.models.base import DBMixin


class RecipeModel(Base, DBMixin):
    __talbename__ = 'recipes'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    description = sa.Column(sa.String(), nullable=False)
    tags = relationship('Tags', secondary='recipe_tags',
                        back_populates='recipes')
