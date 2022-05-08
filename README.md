# Selenium + CI-CD Pipeline POC #

## Usage ##

### Setup ###

```bash
python3 -m venv .venv

source .venv/bin/activate

python3 -m pip install --requirement requirements.txt
```

### Selenium Grid ###

```bash
docker-compose --file ./grid/Selenium-Grid-Recording.Yaml up
```

### Local Runtime ###

```bash
python3 -m src
```

## Teardown ##

### Selenium Grid ###

```bash
docker-compose --file ./grid/Selenium-Grid-Recording.Yaml down
```
