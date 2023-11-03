from flask import Blueprint,jsonify,request
from .testmonial_model import Testmonial
from faker import Faker
import random
import avinit

testmonial = Blueprint("testmonial",__name__)
profile_image= "https://xsgames.co/randomusers/"
testmonial_dir = {}
testmonial_list = []
fake = Faker()
@testmonial.route("/")
def get_testmonials():
  limit = request.args.get('limit')
  limit = int(limit)
  if limit > 25:
    return jsonify({"message":"You can't exeed the limit"})
  for i in range(limit):
    testmonial = Testmonial(id,fake.name(),profile_image,fake.job(),fake.text())
    
    testmonial_dir = {"id":testmonial.id,"name":testmonial.name,"profile_pic":testmonial.profile_pic,"job":testmonial.job,"text":testmonial.text}
    
    testmonial_list.append(testmonial_dir)
  return jsonify(testmonial_list)
   

@testmonial.route("/<int:id>")
def get_testmonial(id):
  
  return jsonify(testmonial_list[id])