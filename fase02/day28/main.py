import time

import schedule


def _task():
    print("⏰¡La tarea ha sido ejecutada!")


hour = "08:00"
schedule.every().day.at(hour).do(_task)

print("Esperando que llegue la hora programada...")

while True:
    schedule.run_pending()
    time.sleep(60)
