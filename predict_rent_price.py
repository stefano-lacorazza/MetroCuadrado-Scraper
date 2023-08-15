import pickle
import pandas as pd
api_key = 'AIzaSyB7ll_7odkimkj8vly0VIt-Dol9useuv5Q'
import requests

    
def lat_lon(p_address, p_city):
    address1 = p_address+'%20'+p_city
    address2 = address1.replace(' ','%20').replace('#','%23')

    api_response = requests.get(
                'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address2, api_key))
    api_response_dict = api_response.json()

    if api_response_dict['status'] == 'OK':
                    latitude = api_response_dict['results'][0]['geometry']['location']['lat']
                    longitude = api_response_dict['results'][0]['geometry']['location']['lng']
    return (latitude, longitude)
def main():
    with open('rent_predictor_model.pkl', 'wb') as model_file:
        model_RFR = pickle.load(model_file)
    city = input("Enter city name")
    address = input("Enter property adress")
    built_area = input("Enter built area")
    total_area = input("Enter total area")
    estrato = input("Enter 'estrato'")
    rooms = input("Enter number of rooms")
    parking_lots = input("Enter number of parking lots")
    bathrooms = input("Enter number of bathrooms")
    age = input("Enter age of the property in years")

    apto = pd.DataFrame([[city, built_area, 
                                  total_area, estrato, 
                                  rooms, parking_lots, 
                                  bathrooms, age, str(lat_lon(address, city)[0]), str(lat_lon(address, city)[1])]])

    print("The predicted rent cost is: "+ str(model_RFR.predict(apto)[0])+' COP')
    



if __name__ == "__main__":
    main()