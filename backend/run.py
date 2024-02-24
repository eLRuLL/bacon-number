import os

from src import create_app


os.environ.setdefault('FLASK_APP', 'src')
app = create_app()
app.run(debug=True, host='0.0.0.0')
