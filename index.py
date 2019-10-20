from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json


with open('config.json', 'r') as c:
    params = json.load(c)['params']

local_server = True
app = Flask(__name__)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_url']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_url']

db = SQLAlchemy(app)

#Class for Insert Data in Database Book Issued: HQ to Circle
class Bookhqtocircle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    officerbeltno = db.Column(db.String(80), nullable=False)
    rank = db.Column(db.String(80), nullable=False)
    officername = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    diaryno = db.Column(db.String(80), nullable=False)
    circle = db.Column(db.String(80), nullable=False)
    serialfrom = db.Column(db.String(80), nullable=False)
    serialto = db.Column(db.String(120), nullable=False)
    #slug = db.Column(db.String(25), nullable=False)

##### Class Seperation ####

#Class for Insert Data in Database Book Issued: Circle to Sector
class Bookcircletosector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    officerbeltno = db.Column(db.String(80), nullable=False)
    rank = db.Column(db.String(80), nullable=False)
    officername = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    sector = db.Column(db.String(80), nullable=False)
    serialfrom = db.Column(db.String(80), nullable=False)
    serialto = db.Column(db.String(120), nullable=False)

##### Class Seperation ####

#Class for Insert Data in Database Book Issued: Sector to Officer
class Booksectortoofficer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    officerbeltno = db.Column(db.String(100), nullable=False)
    rank = db.Column(db.String(100), nullable=False)
    officername = db.Column(db.String(100), nullable=False)
    bookno = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)

##### Class Seperation ####

#Class for Insert Data in Database Entry: Ticket Information
class Entryticketinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    officerbeltno = db.Column(db.String(80), nullable=False)
    rank = db.Column(db.String(80), nullable=False)
    officername = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    diaryno = db.Column(db.String(80), nullable=False)
    circle = db.Column(db.String(80), nullable=False)
    serialfrom = db.Column(db.String(80), nullable=False)
    serialto = db.Column(db.String(120), nullable=False)

##### Class Seperation ####

