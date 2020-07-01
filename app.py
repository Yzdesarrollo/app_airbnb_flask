from flask import Flask, render_template, request, redirect, url_for
import requests as req
import random

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
    res = req.post('http://localhost:3000/api/addproperty', json = addData)
    return redirect(url_for('listPropertyuser'))

@app.route('/listproperties')
def listProperty():
    response = req.get('http://localhost:3000/api/listproperties')
    result = response.json()['res']['data']
    # img = ['casa1', 'casa2', 'casa3', 'casa4', 'casa5']
    # aleatorio = random.choice(img)
    # print(aleatorio)
    return render_template('list-properties.html', properties = result)

@app.route('/listpropertyuser')
def listPropertyuser():
    response = req.get('http://localhost:3000/api/listproperties')
    result = response.json()['res']['data']
    # img = ['casa1', 'casa2', 'casa3', 'casa4', 'casa5']
    # aleatorio = random.choice(img)
    # print(aleatorio)
    return render_template('list-properties-user.html', properties = result)

@app.route('/editproperty')
def editProperty():
    id = request.args.get('id')
    response = req.get(f'http://localhost:3000/api/getproperties?id={id}')
    result = response.json()['res']['data'][0]
    print('result => ', result)
    return render_template('update-property.html', pro = result)

@app.route('/updateproperty', methods = ['POST'])
def updateProperty():
    id = request.args.get('id')
    title = request.form['title']
    tp = request.form['type']
    address = request.form['address']
    rooms = request.form['rooms']
    price = request.form['price']
    area = request.form['area']
    image = request.form['image']
    author = request.form['author']
    addData = {"id":id, "title":title, "type": tp, "address":address, "rooms":rooms,"price":price, "area":area, "image":image, "author":author}
    print('addData =>',addData)
    res = req.put('http://localhost:3000/api/updateproperty', json = addData)
    return redirect(url_for('listPropertyuser'))

@app.route('/deleteproperty')
def deleteProperty():
    id = request.args.get('id')
    deleteData = {'id':id}
    response = req.delete(f'http://localhost:3000/api/deleteproperty?id={id}', json = deleteData)
    return redirect(url_for('listPropertyuser'))

if __name__ == '__main__':
    app.run(debug=True)

