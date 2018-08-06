# muninn
  Free api for getting information about computer games.

# env variables:
  export MUNINN_SETTINGS_ENV='development' for dev env

  export MUNINN_SETTINGS_ENV='production' for prod env

# Dependencies
  Check requirements.txt for details

  install dependcies : pip instatl requirements.txt

# End points (only get)
  All queries and url params are case insensitive except for get game by name endpoint.
  The search endpoints are all case insensitive and can match, so you dont need to provide entire word.

  ## Games

    * /api/v1/games/all - get all games

    can also be paginated and page size changed:
    * /api/v1/games/all/?page={page_num}&page_size={page_size}

    * /api/v1/games/?search={query} - returns a search result done by query which can be name,
    developer name, engine name, publisher name, series, genre, can also be paginated

    * /api/v1/games/?series={series name} - returns games by series, can be paginated

    * /api/v1/games/?genre={genre} - returns games by genre, can be paginated

    * /api/v1/games/?developer={developer name} returns games by developer, can be paginated

    * /api/v1/games/?engine={engine name} returns games by engine, can be paginated

    * /api/v1/games/?pulisher={publisher name} returns games by publisher, can be paginated

    * /api/v1/games/{game name} - returns a game if found
  
  ## Engines

    * /api/v1/engines/all - returns all games, can also be paginated
    
    * /api/v1/engines/?search={query} - returns a search by query which can be name,
    developer name, can be paginated

    * /api/v1/engines/?developer={name} - returns engines created by developers, can be paginated

    * /api/v1/engines/?name={name} - returns engine by name

  ## Developer

    * /api/v1/developers/all returns all developers, can be paginated

    * /api/v1/developers/?search={query} - returns search done by query, can be name, status, industry,
    can be paginated

    * /api/v1/developers/?status={status} - returns developers by status, can be active, unknown, defunct,
    can be paginated

    * /api/v1/developers/?industry={industry} - returns developers by industry, can be paginated

    * /api/v1/developers/?name={name} - returns developer by name

  ## Publisher

    * /api/v1/publishers/all - returns all publishers, can be paginated

    * /api/v1/publisher/?search={query} - returns publishers by query, can be paginated and the query can be,
    name,status

    * /api/v1/publishers/?status={status} - returns publishers by status, can be paginated, status can be active, defunctm unknown

    * /api/v1/publishers/?name={name} - returns publisher by name



# Run tests

python3 manage.py test

coverage: coverage run --source='.' manage.py test api
report: coverage report