from flask import Flask, render_template
from application.controllers import static_blueprint, api_blueprint
from application.providers.orm.sqlalchemy_orm import SQLAlchemyORM
from application.providers.db.sqlite_db_source import SQLiteDBSource
from application.providers.log.log_provider import LogProvider

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

logger = LogProvider().get_logger()
logger.info("Application started")

if __name__ == '__main__':
    app.run(debug=True)
    
