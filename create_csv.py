import csv

def write_csv():
    with open("sample_data.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                "habit_name",
                "category",
                "duration",
                "date_created",
                "last_date_checked",
                "streak",
                "status",
            ]
        )
        writer.writerow(
            [
                "Make the bed",
                "Housework",
                "Weekly",
                "2023-09-01 11:10:00",
                "2023-10-05 15:10:00",
                "10",
                1,
            ]
        )
        writer.writerow(
            [
                "Finish assignment",
                "Work",
                "Weekly",
                "2023-08-20 19:10:00",
                "2023-09-20 12:10:00",
                "28",
                1,
            ]
        )
        writer.writerow(
            [
                "Take notes",
                "University",
                "Daily",
                "2023-07-10 17:10:00",
                "2023-10-04 12:10:00",
                "10",
                1,
            ]
        )
        writer.writerow(
            [
                "Read book",
                "Freetime",
                "Daily",
                "2023-07-23 13:10:00",
                "2023-10-05 11:10:00",
                "22",
                1,
            ]
        )
        writer.writerow(
            [
                "Take dance lesson",
                "Selfcare",
                "Weekly",
                "2023-09-03 13:10:00",
                "2023-10-04 11:10:00",
                "4",
                1,
            ]
        )