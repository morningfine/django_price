from wsgiref.simple_server import make_server

def run_server(env,start_response):
    start_response()
    return []