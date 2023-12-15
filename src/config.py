from activities.activity_routes import router as activities_router
from activities.authentication_routes import router as authentication_routers

def import_routers(app):
    app.include_router(activities_router)
    app.include_router(authentication_routers)