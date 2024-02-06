from CalTrans import API

def main():
    api = API('arabinowitz@ucdavis.edu',  "Motivation1!!")

    # Define the station IDs, start times, and end times
    station_ids = ["1114091"]
    start_times = [1706659200]
    end_times = [1706705940]

    # Pull data for each station
    # for station_id, start_time, end_time in zip(station_ids, start_times, end_times):
    #     parameters = api.generate_query(station_id=station_id, start_time=start_time, end_time=end_time)
    #     api.pull_data(parameters)
    api.pull_data_for_multiple_stations(station_ids, start_times, end_times)

if __name__ == "__main__":
    main()