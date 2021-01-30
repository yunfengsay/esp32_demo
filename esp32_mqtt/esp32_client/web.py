import picoweb
import ujson

app = picoweb.WebApp(__name__)
 
@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    print(resp)
    yield from resp.awrite(resp, content_type = "application/json")

@app.route("/exec")
def exec_code(req, resp):
    print(req.get('body'))
    print(req.get('form'))
    try:
        code = ''
        cc = compile(code, 'web_exec_temp', 'single')
        eval(cc)
    except Exception as e:
        print(e)
    yield from picoweb.start_response(resp)

app.run(debug=True, host = "0.0.0.0")

