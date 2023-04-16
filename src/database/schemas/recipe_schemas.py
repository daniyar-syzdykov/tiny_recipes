from pydantic import BaseModel


class RecipeSchema(BaseModel):
    name: str
    description: str
    ingredients: str
    instructions: str

    class Config:
        orm_mode = True


class RecipeCreateSchema(RecipeSchema):
    name: str
    description: str | None
    ingredients: str | None
    instructions: str | None


class RecipeUpdateSchema(RecipeSchema):
    name: str | None
    description: str | None
    ingredients: str | None
    instructions: str | None
