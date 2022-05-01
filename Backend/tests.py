import unittest
import mysql.connector
from mysql.connector import errorcode
from app import app

MYSQL_USER = "root"
MYSQL_PASSWORD = "biztech07@4"
MYSQL_DB = "biztech07"
MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = "3306"

class TestRestApi(unittest.TestCase):
    #setup test database
    def setUp(self):
        print("setup....................................")
        cnx = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            port=MYSQL_PORT
        )
        cursor = cnx.cursor(dictionary=True)

        #drop database if it already exists
        try:
            cursor.execute("DROP DATABASE {}".format(MYSQL_DB))
            cursor.close()
            print("DB Dropped")
        except mysql.connector.Error as err:
            print("{}{}".format(MYSQL_DB,err))

        cursor = cnx.cursor(dictionary=True)
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(MYSQL_DB)
            )
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
        cnx.database = MYSQL_DB

        #create panelgenearation table
        query = """CREATE TABLE `panelgeneration` (
                    `date` DATE NOT NULL,
                    `panel_id` INT(7),
                    `DC_power` DOUBLE (13,9) NOT NULL,
                    `AC_power` DOUBLE (13,9) NOT NULL,
                    `daily_yeild` DOUBLE (13,9) NOT NULL,
                    `total_yeild` DOUBLE (11,3) NOT NULL,
                    `ambient_temperature` DOUBLE (11,9) NOT NULL,
                    `module_temperature` DOUBLE (11,9) NOT NULL,
                    `irrediance` DOUBLE (9,8) NOT NULL
                )"""
        try:
            cursor.execute(query)
            cnx.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("test_table already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

        #insert data into the panelgeneration table
        insert_data_query = """INSERT INTO `panelgeneration` (`date`,`panel_id`, `DC_Power`, `AC_Power`, `daily_yeild`,`total_yeild`, `ambient_temperature`,`module_temperature`,`irrediance`) VALUES
                                ('2020-05-17', 4136001,224.42,220.04,9351.866667,2516176.867,35.50715917,38.92884879, 0.093825594),
                                ('2020-05-18', 4136001,340.3133333,334.5333333,9266.8,2525592.8,32.15728253,35.15568323, 0.16798548),
                                ('2020-05-19', 4136001,320.6428571,314.9142857,9172.285714,2464013.286,23.7013729,21.968187, 0.015981422),
                                ('2020-05-20', 4136001,294.3733333,289.0266667,9139.266667,2506740.267,33.62940657,37.57149437, 0.206274229),
                                ('2020-05-21', 4136001,369.1733333,362.8133333,8924.266667,2473188.267,35.75847879,41.00935848, 0.238109929),
                                ('2020-05-22', 4136001,373.5928571,367.15,8906.071429,2610284.071,36.88915393,43.0381529, 0.237599299),
                                ('2020-05-23', 4136001,425.08,417.5066667,8101.4,2593261.4,38.68598266,44.41159052, 0.22409626),
                                ('2020-05-24', 4136001,386.5933333,379.8866667,7939.066667,2545621.067,38.56486117,43.50672293, 0.220942424),
                                ('2020-05-25', 4136001,286.8357143,281.35,7890.785714,2618491.786,36.98203237,41.7511568, 0.191253128),
                                ('2020-05-26', 4136001,420.7066667,413.1933333,7856.933333,2537412.933,35.64510623,40.69924507, 0.154430092),
                                ('2020-05-27', 4136001,320.9466667,314.98,7559.4,2601095.4,36.38729221,41.35595914,0.224757782),
                                ('2020-05-28', 4136001,254.2466667,249.3333333,7510.133333,2452741.133,36.11797693,40.40012638,0.224934829),
                                ('2020-05-29', 4136001,456.2214286,447.5071429,7493.214286,2584897.214,37.25479141,44.60627572,0.274623758),
                                ('2020-05-30', 4136001,516.6733333,506.5933333,7035.666667,2563932.667,35.91564847,40.48759877,0.252565094),
                                ('2020-05-31', 4136001,314.3428571,308.5071429,6800.642857,2577214.643,29.7272274,31.1070222,0.066090041),
                                ('2020-06-01', 4136001,103.5285714,100.6,6606.785714,2552473.786,24.98577969,25.3548521,0.052680962),
                                ('2020-06-02', 4136001,143.84,140.3933333,6164.533333,2445053.533,31.52818297,39.44536643,0.323271408),
                                ('2020-06-03', 4136001,514.9733333,504.8733333,6025.266667,2638886.267,28.03211921,71.82951734,0.166819427),
                                ('2020-06-04', 4136001,265.86,260.82,5936,2570237,28.50673903,76.13578828,0.203127349),
                                ('2020-06-05', 4136001,137.2066667,133.9933333,5645.4,2438857.4,31.01463672,78.41396059,0.288733524),
                                ('2020-06-06', 4136001,93.34,90.76,5564.133333,2624263.133,33.36201869,71.7087749,0.265678036),
                                ('2020-06-07', 4136001,130.0266667,126.9333333,4914,2648959,31.5385315,71.34889863,0.223034526),
                                ('2020-06-08', 4136001,340.6133333,334.8133333,4421.266667,2497387.267,32.76734503,71.94022733,0.237023488),
                                ('2020-06-09', 4136001,262.9142857,257.8357143,4332.357143,2632578.357,32.06129237,75.7459543,0.185411752),
                                ('2020-06-10', 4136001,55.56,53.81333333,4320.666667,2653369.667,28.87153155,78.45449728,0.059891529),
                                ('2020-06-11', 4136001,84.6,82.11428571,4318.071429,2556877.071,26.01537355,76.39908786,0.076213266),
                                ('2020-06-12', 4136001,307.7733333,302.3,4073.733333,2433084.733,27.7146523,75.38214117,0.165160775),
                                ('2020-06-13', 4136001,118.9933333,115.7333333,3821.6,2628111.6,30.02002483,78.64223807,0.304937943),
                                ('2020-06-14', 4136001,334.8,329.1,3491.6,2529318.6,27.71768493,71.93408717,0.172524204),
                                ('2020-06-15', 4136001,254.6133333,249.8066667,2133.8,2643669.8,28.1521964,73.68684883,0.163826239),
                                ('2020-06-16', 4136001,22.04666667,21.29333333,1963.533333,2454835.533,28.91297538,71.26802545,0.085298812),
                                ('2020-06-17', 4136001,282.7714286,277.6928571,1650.285714,2641102.286,26.498535,71.3130768,0.031953231)"""
        try: 
            cursor.execute(insert_data_query)
            cnx.commit()
        except mysql.connector.Error as err:
            print("Data insertion to test_table failed\n" +err)
        cursor.close()
        cnx.close()

    #tear down database
    def tearDown(self):
        print("teardown....................................")
        cnx = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )
        cursor = cnx.cursor(dictionary=True)

        #drop test database
        try:
            cursor.execute("DROP DATABASE{}".format(MYSQL_DB))
            cnx.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print("Database{} does not exists. Dropping db failed.".format(MYSQL_DB) )
        cnx.close()


    

    #check if response is 200
    def test_index(self):
        print("test....................................")
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
