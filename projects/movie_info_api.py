import requests as req


class MovieInfo():
    """
    find movies information
    """

    def __init__(self):
        self.movie_name = None
        self.response = None
        self.movie_info = None

    def fetch_info(
            self,
            movie_name
    ):
        """
        calling rapid api to get info of movie name passed
        """

        if type(movie_name) != str:
            raise TypeError('movie name should be a valid string')

        self.movie_name = movie_name

        url = "https://imdb8.p.rapidapi.com/auto-complete?q="

        headers = {
            "x-rapidapi-key": "919a2fd49dmsh039253a833d99b8p1c7c0ajsne850bfcc7d0f",
            "x-rapidapi-host": "imdb8.p.rapidapi.com",
            "useQueryString": "true"
        }

        try:
            self.response = req.get(
                url + movie_name,
                headers=headers
            )

            status_code = self.save_fetched_info()
            return status_code


        except:
            raise ConnectionError(
                'Oops! some error occured while fetching the movie "{}" '.format(
                    movie_name
                )
            )

    def save_fetched_info(self):
        """
        saves response from movie api
        """
        res = None

        if self.response:

            res = self.response.json()['d'][0]
            self.movie_info = dict()

            try:
                self.movie_info['name'] = res['l']

                if self.movie_name.lower() not in self.movie_info['name'].lower():
                    raise NameError()

                self.movie_info['image_url'] = res['i']['imageUrl']
                self.movie_info['rank'] = res['rank']
                self.movie_info['cast'] = res['s']
                self.movie_info['year'] = res['y']

                return 200

            except:
                print('NameErrror : Check movie name again...')
                return 404

    @staticmethod
    def movie_has_details_asked_by_user(
            detail_name_list,
            movie_info
    ):
        """
        check whether user requested details exists or not in fetched movie data
        """
        if movie_info:
            response = dict()

            for detail_name in detail_name_list:
                if detail_name.lower() in movie_info:
                    response[detail_name] = movie_info[detail_name]

            if len(response) > 0:
                return response

    def get_movie_details(
            self,
            detail_name_list
    ):
        """
        get list of details needed from a movie
        e.g imageUrl , year , name , rank
        """

        data = MovieInfo.movie_has_details_asked_by_user(
            detail_name_list,
            self.movie_info
        )

        if data:
            return data
        else:
            print(
                "user requested details not found for movie '{}' \n"
                "choose from these: imageUrl , year , name , rank"
                    .format(self.movie_name)
            )



