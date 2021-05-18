
# tests for filehandler module

#imports
from filehandler import FileHandler

#tests starts from here
def test_JsonFile():
    """
    testing with json files
    """

    f = FileHandler('json')

    data = [
        {
            'country': 'india',
            'year': 2021
        }
    ]

    saved = f.write_file(
        data,
        'myjson.json'
    )
    assert saved == True

    json_data = f.read_file('myjson.json')

    assert json_data[0]['country'] == 'india'
    assert json_data[0]['year'] == 2021


def test_CSVFile():
    """
    testing with csv files
    """

    f = FileHandler('csv')

    data = [
        [1, 2, 3],
        [11, 22, 33]
    ]

    saved = f.write_file(data, 'myjson.csv')

    assert saved == True

    response_data = f.read_file('myjson.csv')

    assert response_data[0][0] == "1"
    assert response_data[1][1] == "22"


