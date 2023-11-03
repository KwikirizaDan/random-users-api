from flask import Blueprint,jsonify,request
from .profile_model import Profile
from faker import Faker

profile = Blueprint("profile",__name__)
profile_list = []
profile_dic = {}
fake = Faker()
profile_image = "https://xsgames.co/randomusers/avatar.php?g=male"
@profile.route("/")
def get_profiles():
  limit = request.args.get('limit')
  limit = int(limit)
  if limit > 25:
    return jsonify({"message":"You can't exeed the limit"})
  for i in range(limit):
    profile = Profile(i,fake.name(),profile_image,fake.url(),fake.job(),fake.address(),fake.phone_number(),fake.company())
    profile_dic = {"id":profile.id,"name":profile.name,"profile image":profile.profile_pic,"name":profile.url,"job":profile.job,"address":profile.address,"phone_number":profile.phone_number,"company":profile.company}
    
    profile_list.append(profile_dic)
  return jsonify(profile_list)

@profile.route("/<int:id>")
def get_profile(id):
  return jsonify(profile_list[id])