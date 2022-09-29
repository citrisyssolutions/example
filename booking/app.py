from flask import Flask, render_template
from booking.controllers import static_blueprint, api_blueprint

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
   return f"[Error] {error.message}", 500

if __name__ == '__main__':
    app.run(debug=True)
