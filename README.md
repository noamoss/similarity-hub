# similarity-hub

## Flexible entities similarity engine for external data source.

### Building Blocks [source](https://drive.google.com/file/d/1Ny9az4KV069HtQ5flKEluE9qjzwvwnAG/view?usp=sharing):

<img src="https://raw.githubusercontent.com/noamoss/similarity-hub/main/similarity-v01.jpg" />

### Project Boards:
- [Phase 1](https://github.com/noamoss/similiarity-hub/projects/1)


### Technical Stack:
- Flask
- PostgreSQL
- React

### prerequisites
- git
- python v.3.7.2+
- pipvenv
- postgresql

### local env setup
- Create a new postgresql DB.
- `pipenv install` (in the repo's ROOT folder)
- `cp ./similarity/local_config.py.example ./similarity/local_config.py` (then set the correct configuration of your local machine).
- `cp _example.env .env`
- `bash ./initiate_local_db.sh`

### Run the server
- `pipenv run flask run` (or inside `pipenv shell`)


### Testing
- `pipenv run py.test` (or inside `pipenv shell`)
