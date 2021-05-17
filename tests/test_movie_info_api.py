# unit tests for movie_info_api module

#imports
from movie_info_api import MovieInfo

#tests starts here

#object initailization
movie_obj = MovieInfo()

def test_fetch_info():
    """
    get status 200 if movie exist ,404 otherwise
    """

    #movie does'nt exists
    status = movie_obj.fetch_info('godzilla98')
    assert status == 404

    #movie  exist
    status = movie_obj.fetch_info('godzilla')
    assert status == 200




def test_get_movie_details():
    """
    get details asked by user about the movie
    None otheriwse
    """
    #valid attribute passed
    res = movie_obj.get_movie_details(
        [
            'year'
        ]
    )
    assert res['year'] == 2021

    #invalid attribute passed
    res = movie_obj.get_movie_details(
        [
            'director_name'
        ]
    )
    assert res == None


