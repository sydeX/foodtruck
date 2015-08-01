import json
import webapp2
from utilities.food_truck_data_source import FoodTruckDataSource
from jinja2 import Environment, PackageLoader


foodTruckCollection = FoodTruckDataSource.get_food_trucks()


class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'DefaultLocation': 'San Francisco',
        }

        env = Environment(loader=PackageLoader('main', ''))
        template = env.get_template('index.html')
        self.response.out.write(template.render(template_values))


class FoodTruckDataByAddress(webapp2.RequestHandler):
    def get(self):
        address = self.request.get('address')
        data = foodTruckCollection.get_truck_data(address)
        self.response.out.write(json.dumps(data))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/trucksByAddr', FoodTruckDataByAddress),
], debug=True)


def main():
    app.run()

if __name__ == "__main__":
    main()
