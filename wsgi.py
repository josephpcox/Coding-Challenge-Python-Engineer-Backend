import sys
import os

if __name__ == "__main__":
    from app.server import create_app
    app = create_app(config_name="local")
    app.run(host="0.0.0.0",port=5000, debug=True)
