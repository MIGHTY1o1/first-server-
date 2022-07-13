#importing the flask library 
from flask import Flask

#flask is the construnctor that takes the name of current mofule as in the argument 

app = Flask('shubh')
#the route() function of the flask class is a decorator
#which tells the applicaion which URL  should call the associated function 

@app.route('/')
#'/' URl is the ond with the hello world 
def hello_world():
    return 'Hello world'


@app.route('/shivam')
#'/' URl is the ond with the hello world 
def whatever_func_name():
    return {"hello": "world"}

#main driver funcrion 

app.run()