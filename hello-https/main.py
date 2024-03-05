# The code of a GCF triggered by HTTP
import functions_framework
@functions_framework.http
def hello_via_http(request):
    if request.args and 'name' in request.args:
        name = request.args['name']
    else:
        name = 'World'
    return 'Hello {}!'.format(name)