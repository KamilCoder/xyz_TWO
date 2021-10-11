# Usage in browser

To use Fast Cezar on your browser
you should make needed steps from Run it! 
(docs - file 2_Run_it.md)

Then open your browser and type address:

### To encode your text:

##### When it's run with docker:
'''
http://0.0.0.0:8000/encoder/YOUR_TEXT
'''

##### When it's run with raw python files:

'''
http://localhost:8000/encoder/YOUR_TEXT
'''

When the address opens you will be asked 
for a login and password - You shouldn't be lying.

### Alternatively to decode your text go to:

##### For docker:

'''
http://0.0.0.0:8000/decoder/YOUR_ENCODED_TEXT
'''

##### For raw python files:

'''
http://localhost:8000/decoder/YOUR_ENCODED_TEXT
'''

You will be also asked for login and pass.

When everythink will be ok you should see your text's as JSON format.
