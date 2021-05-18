import json , csv

class File():
    """
    basic file objects creater
    """
    file = None
    def __init__(self , file_name , file_mode):
        File.file = open(str(file_name),file_mode)


class JsonFile():
    """
    class to handle json file
    """

    def read_data(self , file_name):
        File(file_name , 'r')
        json_data = json.load(File.file)
        File.file.close()
        return json_data


    def write_data(self , data , file_name):

        File(file_name, 'w')
        json_data = json.dump( data , File.file)
        File.file.close()
        return True



    def __bool__(self):
        return FileHandler.file_type == "json"



class CSVFile():
    """
    class to handle csv file
    """

    def read_data(self , file_name):
        File(file_name,'r')
        csv_data = csv.reader(File.file)
        csv_data_list = []

        for data in csv_data:
            csv_data_list.append(data)

        File.file.close()
        return csv_data_list


    def write_data(self , data , file_name):
        try:
            File(file_name, 'w')
            writer = csv.writer(File.file)
            writer.writerows(data)
            File.file.close()
            return True
        except:
            return False

    def __bool__(self):
        return FileHandler.file_type == "csv"


class TextFile():
    """
    check if a file is text file
    """
    def __bool__(self):
        return FileHandler.file_type == 'txt'

    def read_data(self, file_name):
        File(file_name,'r')
        data = File.file.read()
        File.file.close()
        return data

    def write_data(self, data, file_name):
        try:
            File(file_name, 'w')
            data = File.file.write(data)
            File.file.close()
            return True
        except:
            return False


class FileHandler():
    """
    class to handle different files format
    """
    file_type = None


    def __init__(self , file_type):
        FileHandler.file_type = file_type.lower()


    def read_file(self , file_name):
        """
        read data from specified file
        """
        if JsonFile():
            return JsonFile().read_data(file_name)

        elif CSVFile() :
            return CSVFile().read_data(file_name)

        elif TextFile():
            return TextFile().read_data(file_name)

        else:
            return None

    def write_file(self , data , file_name):
        """
        write data to specified file
        """
        if JsonFile():
            return JsonFile().write_data( data , file_name)

        elif CSVFile() :
            return CSVFile().write_data( data , file_name)

        elif TextFile():
            return TextFile().write_data(data, file_name)

        else:
            raise TypeError("file type doesn't exist choose from txt , json or csv ")
            return None




