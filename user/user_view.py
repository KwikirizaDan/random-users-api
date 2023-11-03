from flask import Blueprint,jsonify,request
from .user_model import User
from faker import Faker
import random
import string
import secrets
import  json

user = Blueprint("user",__name__)
profile_image = 'https://xsgames.co/randomusers/avatar.php?g=male'
user_list = []
user_dic = {}
fake = Faker()

def password():
  letters = string.ascii_letters
  digits = string.digits
  special_chars = string.punctuation
  password_length = 12
  alphabet = letters + digits + special_chars

  password = ""
  for i in range(password_length):
    password +="".join(secrets.choice(alphabet))

  return password
  

@user.route("/")
def get_users():
  limit = request.args.get('limit')
  limit = int(limit)
  if limit > 25:
    return jsonify({"message":"You can't exeed the limit"})
    
  for i in range(limit):
    pass_word = password()
    name = fake.name()
    
    user = User(i,name,profile_image,pass_word) 
    #print(name)
    
    user_dic = {"id":user.id,"name":user.name,"profile_img":user.profile_img,"password":user.password}
    
    
    user_list.append(user_dic)
    #print(user_dic)
    #print(name)
  return jsonify(user_list)

@user.route("/<int:id>")
def get_user(id):
  
  return jsonify(user_list[id])