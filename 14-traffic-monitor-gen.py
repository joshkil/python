import random
import math

# This program is designed to work with the traffic-monitor.py programming challenge.
# The program generates two lists of integers representing timestamps
# from two traffic monitors. 

# Given the data of two traffic measurement devices (x and y) configured 
# as shown below. Calculate the number of cars traveling in each direction
# as well as the average and maximum speed of any one car. 
# When a car passes over a sensor, a timestamp in millisecondes past 
# 00:00 hrs is recorded. You can consider each sensor to be at the 
# exact east-west position on the road. 
#                   
# __________________________|_______________________
#   West                    |     <-----        
#  -  -  -  -  -  -  -  -  -|  -  -  -  -  -  -  
#                 ---->     |<-d->|             East
# __________________________|_____|_________________
#                         | x | | y |
#   traffic measuring  >> |___| |___|
#             devices
#   The distance, d, can be considered to infinitesimally small. 
# 
# x =  [841, 976, 1289, 1428, 2600, 2689, 3105, 3203, 6823, 6937, 7395, 7555, 10699, 10788, 12229, 12378, 13771, 13946, 20014, 20106, 22807, 22927, 24729, 24845, 25806, 25950, 27612, 27707, 28815, 28908, 31633, 31728, 32043, 32151, 33315, 33418, 35465, 35604, 37632, 37725, 38113, 38232, 39346, 39488, 40808, 40974, 41309, 41414, 42015, 42142, 43121, 43283, 47812, 47939, 49226, 49343, 53331, 53475, 54465, 54578, 55053, 55202, 58507, 58599]
# y =  [1289, 1428, 2600, 2689, 12229, 12378, 22807, 22927, 24729, 24845, 25806, 25950, 32043, 32151, 33315, 33418, 35465, 35604, 38113, 38232, 42015, 42142, 43121, 43283, 49226, 49343, 53331, 53475, 55053, 55202]
# ANSWERS
# car_count_west:  17
# avg_speed_west:  79.41 km/h
# max_speed_west:  99 km/h
# car_count_east:  15
# avg_speed_east:  70.13 km/h
# max_speed_east:  99 km/h
#
#



RUNTIME_SEC = 60
WHEEL_BASE_MM = 2430
MAX_SPEED_KM_H = 100 
MIN_SPPED_KM_H = 50
random.seed()

x = list()
y = list()

car_count_west = 0
car_count_east = 0
avg_speed_west = 0
avg_speed_east = 0
max_speed_west = 0
max_speed_east = 0


for i in range(RUNTIME_SEC):
    west_bound = random.choice([True, False, False])
    east_bound = random.choice([True, False, False])
    # create an offset so that we don't create each ts1 at a factor of 1000
    offset = random.randrange(0,900) 
    
    if west_bound: 
        speed_km_h = random.randrange(MIN_SPPED_KM_H, MAX_SPEED_KM_H)
        speed_mm_h = speed_km_h * math.pow(10, 6) # 10^6 mm in one km
        speed_mm_ms = speed_mm_h / (60 * 60 * math.pow(10,3)) # 3600 s/h 10^3 ms/s
        ts_1 = (i*1000) + offset # convert seconds to ms
        time_to_back_wheels = WHEEL_BASE_MM / speed_mm_ms
        ts_2 = math.ceil(ts_1 + time_to_back_wheels)
        x.extend([ts_1, ts_2])
        car_count_west += 1
        avg_speed_west += speed_km_h
        max_speed_west = max(max_speed_west, speed_km_h)
       
      
    if east_bound and not west_bound: 
        speed_km_h = random.randrange(MIN_SPPED_KM_H, MAX_SPEED_KM_H)
        speed_mm_h = speed_km_h * math.pow(10, 6) # 10^6 mm in one km
        speed_mm_ms = speed_mm_h / (60 * 60 * math.pow(10,3)) # 3600 s/h 10^3 ms/s
        ts_1 = (i*1000) + offset # convert seconds to ms
        time_to_back_wheels = WHEEL_BASE_MM / speed_mm_ms
        ts_2 = math.ceil(ts_1 + time_to_back_wheels)
        # add to both lists
        x.extend([ts_1, ts_2])
        y.extend([ts_1, ts_2])
        car_count_east += 1
        avg_speed_east += speed_km_h
        max_speed_east = max(max_speed_east, speed_km_h)
        


print("# x = ", x)
print("# y = ", y)
print("# ANSWERS")

print("# car_count_west: ", car_count_west)
print("# avg_speed_west: ", round(avg_speed_west/car_count_west, 2), "km/h")
print("# max_speed_west: ", max_speed_west, "km/h")

print("# car_count_east: ", car_count_east)
print("# avg_speed_east: ", round(avg_speed_east/car_count_east, 2), "km/h")
print("# max_speed_east: ", max_speed_east, "km/h")

