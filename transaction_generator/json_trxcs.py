from faker import Faker
import random
import json

class DataEmployee:

    def __init__(self):
        fake = Faker()
        self.id = 0
        self.name = fake.name()
        self.datetime = str(random.randint(2021,2025)) + str(fake.iso8601())[4:] + "Z"
        self.department_id = random.randint(1,12)
        self.job_id = random.randint(1,183)

    def get_json(self):
        p = {
            'id': self.id,
            'name': self.name,
            'datetime': self.datetime,
            'department_id': self.department_id,
            'job_id': self.job_id
        }
        return p
    
    def input_data(x):
        data = []
        for i in range(0, x):
            Data_Gen = DataEmployee()
            valuer = Data_Gen.get_json()
            valuer["id"] = 2000 + i 
            print(valuer)
            data.append(valuer)
        return data

    def main():
        no_of_input = 1000
        event_data = DataEmployee.input_data(no_of_input)
        event_data = {"Hired_employees": event_data}
        with open("C:/Users/Juan David/Downloads/Globant_test/event_data.json", "w") as outfile:
            json.dump(event_data, outfile)

if __name__ == "__main__":
    DataEmployee.main()