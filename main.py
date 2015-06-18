import json
import webapp2
from utilities.food_truck_data_source import FoodTruckDataSource
from jinja2 import Environment, PackageLoader

foodTruckCollection = FoodTruckDataSource.getFoodTrucks()

class MainPage(webapp2.RequestHandler):
  def get(self):
        search_loc_text=self.request.get('search-loc-text')

        template_values = {
            'DefaultLocation': 'San Francisco',
        }
        env = Environment(loader=PackageLoader('main',''))
        template = env.get_template('index.html')
        self.response.out.write(template.render(template_values))

class getFoodTruckDataByAddress(webapp2.RequestHandler):
    def get(self):
        address = self.request.get('address')
        data = foodTruckCollection.getTruckData(address)
        self.response.out.write(json.dumps(data))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/trucksByAddr', getFoodTruckDataByAddress),

], debug=True)

def main():
    app.run()

if __name__ == "__main__":
    main()