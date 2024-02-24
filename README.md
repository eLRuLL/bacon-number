# The Bacon Number App

It can actually compute the Number between any 2 actors.

### requirements
- docker
- docker-compose

### How to use it

    docker-compose up -d
    
The previous command will generate 4 apps, the frontend, backend, nginx
and neo4j.

After that we need to populate the neo4j database, with the following steps:

- Download the movies database into `datasets/the-movies-dataset`
- Generate the people file with `python tasks/create_people.py`
- Populate the neo4j database with `python tasks/populate_neo4j.py`

The previous commands **could take several minutes**. If it fails, it is 
because the credentials and actual neo4j url is incorrectly setup (TODO).

After that's ready, you just need to go to:

    http://127.0.0.1
    
And the app will be available. Enjoy.