import os
import json

allowed_devices = json.loads(os.environ.get("ALLOWED_DEVICES"))
auth_token = os.environ["AUTH_TOKEN"]
