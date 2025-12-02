while True:
    time = input("What time is it? Enter in HH:MM format (24h): ")
    if (len(time) == 5 and time[2] == ":" and
            time[0].isdigit() and time[1].isdigit() and
            time[3].isdigit() and time[4].isdigit()):

        hours_str, minutes_str = time.split(":")
        hours = int(hours_str)
        minutes = int(minutes_str)

        if 0 <= hours <= 23 and 0 <= minutes <= 59:
            break
        else:
            print("Invalid time range! Hours must be 0–23, minutes 0–59.")
    else:
        print("Wrong format! Please use HH:MM.")

total_minutes = (hours * 60) + minutes
total_seconds = total_minutes * 60

print(f"Time: {time}\n"
      f"Since midnight passed: {total_minutes} minutes\n"
      f"Since midnight passed: {total_seconds} seconds")