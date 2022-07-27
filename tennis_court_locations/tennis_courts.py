"""Info scraped from globaltennisnetwork.com"""
from bs4 import BeautifulSoup
import requests

base_url = "https://www.globaltennisnetwork.com/tennis-courts/courts/city/52-los-angeles-california"
list_of_tennis_parks = []


def la_tennis_courts(): 
    for page_number in range(1,12):
        if page_number == 1:
            url = base_url
        else:
            page = "?page=" + str(page_number)
            url = base_url + page

        park_list = []
        result = requests.get(url)
        soup = BeautifulSoup(result.text, 'html.parser')
        table = soup.find('table', {'class': "table table-striped"})
        data_rows = table.find_all('tr')

        for row in data_rows:
            value = row.find_all('td')
            beautified_value = [ele.text.strip() for ele in value] # type-list
            # print(beautified_value) - [ParkName/Address, Map, Type, Fees, Lights, Indoor, Courts, Players]
            park_list.append(beautified_value)
    #         print(beautified_value)

        park_list = park_list[1:-1]
        del park_list[4]
        
        tennis_park = {}
        outlier = ['109th Street Recreation Center1464 E 109th St, Los Angeles', '', '7.99\xa0m', 'Public', 'No', 'Yes', 'No', '1', '2']
        if outlier in park_list:
            park_list.remove(outlier)
            
        for park in park_list:
            park_name = ""
            address = ""
            for char in park[0]:
                if not char.isdigit():
                    park_name += char
                else:
                    break
            address = park[0].split(park_name)[1]
    #         print(park_name + "\n" + address)
            tennis_park["park_name"] = park_name
            tennis_park["address"] = address
            tennis_park["type"] = park[3]
            tennis_park["fees"] = park[4]
            tennis_park["lights"] = park[5]
            tennis_park["indoor"] = park[6]
            tennis_park["courts"] = park[7]

            list_of_tennis_parks.append(tennis_park)
            tennis_park = {}

    return list_of_tennis_parks

# tennis_courts = la_tennis_courts()

# for court in tennis_courts:
#     print(court)