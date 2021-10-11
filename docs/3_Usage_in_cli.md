# Usage in cli

To use Fast Cezar on CLI go to 
second part of docs named 2_Run_it.md 
and make all needed steps from this file.

Now when your server will run just: 

### To encode your text:

type on terminal:

##### When it's run with docker:

```
curl -H "Content-Type: application/json" --request GET --user LOGIN:PASSWORD http://0.0.0.0:8000/encoder/YOUR_TEXT
```

##### When it's run with raw python files:

```
curl -H "Content-Type: application/json" --request GET --user LOGIN:PASSWORD http://localhost:8000/encoder/YOUR_TEXT
```

### To decode your text:

##### When it's run with docker:

```
curl -H "Content-Type: application/json" --request GET --user LOGIN:PASSWORD http://0.0.0.0:8000/decoder/YOUR_ENCODED_TEXT
```

##### When it's run with raw python files:

```
curl -H "Content-Type: application/json" --request GET --user LOGIN:PASSWORD http://localhost:8000/decoder/YOUR_ENCODED_TEXT
```

Enjoy!!
