from flask import Flask, render_template, request # import the Flask class from the flask module, render_template allows us to use HTML files, request allows us to get the data from the form
from weather import get_current_weather # import the get_current_weather function from the weather.py file
from waitress import serve # import the serve function from the waitress module


#1. Create an instance of the Flask class. This is how we create our web application.
app= Flask(__name__) # This makes you application a flask application. Use this to create a web application. Flask(__name__) is a special variable in Python that is just the name of the module.

#2. Define the route and function for the web page. Routes are the different URLs that the application implements. Each route is a different page. The function is what is executed when that route is accessed.
@app.route('/') # This will be used for the home page. The '/' is the default route. It is the main page of the website. The route is the part of the URL that comes after the domain name. The domain name is the name of the website.
# This is a decorator. It is a way to wrap a function and modify its behavior. The @app is a decorator that wraps the function below it.
# app.route is a decorator that wraps the function below it. The '/' is the path of the URL. The path is the part of the URL that comes after the domain name. The domain name is the name of the website.

@app.route('/index') # Both of these routes will go to the same page The home page. The '/' is the default route. It is the main page of the website. The route is the part of the URL that comes after the domain name. The domain name is the name of the website.

#3. Define a function for the route. This is the function that will be executed when the route is accessed. This function just returns a string. This is the response that will be sent to the client. The client is the web browser. The client sends a request to the server and the server sends a response back to the client.
def index():
    return render_template('index.html') # This will render the index.html file. The index.html file is the home page of the website. The render_template function is used to render the HTML file. The render_template function is from the flask module. The render_template function takes the name of the HTML file as an argument. The HTML file must be in the templates folder. The templates folder is in the same folder as the server.py file.

#4. Define a function for the weather route. This is the function that will be executed when the weather route is accessed. This function just returns a string. This is the response that will be sent to the client. The client is the web browser. The client sends a request to the server and the server sends a response back to the client.
@app.route('/weather')
def get_weather():
    city = request.args.get('city') # This gets the city from the URL. The city is the name of the city that the user entered in the form. The request.args.get() function gets the value of the city from the URL. The city is the name of the city that the user entered in the form.
    
    # Check for empty string or string with only spaces
    if not bool(city.strip()):
        city= "Minneapolis"
    
    weather_data = get_current_weather(city) # This gets the weather data from the get_current_weather function. The weather_data is the data that is returned from the get_current_weather function. The city is the name of the city that the user entered in the form.
    
    # city is not found by API
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')
    
    return render_template(
        'weather.html',
         title=weather_data["name"], # This gets the title from the weather_data variable. The json data is in the weather_data variable. The title is the name of the city.This is found in the "name" key in the json data.
         status=weather_data["weather"][0]["description"].capitalize(), # This gets the status from the weather_data variable. The json data is in the weather_data variable. The status is the description of the weather. This is found in the "description" key in the json data.
         temp=f"{weather_data['main']['temp']:.1f}", # This gets the temp from the weather_data variable. The json data is in the weather_data variable. The temp is the temperature. This is found in the "temp" key in the json data.
         feels_like=f"{weather_data['main']['feels_like']:.1f}" # This gets the feels_like from the weather_data variable. The json data is in the weather_data variable. The feels_like is the feels like temperature. This is found in the "feels_like" key in the json data. .1f is the format specifier. It is used to format the number to one decimal place.
    )

if __name__ == "__main__": # This is the main function. This is the entry point of the application. This is the first function that will be executed when the application is run.
    serve(app,host="0.0.0.0" , port=8000) # This will run the application on the local development server. The host is the IP address of the server. The port is the port number of th