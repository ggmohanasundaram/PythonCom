# Pycom
Overview
--------
  Weather Data Simulator generates weather data from the internal data store and emits as pipe separated values.
    - This simulator has capable to generate the output with real time data and offline data 
    - This simulator is providing a option to the users to define number of output records
    - This simulator generates and emits random data every time
         
High-Level Architecture: 
-----------------------
 1. Weather Data Simulator fetch real time  data from external source.(Data Sky)
 2. Real time data is transformed into required format and loads into Internal database(JSON)
 3. Emits output data
    
            
                            ---------------------     ----------------------
                            |  Dark Sky adaptor  |    | CSV Output adaptor |
                            ---------------------      ---------------------
                                    ^                        ^
                                    |                        |
                                    |                        |
                            __________________       __________________
                            | Input adaptor  |       | Output adaptor  |
                            --------------------------------------------
                            |            Weather Data Simulator       |
                            ---------------------------------------------
                                      | Data Source adaptor|
                                      ----------------------  
                                               |
                                               |
                                               \/
                                       --------------------
                                       |      JSON            |
                                       --------------------                                      
                                                                      
  Design Decisions:
     
        1. ETL Process-
            - This application has been designed as a ETL component
            - Extract the weather data from extrenal sources
            - Transform the data into requied format
            - Load the transformed data into Internal data store
            
        2. Extensiblity 
            - This application has been designed to support diverse input systems and output source
            - Three interfaces have been provided to achieve extensibility,
                    1. Input adaptor
                    2. Output adaptor
                    3. Data Source adaptor
            - input and ouput sources can be added to the simulator by inherting those adaptors  
             
        3. Reliabilty
            - The application has been designed to support multiple input and output source with mimal code changes
                    a. Configuration file for input and output source
                    b. Dynamically loads the implementation
      
  
  Weather data simulator Low Level Components:
  
    A. Import_command
        - Import command loads the import channel from config.py
        - Import channel - imports data from external source to internal data store
             - DarkSkySource is used as external resource to get the test data
             - app/src/data/weatherdata.json is used as internal data store
        
        Note : InputSource class should be inherited for new external source
               and same should be configured in config.py. Import command will automatically
               load the new classes and import the data into internal data store
        
    B. Export_command
        - Export command loads the export channels from config.py
        - Export channel - exports data from internal data store,transforms them and stores into csv
                - app/src/data/output.csv as used to store the transformed data
                
        Note : OutPutChannel class should be inherited for new internal data store
               and same should be configured in config.py. Export command will automatically
               load the new classes and export the data from internal data store
               
How To Run
----------
    This app is developer in python 3.5
    
    Step 1: pip install -r requirements.txt
    Step 2 : python3 app/weather_simulator_main.py
    Note:
     - This app will produce the output from the static file app/src/data/output.csv

Keyword Arguments
-----------------
    get_weather_data has 3 keyword arguments 
    
      1. count - Number of output records required. The default value is 10
            ex : get_weather_data(count=20)
      2. is_import - is a flag to enable online data as output from external source. Default is False
            ex : get_weather_data(count=20,is_import =True, is_export=True)
      3. is_export - is a flag to enable the app to update the csv file from internal store for latest data
           ex : get_weather_data(count=20, is_export=True)
