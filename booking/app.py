import os
from flask import Flask, render_template
from flask import send_from_directory
from controllers import static_blueprint, api_blueprint

app = Flask(__name__)
app.register_blueprint(
    static_blueprint,
    url_prefix="/",
)

app.register_blueprint(
    api_blueprint,
    url_prefix="/api"
)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# @app.errorhandler(Exception)
# def all_exception_handler(error):
#     try:
#         return f"[Error] {error.message}", 500
#     except:
#          return "unkown error"
        
       
if __name__ == '__main__':
    app.run(debug=True)
