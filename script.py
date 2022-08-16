import os
import argparse
from bot import handshake


parser = argparse.ArgumentParser()
parser.add_argument(
    "-u", "--username", type=str, help="Username (uses default credentials otherwise)"
)
parser.add_argument(
    "-p", "--password", type=str, help="Password (uses default credentials otherwise)"
)
parser.add_argument("-q", "--query", type=str, help="Job search query", required=True)
parser.add_argument(
    "--headless",
    action="store_true",
    default=False,
    help="Run headless (runs w/ head by default)",
)
args = parser.parse_args()

username = args.username
password = args.password

# Get username and password from environment if not provided
if username is None and password is None:
    username = os.environ.get("BYU_USERNAME")
    password = os.environ.get("BYU_PASSWORD")

handshake(username, password, args.query, args.headless)
