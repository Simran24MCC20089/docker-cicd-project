import sys
import logging
from datetime import datetime
from app.utils import get_greeting, get_system_info
from app.config import APP_VERSION

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

def main():
    logging.info("🚀 Starting CI/CD Docker App...")
    print("===========================================")
    print("   🤖 Docker CI/CD Interactive Application")
    print("===========================================")

    user = input("Enter your name: ").strip().capitalize()
    greeting = get_greeting(user)
    print(greeting)

    print("\n📅 Current System Info:")
    print(get_system_info())

    print(f"\n🔧 Application Version: {APP_VERSION}")
    print("===========================================")
    logging.info(f"Application executed successfully for user {user} at {datetime.now()}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning("Application interrupted by user.")
        sys.exit(0)
