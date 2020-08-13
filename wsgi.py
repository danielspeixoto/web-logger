import os

from app.main import app

if __name__ == "__main__":
    port = os.getenv('PORT')
    if port is None:
        port = 5000
    app.run(host="0.0.0.0", port=port)
