#!/usr/bin/python

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model_json = my_model.to_dict()
my_new_model = BaseModel(**my_model_json)

