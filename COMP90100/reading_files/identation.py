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

      if not fp.read().strip():
        print(f"[warn] The input file is empty or couldn't be loaded")
        return None
      else:

        data = csv.reader(fp)
        datalist = list(data)
          
        header = datalist[0]
        rows = datalist[1:]

        with open("./task3.json", "w") as outfile:
            json_data = [dict(zip(header, row)) for row in rows] #combining the 2D data (header x row)
            #print(type(json_data))
            #print("json_data:",json_data)
            health_data = json.dumps(json_data) #converting data list to json
            #print(type(health_data))
            #print("health_data:",health_data)
            health_report = produce_report(health_data)
            json_str = json.dump(health_report, outfile, indent=4) #converting return from dict to json and adding to the output file
        return ""  