# MySQL Docker
    ( unsecure version , crypto tests)

## Docker image
The latest from docker hub

## Running

    '''
    docker-compose up
       or
    docker-compose down
    '''
## Test

    '''
    mysql -h 0.0.0.0 -u root -p -e "SELECT version()"
       or
    ./test.test.sh
    '''

## Python test

    '''
    python ./app/app.y
    '''
## DB by default:

    '''
    ./db/user.sql
    '''

## Manual access:
    '''
    mysql> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | mysql              |
    | performance_schema |
    | sys                |
    +--------------------+
    4 rows in set (0.01 sec)
    
    
    mysql> select version();
    +-----------+
    | version() |
    +-----------+
    | 8.0.27    |
    +-----------+
    1 row in set (0.00 sec)
    
    mysql> 
     '''