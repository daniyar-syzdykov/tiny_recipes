from pydantic import parse_obj_as
from fastapi import HTTPException
from src.database.schemas import RecipeSchema, RecipeCreateSchema, RecipeUpdateSchema
from src.database.models import RecipeModel, Tags


async def get_all_recipes(session):
    recipes = await RecipeModel.get_all(session=session)
    recipes = parse_obj_as(list[RecipeSchema], recipes)
    return recipes


async def get_recipe_by_id(session, recipe_id):
    recipe = await RecipeModel.get_by_id(session=session, id=recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    recipe = parse_obj_as(RecipeSchema, recipe)
    return recipe


async def recipe_create(session, recipe: RecipeCreateSchema):
    recipe = await RecipeModel.create(session=session, **recipe.dict())
    recipe = parse_obj_as(RecipeSchema, recipe)
    return recipe


async def recipe_update(session, recipe_id, recipe: RecipeUpdateSchema):
    recipe = await RecipeModel.update(session=session, id=recipe_id, **recipe.dict())
    recipe = parse_obj_as(RecipeSchema, recipe)
    return recipe


async def recipe_delete(session, recipe_id):
    try:
        recipe = await RecipeModel.delete(session=session, id=recipe_id)
    except Exception as e:
        print(e)
        return {'ok': False}
    return {'ok': True}
