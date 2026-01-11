import azure.functions as func
import logging

import blueprints

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# Registering all the blueprints

for bp in blueprints.__all__:
    app.register_functions(bp)





