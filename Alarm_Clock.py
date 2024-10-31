import time
import winsound

# Function to set an alarm
def set_alarm():
    alarm_time = input("Enter the alarm time (HH:MM): ")
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake up!")
            winsound.Beep(1000, 1000)  # Beep for 1 second
            break

# Function to snooze the alarm
def snooze_alarm():
    snooze_time = 5  # Snooze for 5 minutes
    alarm_time = time.time() + snooze_time * 60
    while time.time() < alarm_time:
        pass
    print("Snooze time is over. Wake up!")
    winsound.Beep(1000, 1000)  # Beep for 1 second

# Function to stop the alarm
def stop_alarm():
    print("Alarm stopped")

# Main loop for the alarm clock
while True:
    print("Options:")
    print("Enter '1' to set an alarm")
    print("Enter '2' to snooze the alarm")
    print("Enter '3' to stop the alarm")
    print("Enter '4' to exit")

    choice = input(": ")

    if choice == '1':
        set_alarm()
    elif choice == '2':
        snooze_alarm()
    elif choice == '3':
        stop_alarm()
    elif choice == '4':
        break
    else:
        print("Invalid input. Please enter a valid option.")