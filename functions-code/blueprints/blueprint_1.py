# Register this blueprint by adding the following line of code 
# to your entry point file.  
# app.register_functions(blueprint_1) 
# 
# Please refer to https://aka.ms/azure-functions-python-blueprints


import azure.functions as func
import logging

bp1 = func.Blueprint()


@bp1.route(route="http_trigger_1", auth_level=func.AuthLevel.FUNCTION)
def http_trigger_1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )