# retool-pokedex

REST API to support list, create, and delete operations for a Pokemon list for a [simple Retool project](https://garrettedel.retool.com/apps/pokemon).

## Endpoints

`pokemon/`
- `GET` list of Pokemon in the database
- Example response:
```
{
  'name': 'Wartortle',
  'pokeapi_url': 'http://wartorle.com',
  'date_added': '2020-02-09'
}
```

`pokemon/{pokemon-name}`: `DELETE` single Pokemon from the database
