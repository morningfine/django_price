from wsgiref.simple_server import make_server


# 1、路由的分发器，负责把URL匹配到对应的数据
# 2、开发好对应的业务函数
# 3、一个请求来了之后先走路由分发器，如果找到对应的function，则执行，否则，返回404

def book(env, start_response):
    print("book page")
    start_response("200 ok", [("Content-type", "text/html;charset=utf-8")])

    return [bytes("<h1>book</h1>".encode(encoding="utf-8"))]


def cloth(env, start_response):
    print("cloth page")
    start_response("200 ok", [("Content-type", "text/html;charset=utf-8")])

    return [bytes("<h1>cloth</h1>".encode(encoding="utf-8"))]


def urls_dispatcher():
    urls = {
        "/book": book,
        "/cloth": cloth
    }
    return urls


def run_server(env, start_response):

    urls_list = urls_dispatcher()  # 拿到所有的url
    request_url = env.get("PATH_INFO")
    print(request_url)
    if request_url in urls_list:
        func = urls_list[request_url](env, start_response)
        print(func)
        return func

    else:

        start_response("200 ok", [("Content-type", "text/html;charset=utf-8")])

        return [bytes("<h1>早上好</h1>".encode(encoding="utf-8"))]


if __name__ == '__main__':
    s = make_server("localhost", 8003, run_server)
    s.serve_forever()
