import jieba
import csv


class Label():
    def __init__(self, str_list):
        self.label = dict()
        self.label["traffic convenience"] = (str_list[0])
        self.label["distance from business district"] = (str_list[1])
        self.label["easy to find"] = (str_list[2])
        self.label["wait time"] = (str_list[3])
        self.label["waiter’s attitude"] = (str_list[4])
        self.label["parking convenience"] = (str_list[5])
        self.label["serving speed"] = (str_list[6])
        self.label["price level"] = (str_list[7])
        self.label["cost-effective"] = (str_list[8])
        self.label["discount"] = (str_list[9])
        self.label["decoration"] = (str_list[10])
        self.label["noise"] = (str_list[11])
        self.label["space"] = (str_list[12])
        self.label["cleaness"] = (str_list[13])
        self.label["portion"] = (str_list[14])
        self.label["taste"] = (str_list[15])
        self.label["look"] = (str_list[16])
        self.label["recommendation"] = (str_list[17])
        self.label["overall experience"] = (str_list[18])
        self.label["willing to consume again"] = (str_list[19])

    def __str__(self):
        s = ""
        for k, v in enumerate(self.label):
            s += str(k) + " : " + str(v)
        return s


class DataCleaner():
    def __init__(self, file_name):
        self.file_name = file_name
        self.content_list = []
        self.labels = []
        with open(file_name, 'r', encoding='utf-8-sig') as f:
            csv_file = csv.reader(f)
            for row in csv_file:
                self.content_list.append(row[1])
                self.labels.append(Label(row[2:]))


        for i in range(len(self.content_list)):
            if i %1000 == 0:
                print(self.content_list[i])
                print(self.labels[i])


if __name__ == '__main__':
    d = DataCleaner("./data/trainingset/sentiment_analysis_trainingset.csv")