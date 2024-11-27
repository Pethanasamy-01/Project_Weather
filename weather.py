from flask import Flask,request,render_template
import requests

app=Flask(__name__)

API_KEY="    "

@app.route("/",methods=['GET','POST'])
def weather():
    weather_data=None
    if request.method=="POST":
        city=request.form['city']
        weather_data=city_info(city)
        print(weather_data)
    return render_template("weather.html",weather_data=weather_data)


def city_info(city):
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response=requests.get(url)
    if response.status_code==200:
        return response.json()
    return None

if __name__=="__main__":
    app.run(debug=True)
