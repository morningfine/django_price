from wsgiref.simple_server import make_server


def run_server(env, start_response):
    print("hhhhh", env, start_response)
    start_response("200 ok", [("Content-Type", "text/html;charset=utf-8")])
    return [bytes('你好，世界', encoding="utf-8")]


s = make_server("10.0.108.27", 8003, run_server)
s.serve_forever()
