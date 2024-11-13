import sqlalchemy as sa
import sqlalchemy.orm as so
from app import create_app, db
from app.models import user_credentials, pestisafe_data, pestisafe_result

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        "sa": sa,
        "so": so,
        "db": db,
        "user_credentials": user_credentials,
        "pestisafe_data": pestisafe_data,
        "pestisafe_result": pestisafe_result,
    }
