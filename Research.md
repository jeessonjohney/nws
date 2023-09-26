NWS: National Weather Report

https://tgftp.nws.noaa.gov/data/observations/metar/stations/

Opening this URL points to a file directory where each files are METAR data stored in a .txt file. 
Each file is specific for the station and the file name is the station name.
Googling how often this data is updated, i found few resources where it mentions that its updated every 1 hour (some of tells its precisely 55 minutes).
Noticed that there is an 'updated at' timestamp. which denotes the time at which the data was updated.
Next question is does the METAR data in the directory gets updated randomly for each station or does it sync all at once. Since the stations update it every 1 hour, the cache updating condition should be either station_cache_updated > 5m or station_data_updated > 1h where; station_cache_updated denotes the time at which the cache was introduced to redis and station_data_updated (updated every 5min) denotes the time at which the station pushed new data (updated every one hr).

Noticed that the 'updated at' timestamp which isnt same for all stations. sorted with updated timestamp and found that some of the stations are out dated and doesnt update push METAR data anymore. 
But it seems like all other active stations data is updated all together since the updated time stamp seems to be same or linearly increasing by one second. 

since there are nearly 11k stations and the cache interval is 5 minutes there is no need for a pre-warm cache. More appropriate caching is lazy caching.

