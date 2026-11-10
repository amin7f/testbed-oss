import os

APP_NAME = "security-testbed"
APP_VERSION = "1.0.0"
LOG_LEVEL = "INFO"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "testbed.db")
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")

# ID: S-01
GITHUB_TOKEN = "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"
GITHUB_ORG = "testbed-org"
REQUEST_TIMEOUT = 5
MAX_UPLOAD_MB = 10
DEFAULT_LANGUAGE = "de"
PAGE_SIZE = 20
CACHE_TTL_SECONDS = 300

# ID: S-02
AWS_ACCESS_KEY_ID = "AKIAK3QCPSUQOQNB5K3R"
AWS_SECRET_ACCESS_KEY = "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"
AWS_REGION = "eu-central-1"
AWS_BUCKET = "testbed-exports"
EXPORT_FORMAT = "csv"
EXPORT_BATCH_SIZE = 500
ENABLE_METRICS = True

# ID: S-03
DB_PASSWORD = "e9rNJw43LloV+D6JF7%Q"
DB_USER = "testbed"
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "testbed"
DB_POOL_SIZE = 5
DB_TIMEOUT_SECONDS = 10

# ID: S-07
SMTP_PASSWORD = "CHANGE_ME"
SMTP_USER = "noreply"
SMTP_HOST = "mail.example.org"
SMTP_PORT = 587
SMTP_USE_TLS = True
MAIL_SENDER = "noreply@example.org"
MAIL_SUBJECT_PREFIX = "[testbed]"

# ID: S-08
SERVICE_TOKEN = os.environ.get("SERVICE_TOKEN", "")
SERVICE_URL = "https://service.example.org/api"
SERVICE_RETRIES = 3
FEATURE_EXPORT = True
FEATURE_PREVIEW = True
FEATURE_TOOLS = True
TIMEZONE = "Europe/Berlin"
