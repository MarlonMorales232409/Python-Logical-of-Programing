import requests
import urllib
import json

# api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjQ3MTJkOTI1LTZhYzctNGZmOS1hOWM1LTQ2MDQ2NmQxNWNlNCIsImlhdCI6MTYzNzM1NjI2NSwic3ViIjoiZGV2ZWxvcGVyL2E4NzA4ODAzLTJkY2MtNDA3Yy1iZWJiLTZlNzZmYjcwNTJkOCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE1Mi4yMDcuMjIzLjYiXSwidHlwZSI6ImNsaWVudCJ9XX0.jvsYwjuwgCl4S0KRbHJyfZTrGAnncO8FdoGgSmxhZhYHk9lEQVKMAb1WpCxbmN3uxtTq-0VmVDB2HSj0RrTI1A"


class Barcher(object):
    """
    A simple client library for the Clash of Clans API in python
    """

    def __init__(self, token):
        import requests
        self.requests = requests
        self.token = token
        self.api_endpoint = "https://api.clashofclans.com/v1"
        self.timeout = 30

    """
    Generic get method to the API
    """

    def get(self, uri, params=None):
        headers = {
            'Accept': "application/json",
            'Authorization': "Bearer " + self.token
        }

        url = self.api_endpoint + uri

        try:
            response = self.requests.get(
                url, params=params, headers=headers, timeout=30)
            return response.json()
        except:
            if 400 <= response.status_code <= 599:
                return "Error {}".format(response.status_code)
    """
    Search for clans with specific criteria
    params: {
      "name": 'SomeClanName',
      "warFrequency": ['always', 'moreThanOncePerWeek','oncePerWeek','lessThenOncePerWeek','never','Unknown'],
      "locationId": 1,
      "minMembers": 20,
      "minClanPoints": 1200,
      "minClanLevel": 1-10,
      "limit": 5,
      "after": 2,
      "before": 100
    }
    """

    def search_clans(self, params):
        return self.get('/clans', params)

    """
    Find a specific clan by clan tag (omit # symbol)
    ex: #123456 would be
    client.find_clan("123456")
    """

    def find_clan(self, tag):
        return self.get('/clans/%23' + tag)

    """
    Retrieve member for a specific clan tag
    client.clan_members_for("123456")
    """

    def clan_members_for(self, tag):
        return self.get('/clans/%23' + tag + '/members')
    """
    return all locations for clash players
    client.locations()
    """

    def locations(self):
        return self.get('/locations')

    """
    return specific location by its id
    client.location(4)
    """

    def location(self, id):
        return self.get('/locations/' + id)

    """
    return all rankings associated with a given location:
    client.rankings_at_location(1, 5)
    """

    def rankings_at_location(self, location_id, ranking_id):
        return self.get('/locations/' + location_id + '/rankings/' + ranking_id)

    """
    return all leagues
    client.leagues()
    """

    def leagues(self):
        return self.get('/leagues')


token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjQ3MTJkOTI1LTZhYzctNGZmOS1hOWM1LTQ2MDQ2NmQxNWNlNCIsImlhdCI6MTYzNzM1NjI2NSwic3ViIjoiZGV2ZWxvcGVyL2E4NzA4ODAzLTJkY2MtNDA3Yy1iZWJiLTZlNzZmYjcwNTJkOCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE1Mi4yMDcuMjIzLjYiXSwidHlwZSI6ImNsaWVudCJ9XX0.jvsYwjuwgCl4S0KRbHJyfZTrGAnncO8FdoGgSmxhZhYHk9lEQVKMAb1WpCxbmN3uxtTq-0VmVDB2HSj0RrTI1A"
client = Barcher(token)
print(client.search_clans({'name': 'five'}))
# print(client.locations())
# print(client.location('32000209'))

"""
curl -H "Authorization: Bearer Your-API-Key" https://api.clashofclans.com/v1/clans?name=five
"""
