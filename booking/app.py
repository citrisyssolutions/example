from flask import Flask, render_template
from controllers import static_blueprint, api_blueprint
from exception.errors import  ValidationError
app = Flask(__name__)
app.register_blueprint(
    static_blueprint,
    url_prefix="/",
)

app.register_blueprint(
    api_blueprint,
    url_prefix="/api"
)

@app.errorhandler(Exception)
def all_exception_handler(error):
    try:
        return f"[Error] {error.message}", 500
    except:
         return "unkown error"
        
       
if __name__ == '__main__':
    app.run(debug=True)
