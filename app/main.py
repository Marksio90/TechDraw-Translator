from app.logging_config import setup_logging
from ui.desktop_app import run

if __name__ == "__main__":
    setup_logging()
    raise SystemExit(run())
