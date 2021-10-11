# Run it!

To run Fast Cezar you can download
docker image or python raw files.

### Run from docker image

To run Fast Cezar from docker image,
you must pull image by tapping in terminal:

'''
docker pull kamilcoder/fast_cezar-docker
'''

then simply run it by:

'''
docker run -p 8000:8000 kamilcoder/fast_cezar-docker
'''

You should be now able to connect to the application
by browser or simply by curl at: https://0.0.0.0:8000/

To use it, You will need login and password.
Do not tell it any one, but login is admin and pass is admin...

### Run from Python raw files

To run Fast Cezar from raw files
of corse you need Python. 
You should know that there is some other
stuff that you will need...
Open your terminal and let your keyboard fire!


'''
pip3 install fastapi
pip3 install uvicorn
'''

next download files from github:

'''
git clone https://github.com/KamilCoder/xyz_TWO/
'''

then go inside xyz_TWO directory like this:

'''
cd xyz_TWO
'''

and run app like this:

'''
uvicorn fast_cezar:app
'''

Go! Boom! Here you have! 
Now your Fast Cezar is running at http://localhost:8000/
