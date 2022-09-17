from flask import Flask,render_template
from booking.routes import static_blueprint, api_blueprint

app = Flask(__name__)
app.register_blueprint(
    static_blueprint,
    url_prefix="/",
)

app.register_blueprint(
    api_blueprint,
    url_prefix="/api"
)


if __name__ == '__main__':
 app.run(debug=True)

