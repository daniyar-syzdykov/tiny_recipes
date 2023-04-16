from sqlalchemy.orm import declarative_base

Base = declarative_base()


from .recipe_model import RecipeModel
from .tags_model import Tags