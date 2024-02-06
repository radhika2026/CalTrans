import requests
import pandas as pd
from io import StringIO
from bs4 import BeautifulSoup
from datetime import datetime
from .utils import adjust_time_parameters

class API():
    def __init__(self, username, password):
            self.base_url = "https://pems.dot.ca.gov/"
            self.session = self.authenticate(username, password)

    def authenticate(self, username, password):
        values = {'username': username, 'password': password}
        response = requests.post(self.base_url, data=values)
        if "Incorrect username or password" in response.text:
            print("Incorrect username or password")
            return None
        session = requests.Session()
        session.cookies = response.cookies
        return session
        
    def generate_query(self, station_id, start_time, end_time, dnode='VDS', content='loops', tab='det_timeseries',
                    export='text', q='vmt', gn='hour', tod='all', tod_from=0, tod_to=0,
                    dow=[1, 1, 1, 1, 1, 1, 1], holidays='on', q2=''):
        
        start_time_encoded, end_time_encoded = adjust_time_parameters(start_time, end_time)
        dow_values = ''.join('&dow_' + str(i) + '=on' for i in range(len(dow)))
        parameters =  f"report_form=1"\
            f"&station_id={station_id}"\
            f"&dnode={dnode}"\
            f"&content={content}"\
            f"&tab={tab}"\
            f"&export={export}"\
            f"&q={q}"\
            f"&gn={gn}"\
            f"&s_time_id={start_time}&s_time_id_f={start_time_encoded}"\
            f"&e_time_id={end_time}&e_time_id_f={end_time_encoded}"\
            f"&tod={tod}&tod_from={tod_from}&tod_to={tod_to}"\
            f"{dow_values}"\
            f"&holidays={holidays}"\
            f"&q2={q2}"
        
        return parameters


    def pull_data(self, parameters):
        if self.session is None:
            print("Error: Session authentication failed. Cannot make request.")
            return
        response = self.session.get(self.base_url + "?" + parameters)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')
            df = pd.read_table(StringIO(str(soup)))
            print("df", df)
        else:
            print("error")
    
    def pull_data_for_multiple_stations(self, station_ids, start_times, end_times):
        if len(station_ids) != len(start_times) != len(end_times):
            print("Error: Length of station_ids, start_times, and end_times must be the same.")
            return
        
        for station_id, start_time, end_time in zip(station_ids, start_times, end_times):
            parameters = self.generate_query(station_id=station_id, start_time=start_time, end_time=end_time)
            self.pull_data(parameters)
             

# generate_query(station_id=station_id, start_time=start_time, end_time=end_time)


