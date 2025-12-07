while True:
    time = input("Enter takeoff time Enter in HH:MM format (24h): ")
    if (len(time) == 5 and time[2] == ":" and
            time[0].isdigit() and time[1].isdigit() and
            time[3].isdigit() and time[4].isdigit()):

        hours_str, minutes_str = time.split(":")
        hours = int(hours_str)
        minutes = int(minutes_str)

        if 0 <= hours <= 23 and 0 <= minutes <= 59:
            while True:
                try:
                    flight_time = int(input("Enter flight duration in minutes: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a whole number.")
            break
        else:
            print("Invalid time range! Hours must be 0–23, minutes 0–59.")
    else:
        print("Wrong format! Please use HH:MM.")

total_minutes = (hours * 60) + minutes + flight_time
hours_after = int((total_minutes / 60) % 24)
minutes_after = total_minutes % 60

print(f"Santa will land at {hours_after:02d}:{minutes_after:02d}")





