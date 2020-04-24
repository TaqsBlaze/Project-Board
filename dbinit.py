#Script to initialize database
from LeNode import db
import sys





    
    
class Db:
    def __init__(self):
        self.name = "name"
    def init_db(self):
        try:
            db.create_all()
            print("\n\n\n")
            print("[+]Db initialized successfully")
        except Exception as error:
            print(error)
            
    def drop_db(self):
        print("\n\n\n")
        print("This will delete database table are you sure you want to continue?")
        action = str(input("y/n:"))
        if(action=="y"):
            db.drop_all()
            print("[+]Table(s) deleted")
        else:
            exit()
            
    def usage(self):
        msg='''
        python dbinit.py [option]
        OPTIONS:
        init ------> to initialize db
        drop ------> to drop all tables
        '''
        return msg
try:
    if(sys.argv[1]=='init'):
        Db().init_db()
    else:
        if(sys.argv[1]=='drop'):
            Db().drop_db()
        else:
            Db().usage()
except IndexError:
    Db.usage()