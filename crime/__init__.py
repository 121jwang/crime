import urllib
import json


class Imp:
    def __init__(self, key):
        urllib.request.urlcleanup()
        self.response = urllib.request.urlopen(
            urllib.request.Request(
                f"https://api.usa.gov/crime/fbi/sapi/api/data/nibrs/arson/offense/national/count?api_key={key}"
            )
        )
        self.obj = json.loads(self.response.read())

    def results(self):
        return self.obj['results']
    
    def byYear(self):
        return {d["return_year"]: d for d in results()}

