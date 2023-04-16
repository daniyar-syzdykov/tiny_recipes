from fastapi import Depends
from fastapi import APIRouter
from src.database.session import get_session
from src.api.v1.schemas.request_schemas import RecipeCreateSchema, RecipeUpdateSchema
from src.api.v1.logic import get_all_recipes, get_recipe_by_id, recipe_create, recipe_update, recipe_delete

recipe_router = APIRouter(prefix="/recipes")


@recipe_router.get("/")
async def list_recipes(session=Depends(get_session)):
    recipes = await get_all_recipes(session)
    return recipes


@recipe_router.get("/{recipe_id}")
async def get_recipe(recipe_id: int, session=Depends(get_session)):
    recipe = await get_recipe_by_id(session=session, recipe_id=recipe_id)
    return recipe


@recipe_router.post("/")
async def create_recipe(body: RecipeCreateSchema, session=Depends(get_session)):
    recipe = await recipe_create(session=session, recipe=body)
    return recipe


@recipe_router.put("/{recipe_id}")
async def update_recipe(recipe_id: int, body: RecipeUpdateSchema, session=Depends(get_session)):
    recipe = await recipe_update(session=session, recipe_id=recipe_id, recipe=body)
    return recipe


@recipe_router.delete("/{recipe_id}")
async def delete_recipe(recipe_id: int, session=Depends(get_session)):
    recipe = await recipe_delete(session=session, recipe_id=recipe_id)
    return recipe
