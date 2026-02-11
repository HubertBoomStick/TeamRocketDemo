# Team Rocket Project


This is Rocket Project!

installation!
```
sudo apt update
sudo apt install -y \
  git \
  python3 \
  python3-pip \
  python3-venv \
  build-essential \
  curl
```

Create a Python virtual environment and activate it
```
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies
```
pip install --upgrade pip
pip install fastapi "uvicorn[standard]"
```

Run the server
```
uvicorn main:app --reload
```

--------------------------------------------------------------
Fix the problem
```
sudo apt update
sudo apt install -y python3-venv python3-pip
```

Reactivate
```
python3 -m venv .venv
source .venv/bin/activate
```

Now run this
```
python -m pip install --upgrade pip
python -m pip install fastapi "uvicorn[standard]"
```