#Class for Insert Data in Database Entry: Ticket Information
class Entrystatementregister(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    officerbeltno = db.Column(db.String(80), nullable=False)
    rank = db.Column(db.String(80), nullable=False)
    officername = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    diaryno = db.Column(db.String(80), nullable=False)
    circle = db.Column(db.String(80), nullable=False)
    serialfrom = db.Column(db.String(80), nullable=False)
    serialto = db.Column(db.String(120), nullable=False)

##### Class Seperation ####


# All App Routes
#Home Page Route
@app.route('/')
def home():
    pageTitle="Challan Information & Management System"
    return render_template('index.html', pageTitle=pageTitle)

# Book Issued: HQ 2 Circle Route
# Input Form: HQ 2 Circle
@app.route('/bookHQ2Circle', methods=['GET', 'POST'])
def bookhq2ircle():
    pageTitle = "Book Issued: HQ to Circle"
    return render_template('bookHQ2Circle.html', pageTitle=pageTitle)

# Data Saved Entry: HQ 2 Circle
@app.route('/HQ2CircleSuccess', methods=['GET', 'POST'])
def bookhq2circlesuccess():
    if(request.method=='POST'):
        '''Add Entry to the Database'''
        beltno= request.form.get('officerbeltno')
        rank = request.form.get('rank')
        officername = request.form.get('officername')
        date = request.form.get('date')
        diaryno = request.form.get('diaryno')
        circle = request.form.get('circle')
        serialfrom = request.form.get('serialfrom')
        serialto = request.form.get('serialto')
        # saving data in entry variable
        entry= Bookhqtocircle(officerbeltno=beltno, rank=rank, officername=officername, date=date, diaryno=diaryno, circle=circle, serialfrom=serialfrom, serialto=serialto)
        # saving data from entry to session
        db.session.add(entry)
        # commit data to database
        db.session.commit()
    return render_template('Success.html')
# data saved break point


###### Rout Seperation #######


# Book Issued: Circle 2 Sector
# Input Form: Circle 2 Sector
@app.route('/bookCircle2Sector', methods=['GET', 'POST'])
def bookcircle2sector():
    pageTitle="Book Issued: Circle to Sector"
    return render_template('bookCircle2Sector.html', pageTitle=pageTitle)

# Data Saved Entry: Circle 2 Sector
@app.route('/Circle2SectorSuccess', methods=['GET', 'POST'])
def circle2sectorsuccess():
    if(request.method=='POST'):
        '''Add Entry to the Database'''
        beltno= request.form.get('officerbeltno')
        rank = request.form.get('rank')
        officername = request.form.get('officername')
        date = request.form.get('date')
        city = request.form.get('city')
        sector = request.form.get('sector')
        serialfrom = request.form.get('serialfrom')
        serialto = request.form.get('serialto')
        # saving data in entry variable
        entry= Bookcircletosector(officerbeltno=beltno, rank=rank, officername=officername, date=date, city=city, sector=sector,  serialfrom=serialfrom, serialto=serialto)
        # saving data from entry to session
        db.session.add(entry)
        # commit data to database
        db.session.commit()
    return render_template('Success.html')
# data saved break point


###### Rout Seperation #######

# Book Issued: Sector 2 Officer
# Input Form: Sector 2 Officer
@app.route('/bookSector2Officer', methods=['GET', 'POST'])
def booksector2officer():
    pageTitle="Books Issued: Sector to Officer"
    return render_template('bookSector2Officer.html', pageTitle=pageTitle)

# Data Saved Entry: Circle 2 Sector
@app.route('/Sector2OfficerSuccess', methods=['GET', 'POST'])
def sector2officersuccess():
    if(request.method=='POST'):
        '''Add Entry to the Database'''
        officerbeltno= request.form.get('officerbeltno')
        rank = request.form.get('rank')
        officername = request.form.get('officername')
        bookno = request.form.get('bookno')
        date = request.form.get('date')
        # saving data in entry variable
        entry= Booksectortoofficer(officerbeltno=officerbeltno, rank=rank, officername=officername,bookno=bookno, date=date)
        # saving data from entry to session
        db.session.add(entry)
        # commit data to database
        db.session.commit()
    return render_template('Success.html')
# data saved break point

###### Rout Seperation #######

# Entry: Ticket Information
# Input Form: Ticket Information
@app.route('/entryTicketInfo', methods=['GET', 'POST'])
def entryticketinfo():
    pageTitle = "Entry: Ticket Information"
    return render_template('entryTicketInfo.html', pageTitle=pageTitle)

# Data Saved Entry: Ticket Information
@app.route('/TicketInfoSuccess', methods=['GET', 'POST'])
def ticketinfosuccess():
    if(request.method=='POST'):
        '''Add Entry to the Database'''
        officerbeltno= request.form.get('officerbeltno')
        rank = request.form.get('rank')
        officername = request.form.get('officername')
        date = request.form.get('date')
        diaryno = request.form.get('diaryno')
        circle = request.form.get('circle')
        serialfrom = request.form.get('serialfrom')
        serialto = request.form.get('serialto')
        # saving data in entry variable
        entry= Entryticketinfo(officerbeltno=officerbeltno, rank=rank, officername=officername, date=date, diaryno=diaryno, circle=circle, serialfrom=serialfrom, serialto=serialto)
        # saving data from entry to session
        db.session.add(entry)
        # commit data to database
        db.session.commit()
    return render_template('Success.html')
# data saved break point

###### Rout Seperation #######

@app.route('/paidTicketInfo')
def paidTicketInfo():
    pageTitle = "Paid Ticket: Information"
    return render_template('paidTicketInfo.html', pageTitle=pageTitle)


###### Rout Seperation #######

@app.route('/usedCBInfo')
def usedCBInfo():
    pageTitle="Used Challan Books Information"
    return render_template('usedCBInfo.html', pageTitle=pageTitle)


###### Rout Seperation #######

@app.route('/entryBankName')
def enteryBankName():
    pageTitle = "Entry: Bank Name"
    return render_template('entryBankName.html', pageTitle=pageTitle)


###### Rout Seperation #######

@app.route('/entryVehicleCategory')
def enteryVehicleCategory():
    pageTitle = "Entry: Vehicle Category"
    return render_template('entryVehicleCategory.html', pageTitle=pageTitle)


###### Rout Seperation #######

# Entry: Ticket Information
# Input Form: Ticket Information
@app.route('/statementsRegisters', methods=['GET', 'POST'])
def statementregisters():
    pageTitle="Statements / Registers"
    return render_template('statementsRegisters.html', pageTitle=pageTitle)

# Data Saved Entry: Ticket Information
@app.route('/StatementsRegistersSuccess', methods=['GET', 'POST'])
def statementregistersuccess():
    if(request.method=='POST'):
        '''Add Entry to the Database'''
        officerbeltno= request.form.get('officerbeltno')
        rank = request.form.get('rank')
        officername = request.form.get('officername')
        date = request.form.get('date')
        diaryno = request.form.get('diaryno')
        circle = request.form.get('circle')
        serialfrom = request.form.get('serialfrom')
        serialto = request.form.get('serialto')
        # saving data in entry variable
        entry= Entrystatementregister(officerbeltno=officerbeltno, rank=rank, officername=officername, date=date, diaryno=diaryno, circle=circle, serialfrom=serialfrom, serialto=serialto)
        # saving data from entry to session
        db.session.add(entry)
        # commit data to database
        db.session.commit()
    return render_template('Success.html')
# data saved break point

###### Rout Seperation #######

@app.route('/rcvBook')
def rcvBook():
    pageTitle = "Receive Book"
    return render_template('rcvBook.html', pageTitle=pageTitle)


###### Rout Seperation #######

@app.route("/test/<string:post_slug>", methods=['GET'])
def testPage(post_slug):
    ali='aliali'
    sample=Bookhqtocircle.query.filter_by(slug=post_slug).first()
    return render_template('test.html', params=params, sample=sample)

####ali####
###### Rout Seperation ##########

app.run(debug=True)
#app.run(host='172.40.4.27',port=5000, debug=True)