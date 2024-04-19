import os
import loguru


ENVIRONMENT = os.environ.get('ENVIRONMENT', False)
LOGGER = loguru.logger
if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    OWNER_ID = os.environ.get('OWNER_ID', 6258709129)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = "22556030"
    OWNER_ID = 5837099475
    API_HASH = "9f445a41203dc7d430f7c4f880e96c8a"
    BOT_TOKEN = "6389119744:AAHnk-1s4jecRD0LrPxZW3kUN9pXRPwa5sI"
    DATABASE_URL = "postgres://kjirmkdwfojicj:0098039db39a3ca99144622cd18e4b6bd15b5cefe6102021192560d7a0cea764@ec2-46-137-0-50.eu-west-1.compute.amazonaws.com:5432/dcsito1dmgpt2e"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "-1001779717901"
