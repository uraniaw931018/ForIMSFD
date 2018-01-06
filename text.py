# I select this one because it's originated from the first
# academic experience in my resume: Campus Page Database Management System, 
# which is from my database course. I complete this project almost
# on my own because in the final, everybody's time is limited, 
# so in terms of our four in the group, the other three can not write that
# and have to learn it, so for completing the final goal, I spent two days
# completing the project, with a little experience from some courses before. 

# There is an interesting thing is that: The SALT attribute was added after all
# the table has been created and all data has been inserted, so it's hard to insert
# it one by one because it needs to be calculated from password using sha256, 
# so I add a function in the following code in the "if pw == hashlib.sha256(salt.encode() + password.encode()).hexdigest():" part
# if login unscussefully, calculate and insert into table the related hash attribute, 
# then login one by one, refresh table, then all the hash code has been inserted easier.
# Although it's not a so flexible way to solve the problem, but it just shows me
# that coding can be used in multiple situations even in face of doing some big
# adjustment, what matters is how we can manipulte it flexiblely.

class LoginHandler(BaseHandler):
    def get(self):
        self.set_secure_cookie("user", '', expires=time.time() + 900)
        self.render('login.html')
    def post(self):
        userid = self.get_argument("ui")
        password = self.get_argument("pw")
        print(userid)
        print(password)
        ret = self.db.query('SELECT * FROM user WHERE userid = %s', userid)
        if ret:
            self.set_secure_cookie("user", self.get_argument("ui"),expires=time.time()+900)
            type = ret[0]['usertype']
            salt = ret[0]['salt']
            pw = ret[0]['Password']

            if pw == hashlib.sha256(salt.encode() + password.encode()).hexdigest():
                if not type:
                    self.render('student.html')
                elif (type == 'A'):
                    self.render('admin.html')
                elif (type == 'S'):
                    self.render('student.html')
                elif (type == 'F'):
                    self.render('staff.html')
            else:
                self.write("Please input the right passworld!")

        else:
            self.render('register.html')

