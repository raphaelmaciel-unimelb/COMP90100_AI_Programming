def daily_health(walkydict):

    """
    Returns the str with a colour-coded classification ranging from 
            "green" (all indicators met) 
        to 
            "red" (no indicators met)
    Args:
      walkydict (dict {"steps": int, "exercise_time": int, "sleep_time": int): three predefined indicators
    Returns:
      conditions[health_counter] (Str) : classification colour-code    
    """

    good_health = {"steps": 10000, "exercise_time": 30, "sleep_time": 7} #dict with the Health indicators
    conditions = {3: "green", 2: "yellow", 1: "orange", 0: "red"} #dict with the condition rules

    health_counter = int(0)

    #counting health counter
    for key in walkydict:
        if (key in good_health):
          try: 
            if(walkydict[key] >= good_health[key]):
                health_counter += 1
          except:
            continue
    
    #return colour-coded classification string
    if health_counter <= 3:
      return conditions[health_counter]
    else:
      return ""

print(daily_health({"steps": 11000, "exercise_time": 40, "sleep_time": 8}))

#Test cases below ----
# print(daily_health({"steps": 11000, "exercise_time": 40, "sleep_time": 3}))
# print(daily_health({"steps": 10500, "exercise_time": 15, "sleep_time": 5}))
# print(daily_health({"steps": 0, "exercise_time": 0, "sleep_time": 0}))
# print(daily_health({"steps": 0, "exercise_time": 0, "sleep_time": -1}))
# print(daily_health({"walk": 0, "gym": 0, "sleep_time": -1}))
# print(daily_health({}))
# print(daily_health({"steps": 11000, "exercise_time": 40, "sleep_time": 8, "gym": 4}))
# print(daily_health({"steps": 'a', "exercise_time": 40, "sleep_time": 8, "gym": 4}))
