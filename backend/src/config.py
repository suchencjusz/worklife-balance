from activities.routes import router as activities_router


def import_routers(app):
    app.include_router(activities_router)