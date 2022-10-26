from bs4 import BeautifulSoup
import requests
import unittest

# Task 2: Look at the Get the URL that links to webpage of universities with Olympic medal wins
# search for the url in the University of Michgian wikipedia page (in the third pargraph of the intro)
# HINT: You will have to add https://en.wikipedia.org to the URL retrieved using BeautifulSoup
def getLink(soup):
    tag = soup.find('a', class_="mw-redirect", string = "Olympic Games")
    link = "https://en.wikipedia.org"
    link += tag.get('href')
    return link

# Task 3: Get the details from the box titled "College/school founding". Get all the college/school names and the year they were
# founded and organize the same into key-value pairs.
def getAdmissionsInfo2019(soup):
    tag = soup.find('table', class_="toccolours")
    td_tags = tag.find_all('td')
    td_tags = td_tags[2:]
    dic = {}
    for i in range(len(td_tags) - 1):
        if(i % 2 == 0):
            year = td_tags[i+1].text.rstrip()
            dic[td_tags[i].text] = year
    return dic



def main():
    # Task 1: Create a BeautifulSoup object and name it soup. Refer to discussion slides or lecture slides to complete this

    url = "https://en.wikipedia.org/wiki/University_of_Michigan"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    #Call the functions getLink(soup) and getAdmissionsInfo2019(soup) on your soup object.
    getLink(soup)
    getAdmissionsInfo2019(soup)

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/University_of_Michigan').text, 'html.parser')

    def test_link_nobel_laureates(self):
        self.assertEqual(getLink(self.soup), 'https://en.wikipedia.org/wiki/List_of_American_universities_with_Olympic_medals')

    def test_admissions_info(self):
        self.assertEqual(getAdmissionsInfo2019(self.soup), {'Literature, Science, andthe Arts': '1841',
                                                            'Medicine': '1850', 
                                                            'Engineering': '1854', 
                                                            'Law': '1859',
                                                            'Dentistry': '1875', 
                                                            'Pharmacy': '1876', 
                                                            'Music, Theatre &Dance': '1880', 
                                                            'Nursing': '1893', 
                                                            'Architecture &Urban Planning': '1906', 
                                                            'Graduate Studies': '1912', 
                                                            'Government': '1914', 
                                                            'Education': '1921',
                                                            'Business': '1924', 
                                                            'Environment andSustainability': '1927', 
                                                            'Public Health': '1941', 
                                                            'Social Work': '1951', 
                                                            'Information': '1969', 
                                                            'Art & Design': '1974', 
                                                            'Kinesiology': '1984'})

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)