APP_Key
-------
    The App_key is required to connect with Dataskysource. To get the online data, app_key should be configured
    in config.py
    
    Note: I have removed my app_key from config.py for security reasons. The app key can 
    be generated online(https://darksky.net/dev) or I can share via email.

Sample_output
-------------
    #get_weather_data(count=10)
    
    Welcome to Weather Data Simulator
    Location|Position|Local Time|Conditions Time|Temperature|Pressure|Humidity
    Waitara|-33.7,151.1,171|2017-08-28 00:00:00|Rain|5.51|1019.55|72
    Wynyard|-40.98,145.72,58|2017-08-27 18:00:00|Rain|7.61|1024.3|60
    Fortitude Valley|-27.45,153.03,21|2017-08-28 04:00:00|Sunny|10.28|1017.03|57
    Parramatta|-33.81,151.0,12|2017-08-27 20:00:00|Rain|9.24|1018.84|66
    Herston|-27.44,153.02,31|2017-08-27 04:00:00|Rain|12.41|1019.91|82
    Docklands|-37.81,144.94,10|2017-08-27 09:00:00|Rain|9.93|1023.65|56
    Southbank|-37.82,144.95,4|2017-08-27 03:00:00|Rain|8.17|1019.7|85
    Brisbane|-27.47,153.02,28|2017-08-27 14:00:00|Rain|22.24|1016.37|40
    Hornsby|-33.7,151.09,191|2017-08-27 05:00:00|Rain|5.28|1018.29|85
    -------
    #get_weather_data(is_export=True)
    
    Welcome to Weather Data Simulator
    The step export_data result is True 
    The step export_process result is True 
    The step export_write_data result is True 
    Location|Position|Local Time|Conditions Time|Temperature|Pressure|Humidity
    Waitara|-33.7,151.1,171|2017-08-27 19:00:00|Rain|8.92|1018.06|74
    Wynyard|-40.98,145.72,58|2017-08-26 18:00:00|Rain|11.17|1012.98|80
    Fortitude Valley|-27.45,153.03,21|2017-08-28 07:00:00|Sunny|10.54|1019|55
    Parramatta|-33.81,151.0,12|2017-08-27 18:00:00|Rain|12.26|1017.3|56
    Herston|-27.44,153.02,31|2017-08-28 04:00:00|Sunny|10.24|1017.04|57
    Docklands|-37.81,144.94,10|2017-08-28 10:00:00|Rain|9.23|1027.02|71
    Southbank|-37.82,144.95,4|2017-08-27 00:00:00|Rain|9.46|1019.36|80
    Brisbane|-27.47,153.02,28|2017-08-27 20:00:00|Rain|15.23|1017.2|57
    Hornsby|-33.7,151.09,191|2017-08-28 11:00:00|Sunny|12.84|1020.72|46
    ------
    #get_weather_data(count=20, is_import=True, is_export=True)
    
    Welcome to Weather Data Simulator
    Download data from Dark Sky Source
    The step import_data result is True 
    The step import_process result is True 
    The step import_write_data result is True 
    The step export_data result is True 
    The step export_process result is True 
    The step export_write_data result is True 
    Location|Position|Local Time|Conditions Time|Temperature|Pressure|Humidity
    Wynyard|-40.98,145.72,58|2017-08-29 04:00:00|Sunny|5.42|1020.52|93
    Southbank|-37.82,144.95,4|2017-08-28 21:00:00|Rain|9.04|1025.22|76
    Kangaroo Point|-27.46,153.03,2|2017-08-28 04:00:00|Sunny|10.17|1016.4|57
    East Brisbane|-27.48,153.05,13|2017-08-29 03:00:00|Sunny|9.47|1020.23|67
    Strathfield|-33.88,151.08,38|2017-08-29 09:00:00|Sunny|11.81|1023.96|55
    Highgate Hill|-27.48,153.01,58|2017-08-28 23:00:00|Sunny|11.26|1020.68|64
    South Wharf|-37.82,144.95,4|2017-08-29 11:00:00|Sunny|13.28|1024.46|56
    Parramatta|-33.81,151.0,12|2017-08-27 16:00:00|Rain|15.88|1014.12|43
    Melbourne|-37.81,144.96,25|2017-08-29 02:00:00|Rain|7.09|1024.68|82
    PendleHill|-33.8,150.95,52|2017-08-28 02:00:00|Sunny|6.04|1017.82|63
    North Melbourne|-37.79,144.94,10|2017-08-27 19:00:00|Rain|7.88|1024.73|71
    South Yarra|-37.84,144.98,17|2017-08-28 20:00:00|Rain|9.22|1024.98|74
    West Melbourne|-37.8,144.92,3|2017-08-29 09:00:00|Sunny|10.21|1025.07|66
    Flemington|-37.78,144.92,18|2017-08-27 17:00:00|Rain|8.37|1023.94|69
    Hornsby|-33.7,151.09,191|2017-08-28 01:00:00|Sunny|5.83|1017.74|70
    Paddington|-27.46,153.0,29|2017-08-29 06:00:00|Sunny|8.26|1021.6|68
    Herston|-27.44,153.02,31|2017-08-29 01:00:00|Sunny|10.21|1020.49|64
    Brisbane|-27.47,153.02,28|2017-08-27 19:00:00|Rain|18.88|1015.48|44
    
        
            
            
            
