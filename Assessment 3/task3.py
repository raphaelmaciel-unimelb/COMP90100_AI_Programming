import csv
import json
import os

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
              if(float(walkydict[key]) >= good_health[key]):
                health_counter += 1
            except:
              continue
    
    #return colour-coded classification string
    if health_counter <= 3:
      return conditions[health_counter]
    else:
      return ""

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


      totalsteps = int()
      steplistsize = int()
      
      totalsleep = int()
      sleeplistsize = int()

      totalgreendays = int()
      hightestdailystep = int()

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
          "average_steps": avg_steps,
          "average_sleep_hours": round(avg_sleep,2),
          "green_days": totalgreendays,
          "highest_daily_step_count": hightestdailystep
          }
    else:
      #in case walkydict_list is empty
      report = {
        "average_steps": 0,
        "average_sleep_hours": 0,
        "green_days": 0,
        "highest_daily_step_count": 0
        }
    
    return report

def load_walky_file(filename):
  
    """
    Returns the JSON file with summary report 

    Args:
      filename (csv file): predefined header (steps,exercise_time,sleep_time)
    Returns:
      Report in a suitable JSON format to a file called 'task3.json' {
        "Average steps": float,
        "Average sleep hours": float,
        "Number of green days": int,
        "Highest daily step count": int
      }  
    """
    if not os.path.exists(filename):
      print(f"Couldn't find file with name {filename}")
    else:
      with open(filename, "r") as fp:
        data = csv.reader(fp)
        datalist = list(data)
        
        header = datalist[0]
      
        if len(header) == 0:
          print(f"[warn] The input file is empty or couldn't be loaded")
          return None
        else:
          rows = datalist[1:]

          multiple_days=[]

          #reading the input file lines and creating the dict data structure
          for row in rows:
            lines = {
              "steps": int(row[0]),
              "exercise_time": int(row[1]),
              "sleep_time": float(row[2])
            }
            multiple_days.append(lines)

            json_data=dict()
            json_data = multiple_days

          #creating the json file with the health data report
          with open("task3.json", "w") as outfile:
              health_report = produce_report(json_data)#creating health summary report data structure
              json.dump(health_report, outfile, indent=4) #saving data summary report to the output file
          return True      

if load_walky_file("example.csv"):
  print( "Data saved successfully to 'task3.json' ")
else:
  print( "Failed to save data to 'task3.json'")
