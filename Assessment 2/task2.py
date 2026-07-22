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

    for key in walkydict:
        if (key in good_health): 
            try:
                if(walkydict[key] >= good_health[key]):
                    health_counter += 1
            except:
                continue
    
    return conditions[health_counter]

def produce_report(walkydict_list):
  
    """
    Returns the dict with multi-day summary report 

    Args:
      walkydict_list (list of dict {"steps": int, "exercise_time": int, "sleep_time": int): three predefined indicators
    Returns:
      report (dict) : {
        "Average steps": int,
        "Average sleep hours": int,
        "Number of green days": int,
        "Highest daily step count": int
        }    
    """
    listsize = len(walkydict_list)
    
    #checking if the walkydict_list is not empty
    if listsize != 0:

      totalsteps = int(0)
      steplistsize = int(0)
      
      totalsleep = int(0)
      sleeplistsize = int(0)

      totalgreendays = int(0)
      hightestdailystep = int(0)
      
      #loopint around the list and counting steps, sleep_time and the number of green days
      for i in range(listsize):
        if "steps" in walkydict_list[i]:
          try:
            totalsteps += int(walkydict_list[i]["steps"]) #counting the total of steps
            steplistsize += 1 #counting number of days with steps
            if hightestdailystep < int(walkydict_list[i]["steps"]):
              hightestdailystep = int(walkydict_list[i]["steps"]) #checking the highest daily step
          except ValueError:            
            print(f"  [warn] Steps value: '{walkydict_list[i]["steps"]}' is not numeric")
          
        if "sleep_time" in walkydict_list[i]:
          try:
            totalsleep += float(walkydict_list[i]["sleep_time"])
            sleeplistsize += 1
          except ValueError:            
            print(f"  [warn] Sleep value: '{walkydict_list[i]["sleep_time"]}' is not numeric")
          
        if daily_health(walkydict_list[i]) == 'green':
          totalgreendays += 1 #couting the days in green
      
      #calculating averages for step and sleep
      avg_steps=int(0)
      avg_sleep=float(0)

      if steplistsize:
        avg_steps = int(round(totalsteps/steplistsize))


      if sleeplistsize:
        avg_sleep = float(round(totalsleep/sleeplistsize,2))


      report = {
          "Average steps": avg_steps,
          "Average sleep hours": avg_sleep,
          "Number of green days": totalgreendays,
          "Highest daily step count": hightestdailystep
      }
    else:
      #in case walkydict_list is empty
      report = {
        "Average steps": 0,
        "Average sleep hours": 0.00,
        "Number of green days": 0,
        "Highest daily step count": 0
        }

    print(f"Average steps: {report["Average steps"]}")
    print(f"Average sleep hours: {report["Average sleep hours"]:.2f}")
    print(f"Number of 'green' days: {report["Number of green days"]}")
    print(f"Highest daily step count: {report["Highest daily step count"]}")



produce_report([ {"steps": 11000, "exercise_time": 40, "sleep_time": 8}, {"steps": 6000, "exercise_time": 10, "sleep_time": 5}])

#Test cases below ----
# produce_report([ {"steps": '', "steps":'' , "exercise_time": '', "sleep_time": ''}, {"steps": 1000, "exercise_time": 10, "sleep_time": 5}])
# produce_report([ {"steps": 11000, "exercise_time": 40, "sleep_time": 8}, {"steps": 6000, "exercise_time": 10, "sleep_time": 5}, {"steps": 15000, "exercise_time": 1, "sleep_time": 8}])
# produce_report([ {"exercise_time": 40, "sleep_time": 8}, {"steps": 6000, "exercise_time": 10, "sleep_time": 5}])
# produce_report([ {"exercise_time": 40, "sleep_time": 8}, {"steps": 6000, "exercise_time": 10}])
# produce_report([])
# produce_report("")
# produce_report([ {"exercise_time": 40, "sleep_time": 8}, {"steps": 'a', "exercise_time": 10, "sleep_time": 5}])
# produce_report([ {"exercise_time": 'a', "sleep_time": 'a'}, {"steps": 'a', "exercise_time": 'a', "sleep_time": 'a'}])
