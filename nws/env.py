import environ

env = environ.Env()
environ.Env.read_env()


LOG_LEVEL = env.str("LOG_LEVEL", "INFO")
REDIS_SERVER = env.str("REDIS_SERVER", "")
DEBUG = env.bool("DEBUG", "")
LOG_FILE = env.str("LOG_FILE", "")
CACHE_TIMEOUT_SECONDS = env.str("CACHE_TIMEOUT_SECONDS", "")
NWS_ROOT_URL = env.str("NWS_ROOT_URL", "")
