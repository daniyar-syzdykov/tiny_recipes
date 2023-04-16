import sqlalchemy as sa
from sqlalchemy.orm import relationship
from src.database.models.base import Base, DBMixin


class RecipeModel(Base, DBMixin):
    __tablename__ = 'recipes'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    description = sa.Column(sa.String(), nullable=True)
    ingredients = sa.Column(sa.String(), nullable=True)
    instructions = sa.Column(sa.String(), nullable=True)
    tags = relationship('Tags', secondary='recipe_tags',
                        back_populates='recipes')


class RecipeTags(Base, DBMixin):
    __tablename__ = 'recipe_tags'

    id = sa.Column(sa.Integer, primary_key=True)
    recipe_id = sa.Column(sa.Integer, sa.ForeignKey('recipes.id'))
    tag_id = sa.Column(sa.Integer, sa.ForeignKey('tags.id'))
    # recipe = relationship('RecipeModel', back_populates='tags')
    # tag = relationship('Tags', back_populates='recipes')