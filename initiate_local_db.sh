# Configuration as in `local_config.py`.
# Assuming that on local machine, user/pass/db are the same string.
PROJECT_NAME='similarity'

# Colors.
RESET_COLORS='\033[00m'
BLUE='\033[34m'

echo
echo
echo -e "${BLUE}  >  Creating Database... ${RESET_COLORS}"

psql -U postgres -c "CREATE ROLE ${PROJECT_NAME} PASSWORD '${PROJECT_NAME}' SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;"
psql -U postgres -c "CREATE DATABASE ${PROJECT_NAME} OWNER ${PROJECT_NAME};"


pipenv run flask db migrate
pipenv run flask create-db
