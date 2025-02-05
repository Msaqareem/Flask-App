from flask import *
from flask import render_template
import pymysql
import harshfunction


# initialize the app
app  = Flask(__name__)

app.secret_key = "kl_@sy678_yth@9)(#j[f]sd87ty+!"



@app.route('/signup', methods=['POST','GET'])
def signup():
     if request.method =='POST' :
          username = request.form['username']
          email = request.form['email']
          title = request.form['title']
          password1= request.form['password 1']
          password2= request.form['password 2']

     #   check password
          if len(password1)<8:
                return render_template('signup.html',error='password must have more than 8 characters')
          elif password1 != password2 :
                return render_template('signup.html', error='password do not match')
          else:
            #   Connect database
            connection = pymysql.connect(host='localhost',user='root',password='',database='fungocyberdb')

            # prepare data
            userdata = ()

    
       # create cursor
            cursor =connection.cursor()

            # prepare data
            userdata = (username,harshfunction.hash_password(password2),email,title) 

            # sql query
            user_sql = 'insert into users(username,password,email,title) values (%s,%s,%s,%s)'

            # execute query
            cursor.execute(user_sql,(userdata))

            # comit to save database
            connection.commit()

            
            # return to user
            return render_template('signup.html',success='Registration Successful')
     else:
          return render_template('signup.html')
     
    

    #  sign in
@app.route('/signin',methods=['POST','GET'])

def signin():
     if request.method == 'POST':
            username = request.form['username']
            password =request.form['password']

             # connect database
            connection = pymysql.connect(host='localhost',user='root',password='',database='fungocyberdb')

              # create cursor
            cursor =connection.cursor()

               # prepare data
            signindata = (username,password)

               # sql query
            signin_sql = 'select * from users where username = %s and password = %s'

               # execute cursor
            cursor.execute (signin_sql,(signindata))

            if cursor.rowcount == 0:
              return render_template('signin.html',error='Invalid Credentials')

            else:
               session['key'] = username
               return redirect('/')
     else:
          return render_template('signin.html')
          

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/signin') 

if __name__ =='__main__':
    app.run(debug=True)
