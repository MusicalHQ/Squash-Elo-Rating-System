import pickle

class data:
    def __init__(self,data_file,data=[]):
        self.data_file = data_file
        self.data = data
        try:
            self.load()
        except:
            self.save()
    def save(self):
        data_outfile = open(self.data_file,'wb')
        pickle.dump(self.data,data_outfile)
        data_outfile.close()
    def load(self):
        data_outfile = open(self.data_file,'rb')
        self.data = pickle.load(data_outfile)
        data_outfile.close()



