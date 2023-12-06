from app.router import app
import os

app.secret_key = os.urandom(24)

app.run(debug=True, host='0.0.0.0', port=8000)