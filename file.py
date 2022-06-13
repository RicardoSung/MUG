import json

class json_op():
    def __init__(self, json_path, dict_name, dict_data=None):
        self.json_path = json_path
        self.dict_name = dict_name
        self.dict_data = dict_data
        with open(self.json_path,'f') as f:
            self.json_data = json.load(f)

    def json_pop(self):
        return self.json_data[self.dict_name]


    def json_write(self):
        if self.dict_data != None:
            self.json_data[self.dict_name] = self.dict_data
            with open(self.json_path,'w') as f:
                json.dump(self.dict_data, f)
                return True
        else :
            return False




