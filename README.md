**Activate the virtual environment**

```
source env/scripts/activate
```

**Install all packages**

```
pip install -r requirements.txt
```

**Run the tests**

Make sure to activate activate virtualenv by following line 4.

```
python -m pytest backend/tests
```

**Run the application and API**

Make sure to activate activate virtualenv by following line 4.

```
python -m backend.app
```

**Run a peer instance**

Make sure to activate activate virtualenv by following line 4.

```
export PEER = True && python -m backend
```
**Run the frontend**

In the frontend directory

```
npm run start
```

**Seed the backend with data**

Make sure to activate activate virtualenv by following line 4.

```
export SEED_DATA=True && python -m backend.app
```
