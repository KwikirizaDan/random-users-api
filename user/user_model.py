class User:
  id = 0
  profile_img = ''
  user_name = ""
  password = ""
  def __init__(self,id,user_name,profile_img,password):
    self.id = id
    self.profile_img = profile_img
    self.name = user_name
    self.password = password

