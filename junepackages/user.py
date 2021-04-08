import pyrebase

firebaseConfig = {'apiKey': "AIzaSyBMUlXffmgsJlB2hnEBjXx5l88WgY4Pm2A",
  'authDomain': "projectjune-c542f.firebaseapp.com",
  'databaseURL': "https://projectjune-c542f-default-rtdb.firebaseio.com/",
  'projectId': "projectjune-c542f",
  'storageBucket': "projectjune-c542f.appspot.com",
  'messagingSenderId': "1027810386540",
  'appId': "1:1027810386540:web:3d9efec9ceaa883586ae49",
  'measurementId': "G-V0Q5VL9YWS"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def signup():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    auth.create_user_with_email_and_password(email, password)

signup()


