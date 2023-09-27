# National weather service API - V1

## Description

This repository contains a JSON web API that returns the latest weather info given a specific US station code. The data is cached in Redis for 5 minutes, but can be refreshed by passing the nocache=1 parameter.

## Upcoming in V2

This is a v1 project which was developed based on an assignment. The architecture, implementation, and API structure were all created to match those requirements. However, a v2 project with an advanced UI and conventional standard REST APIs is in development.

### Whats upcoming

* Advanced UI.
* Update the API to use conventional standard REST APIs.
* Add additional features and functionality to the API.
* Generalised caching mechanism. 
* Test cases

## Repository

The main branch is master branch. Always start a branch from here.

## System Requirements

1. Docker
2. Docker compose

## Setup

1. Clone this repository.
2. Build using docker command:

```
docker-compose up --build
```

The API will be running at port 8000.


## API Reference

#### Liveness API

```http
  GET /metar/ping
```


#### Get weather information for the given station code.

```http
  GET /metar/info?scode=<station_code>&no-cache=<cache_flag>
```

| Parameter       | Type     | Description                       |
| :-------------- | :------- | :-------------------------------- |
| `station_code`  | `string` | **Required**. US Station code. Eg: KSGS |
| `cache_flag`    | `integer`| Setting this query parameter to 1 will return the live data instead of the cached data |


## Example

To get weather information for the station code KSGS, you would send a GET request to the following URL:

```
http://localhost:8000/metar/info?scode=KSGS
```

The response would be a JSON object with the following structure:

```
{
  "message": "success",
  "data": {
    "last_observation": "2023/09/26 21:00GMT",
    "station": "TKPN",
    "temperature": "23 C (73.4 F)",
    "wind": "011 at 12.6585734 mph (11 knots)"
  }
}
```

## Assumptions

1. The METAR API is reliable and always returns valid data.
2. The Redis server is running and accessible.
3. Docker Compose file

## Authors

- [@jeessonjohney](https://github.com/jeessonjohney)
## License

[GNU general public license](https://www.gnu.org/licenses/gpl-3.0.en.html)


