# similarity-hub

## Flexible entities similarity engine for external data source.

### Building Blocks [source](https://drive.google.com/file/d/1Ny9az4KV069HtQ5flKEluE9qjzwvwnAG/view?usp=sharing):

<img src="https://raw.githubusercontent.com/noamoss/similarity-hub/main/similarity-v01.jpg" />

### Project Boards:
- [Phase 1](https://github.com/noamoss/similiarity-hub/projects/1)


### Technical Stack:
- Django
- PostgreSQL
- React

### prerequisites
- git
- python v.3.7.2+
- pipvenv
- postgresql

### local env setup
- Create a new postgresql DB.

  For example:
  ```bash
  psql -U postgres -c "CREATE ROLE similarity_hub PASSWORD 'similarity_hub' SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;"
  psql -U postgres -c "CREATE DATABASE similarity_hub OWNER similarity_hub;"
  ```
- `pipenv install` (in the repo's ROOT folder)
- `cp similarity_hub/local_settings.py.example local_settings.py` (then set the correct settings for your local machine).
- `cp _example.env .env` (if preferable than local settings)
  - Note: Be aware that local settings will override any other settings defined in `.env`.
- `pipenv run python manage.py migrate` (or inside `pipenv shell`)

### Run the server
- `pipenv run python manage.py runserver` (or inside `pipenv shell`)


### Testing
- `pipenv run python manage.py test` (or inside `pipenv shell`)
