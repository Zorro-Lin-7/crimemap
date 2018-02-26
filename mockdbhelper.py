class MockDBHelper(object):
    
    def connect(self, database='crimemap'):
        pass
        
    def add_crime(self, category, date, latitude, longitude, description):
        data = [category, date, latitude, longitude, description]
        for i in data:
            print(i, type(i))
            
    def get_all_inputs(self):
        return []
                 
    def add_input(self, data):
        pass
        
    def clear_all(self):
        pass