from pydantic import BaseModel


class RecipeCreateSchema(BaseModel):
    name: str
    description: str | None
    ingredients: str | None
    instructions: str | None

class RecipeUpdateSchema(BaseModel):
    name: str | None
    description: str | None
    ingredients: str | None
    instructions: str | None