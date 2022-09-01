import functions_framework

from .src import MyLibrary


@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = f"get_json = {request_json['name']}"
    elif request_args and 'name' in request_args:
        name = f"args = {request_args['name']}"
    else:
        name = 'World'
    return f'{name}. v2 {MyLibrary.get_project_name()}'
