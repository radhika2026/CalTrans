from CalTrans import API

def main():
    api = API('arabinowitz@ucdavis.edu',  "Motivation1!!")

    # Define the station IDs, start times, and end times
    station_ids = ["1114091"]
    start_times = [1706659200]
    end_times = [1706705940]


    api.pull_data_for_multiple_stations(station_ids, start_times, end_times)

if __name__ == "__main__":
    main()