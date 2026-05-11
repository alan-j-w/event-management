import os
import django
import shutil
from datetime import date, timedelta

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventpr.settings')
django.setup()

from eventapp.models import Event

def populate():
    # Ensure media directory exists
    base_dir = os.path.dirname(os.path.abspath(__file__))
    media_pic_dir = os.path.join(base_dir, 'pic', 'pic')
    os.makedirs(media_pic_dir, exist_ok=True)

    # Delete old events to start fresh
    print("Cleaning up old events...")
    Event.objects.all().delete()

    # List of high-quality cultural and global events
    events_data = [
        {
            'name': 'Thrissur Pooram 2026',
            'desc': 'Experience the mother of all festivals in Kerala. A majestic pageant of 30 decorated elephants, traditional percussion (Panchavadyam), and an incredible display of colors and culture at the Vadakkunnathan Temple.',
            'location': 'Thrissur, Kerala',
            'date': date(2026, 4, 28),
            'img_abs_path': r'C:\Users\ALAN\.gemini\antigravity\brain\7b73a225-e5bc-4c0b-a2f3-3f9bb16626d7\thrissur_pooram_elephant_pageant_1778510468992.png',
            'img_name': 'pooram.png'
        },
        {
            'name': 'Nehru Trophy Boat Race',
            'desc': 'The famous Vallam Kali (Snake Boat Race) on the Punnamada Lake. Watch hundred-foot long boats carved out of wood, filled with 100 rowers, as they compete for the prestigious trophy in a high-octane atmosphere.',
            'location': 'Alappuzha, Kerala',
            'date': date(2026, 8, 12),
            'img_abs_path': r'C:\Users\ALAN\.gemini\antigravity\brain\7b73a225-e5bc-4c0b-a2f3-3f9bb16626d7\kerala_snake_boat_race_1778510491503.png',
            'img_name': 'boat_race.png'
        },
        {
            'name': 'Classical Kathakali Night',
            'desc': 'A mesmerizing performance of Kathakali, the classical dance-drama of Kerala. Witness the intricate makeup, grand costumes, and the powerful storytelling through mudras and expressions.',
            'location': 'Kalamandalam, Kerala',
            'date': date(2026, 6, 15),
            'img_abs_path': r'C:\Users\ALAN\.gemini\antigravity\brain\7b73a225-e5bc-4c0b-a2f3-3f9bb16626d7\kathakali_dance_performance_1778510514944.png',
            'img_name': 'kathakali.png'
        },
        {
            'name': 'Tomorrowland Global Fest',
            'desc': 'The world\'s most iconic electronic dance music festival comes to life. A fantasy-themed mainstage, world-class DJs, and a global audience celebrating unity and music under the stars.',
            'location': 'Boom, Belgium',
            'date': date(2026, 7, 20),
            'img_abs_path': r'C:\Users\ALAN\.gemini\antigravity\brain\7b73a225-e5bc-4c0b-a2f3-3f9bb16626d7\tomorrowland_music_festival_mainstage_1778510542032.png',
            'img_name': 'tomorrowland.png'
        },
        {
            'name': 'World Technology Summit',
            'desc': 'Bringing together the brightest minds in AI, Robotics, and Quantum Computing. A global platform for innovation, featuring keynote speeches from industry giants and hands-on tech workshops.',
            'location': 'Silicon Valley, USA',
            'date': date(2026, 11, 10),
            'img_abs_path': r'C:\Users\ALAN\.gemini\antigravity\brain\7b73a225-e5bc-4c0b-a2f3-3f9bb16626d7\global_tech_summit_keynote_1778510567181.png',
            'img_name': 'tech_summit.png'
        }
    ]

    print("Starting population...")
    for data in events_data:
        dest_img_path = os.path.join(media_pic_dir, data['img_name'])
        
        if os.path.exists(data['img_abs_path']):
            shutil.copy(data['img_abs_path'], dest_img_path)
            img_field_value = f"pic/{data['img_name']}"
        else:
            img_field_value = "pic/default.jpg"
            print(f"Warning: {data['img_abs_path']} not found")

        # Create event
        event = Event.objects.create(
            name=data['name'],
            desc=data['desc'],
            location=data['location'],
            date=data['date'],
            img=img_field_value
        )
        print(f"Created event: {data['name']}")

    print("Population complete! Your database is now updated with cultural and global events.")

if __name__ == '__main__':
    populate()
