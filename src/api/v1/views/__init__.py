from fastapi import APIRouter

from src.api.v1.views.recipe_vews import recipe_router

main_router = APIRouter(prefix='/api/v1')
main_router.include_router(recipe_router)
