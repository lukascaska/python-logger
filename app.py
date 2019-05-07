import datetime, logging, sys, json_logging, flask

app = flask.Flask(__name__)
json_logging.ENABLE_JSON_LOGGING = True
json_logging.init(framework_name='flask')
json_logging.init_request_instrument(app)

# init the logger as usual
logger = logging.getLogger("test-logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

@app.route('/')
def home():
    logger.info("test log statement", extra = {'props': {'type_log': 'business'}})
    return "Hello world : " + str(datetime.datetime.now())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(8080), use_reloader=False)