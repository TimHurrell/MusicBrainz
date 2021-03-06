import unittest
from Scraping import myRequiredData
from Scraping import RemoveRereleases
#target = __import__('request.py')
#myRequiredData = target.myRequiredData


class TestFilter(unittest.TestCase):
    def test_filter(self):
        """
        Test filter is true
        
        """
        releasetype = "Album"
        releasestatus = "Official"
        releaseyear = "2018"
        result = myRequiredData(releasetype,releasestatus,releaseyear)
        self.assertIs(result.filter,True)


class TestList(unittest.TestCase):

    def test_list(self):
        """
        Test filter is true
        
        """
        List1 = [("Queen","Flash","2017"),("Queen","Flash","2018")]
        result = RemoveRereleases(List1)
        for release in result:
            print (release)
       # print(result.title)
        #self.assertIs(result.filter,True)

if __name__ == '__main__':  
    unittest.main()
 
