import os
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE','learning_templates.settings')

import django
django.setup()

#fake population script

from basic_app.models import Hit



def import_data():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    temp=os.path.join(BASE_DIR,'learning_templates')
    path=os.path.join(temp,'data')
    os.chdir(path) # changes the directory
    
    with open('batting_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = Hit(date=row['date'],
                gamepk=row['gamepk'],
                hometeamid=row['hometeamid'],
                hometeamname=row['hometeamname'],
                awayteamid=row['awayteamid'],
                awayteamname=row['awayteamname'],
                parkid=row['parkid'],
                park=row['park'],
                batterid=row['batterid'],
                battername=row['battername'],
                batside=row['batside'],
                batterteamid=row['batterteamid'],
                pitcherid=row['pitcherid'],
                pitchername=row['pitchername'],
                pitcherteamid=row['pitcherteamid'],
                pitchside=row['pitchside'],
                balls=row['balls'],
                strikes=row['strikes'],
                result_type=row['result_type'],
                pitch_type=row['pitch_type'],
                pitch_speed=row['pitch_speed'],
                zone_location_x=row['zone_location_x'],
                zone_location_z=row['zone_location_z'],
                launch_speed=row['launch_speed'],
                launch_horiz_ang=row['launch_horiz_ang'],
                launch_vert_ang=row['launch_vert_ang'],
                landing_location_x=row['landing_location_x'],
                landing_location_y=row['landing_location_y'],
                hang_time=row['hang_time'])
            p.save()

if __name__ =='__main__':
    print("importing data!")
    import_data()
    print("import complete!")
