from flask import Flask,jsonify,Blueprint,json
from profile.profile_view import profile
from user.user_view import user
from testmonial.testmonial_view import testmonial

app = Flask(__name__)
app.json.sort_keys = False

app.register_blueprint(user,url_prefix="/user")
#app.register_blueprint(testmonial,url_prefix="/testmonial")
app.register_blueprint(profile,url_prefix="/profile")
if __name__=='__main__':
  app.run(host='0.0.0.0',port=5000,debug=False)


print('')