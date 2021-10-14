# Fast Cezar - cipher API 
Cezar Cipher API based on FastAPI

----------------------------------------------

## Table of Contents

* General info
* Technologies
* Setup
* How to use / Examples


### General info

Fast Cezar use FastAPI to encode and decode your text.
The key is 5 but it's simply to change it in code,
or make it as input.
It's simply to use and working fast.
Fast Cezar to use requires authentication.

### Technologies

Fast Cezar use Python3 with FastAPI

### Setup

You can simply use:
Docker:

```
docker pull kamilcoder/fast_cezar-docker
```

or:

```
git clone https://github.com/KamilCoder/Fast_Cezar.git
```

### How to use / Examples

For example - using Fast Cezar as docker image, and curl from terminal:

```
curl -H "Content-Type: application/json" --request GET --user LOGIN:PASSWORD http://0.0.0.0:8000/encoder/dog
```

gives you response with json like:

```
cihper : itl
```

For example to decode you text using uvicorn: fast_cezar:app and browser:

```
http://localhost:8000/decoder/itl
```

gives response:

```
decoded : dog
```
