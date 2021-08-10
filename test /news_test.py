from app.models import Sources
import unittest
from unittest.main import main 


class SourcesTest(unittest.TestCase):
     '''
     Test Class to test the behaviour of the Sources cass
     '''

     def setUp(self):
         '''
         Set up method that will run before every Test
         '''
         self.new_news= Sources(1235,'BBC News','https://www.bbc.co.uk/news/technology-54148474','Business','USA', 'English' ) 

     def test_instance(self):
         self.assertTrue(isinstance(self.new_news,Sources)) 
