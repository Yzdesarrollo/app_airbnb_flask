from flask import Flask, render_template, request, redirect, url_for
import requests as req

app = Flask (__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signin')
def signin():
    return render_template('sign-in.html')

@app.route('/signup')
def signup():
    return render_template('sign-up.html')

@app.route('/registerProperty')
def registerProperty():
    return render_template('add-property.html')

@app.route('/adduser', methods = ['POST'])
def addUser():
    name = request.form['name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    addData = {"name":name, "last_name": last_name, "email":email, "password":password}
    # print(addData)
    res = req.post('http://localhost:3000/api/adduser', json = addData)
    return redirect(url_for('registerProperty'))

@app.route('/addproperty', methods = ['POST'])
def addProperty():
    title = request.form['title']
    tp = request.form['type']
    address = request.form['address']
    rooms = request.form['rooms']
    price = request.form['price']
    area = request.form['area']
    image = request.form['image']
    author = request.form['author']
    addData = {"title":title, "type": tp, "address":address, "rooms":rooms,"price":price,"area":area,"image":image,"author":author}
    # print(addData)
    res = req.post('http://localhost:3000/api/addproperty', json = addData)
    # print('res =>',res )
    return redirect(url_for('listProperty'))

@app.route('/listproperties')
def listProperty():
    response = req.get('http://localhost:3000/api/listproperties')
    # print(response.json()['res']['data'])
    result = response.json()['res']['data']
    return render_template('list-properties.html', properties = result)

@app.route('/updateproperty')
def updateProperty():
    # response = req.put('http://localhost:3000/api/updateproperty')
    # print(response.json()['res']['data'])
    # # result = response.json()['res']['data']
    # # print('result => ', result)
    return render_template('update-property.html')

if __name__ == '__main__':
    app.run(debug=True)

