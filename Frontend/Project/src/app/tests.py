
import unittest
from mockdb import mockDB
from app import app

    
class TestRestApi(mockDB):
    #check if response is 200
    def test_index(self):
        with self.mock_db_config: 
            tester = app.test_client(self)
            response = tester.get('/')
            statuscode = response.status_code
            self.assertEqual(statuscode,200)
 
    #check if content return is charset=utf-8
    def test_index_context(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.content_type,"text/html; charset=utf-8")

    # check for data returned 
    def test_index_data(self):
        with self.mock_db_config:
            tester = app.test_client(self)
            response = tester.get('/')
            self.assertTrue(b'date' in response.data)
            self.assertTrue(b'panel_id' in response.data)
            self.assertTrue(b'DC_Power' in response.data)
            self.assertTrue(b'AC_Power' in response.data)
            self.assertTrue(b'daily_yeild' in response.data)
            self.assertTrue(b'total_yeild' in response.data)
            self.assertTrue(b'ambient_temperature' in response.data)
            self.assertTrue(b'module_temperature' in response.data)
            self.assertTrue(b'irrediance' in response.data)					

if __name__ == "__main__":
    unittest.main()
