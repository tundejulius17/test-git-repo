import azure.functions as func
import logging

from blueprints import __all__

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# Registering all the blueprints
import blueprints
for blueprint_name in blueprints.__all__:
    blueprint = getattr(blueprints, blueprint_name)
    app.register_functions(blueprint)

