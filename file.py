import json
import os, sys

file_settings_json={    
    "literature_path": "./" ,
    "md_path":"./"
    }

app_settings_json={

}

language_settings_json={

}


class file_init():
    def __init__(self):
        if not os.path.exists('.MUG'):
            os.makedirs('.MUG')
            with open("./.MUG/file_settings.json",'w') as f:
                json.dump(file_settings_json, f)
            with open("./.MUG/app_settings.json",'w') as f:
                json.dump(app_settings_json, f)
            with open("./.MUG/language_settings.json",'w') as f:
                json.dump(language_settings_json, f)
        else:
            pass



class json_op():
    def __init__(self, json_path, dict=None, dict_name=None, dict_data=None):
        self.json_path = json_path
        self.dict_name = dict_name
        self.dict_data = dict_data
        self.dict = dict
        
    def json_read(self):
        if self.json_path != None:
            with open(self.json_path,'f') as f:
                self.json_data = json.load(f)
    
    # To get a parameter of a property once
    def json_pop(self):
        self.json_read()
        if self.dict_name != None:
                return self.json_data[self.dict_name]

    # To change a parameter of a property once
    def json_write(self):
        self.json_read()
        if self.dict_data != None:
            self.json_data[self.dict_name] = self.dict_data
            with open(self.json_path,'w') as f:
                json.dump(self.dict_data, f)
                return True
        else :
            return False

    def json_write_file(self):
        if self.dict != None:
            with open(self.json_path,'w') as f:
                json.dump(self.dict, f)
                return True
        else :
            return False


