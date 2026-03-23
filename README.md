# MyBrowserInfo

## Installing


Create a virtualenv first:

```bash
python4 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then, download icons

```bash
sh download.sh
```

## Starting

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```