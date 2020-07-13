"""
    Retrive the data for a city from api-adresse.data.gouv.fr
    =========================================================
 
    You can use it for search complete or partial city from string.
 
    :Example:
 
    >>> from getCities import GetCities
    >>> cities = GetCities('bordeaux')
    >>> print('cities')
    
 
    The results
    -----------
 
    If the query is ok, the class will return a list of cities with the number of result.
    The query is considered like ok if the string passed on parameter contains more than three letters.

    The errors
    ----------
    
    The class can return two kinds of errors.
    • If the params is shorter than 3 characters
    • If the request failed
 
"""

class GetCities:

    def __init__(self, userResearch):
        self.cityToSearch = str(userResearch)
        self.url = "http://api-adresse.data.gouv.fr/search/"
        if len(self.cityToSearch) > 3 :
            pass
        else :
            raise ValueError("'userResearch' must contains at least 3 letters")
    
    def __repr__(self):
        """
            Return the result of the query
    
            This return a dict with the following keys:
    
            :nb_of_results: The number of results for the query
            :results: All the cities corresponding to the query
            :type nb_of_results: int
            :type results: int
            :return: A dict with thoose two data
            :rtype: dict
        """
        return self.displayCities()

    def __str__(self):
        result = self.displayCities()
        return "Your research for \" %s \" has %s results." % (self.cityToSearch, result['nb_of_results'])

    def getCitiesFromApi(self):
        """
            Create the request to the api to get cities from the query
        """
        import urllib.parse
        import json
        import requests

        searchCitiesParams = {'q': self.cityToSearch, 'type': 'municipality', 'autocomplete' : 1}
        searchCitiesQuery = urllib.parse.urlencode(searchCitiesParams , quote_via=urllib.parse.quote )
        searchCitiesResponse = requests.get(self.url, params=searchCitiesQuery)

        if searchCitiesResponse.status_code == 200:
            return json.loads(searchCitiesResponse.content.decode('utf-8'))
        else:
            return None

    def displayCities(self):
        """
            Create the dataset for the user
        """
        corresponsiveCities = self.getCitiesFromApi()
        
        if corresponsiveCities is not None:
            userResearchResults = {'nb_of_results': len(corresponsiveCities['features']), 'results' : corresponsiveCities['features']}
            print(userResearchResults)
            return userResearchResults
        else:
            raise ValueError("The request failed")

