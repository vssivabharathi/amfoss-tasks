import discord
from dotenv import load_dotenv
import os
from datetime import datetime
import csv
import requests
from bs4 import BeautifulSoup

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')

ESPN_URL = 'https://www.espncricinfo.com/live-cricket-score'

intents = discord.Intents.all()
client = discord.Client(intents=intents)


help_message = """
**Cricket Bot Commands:**
- `/livescore`: Generate live cricket score and append it to the CSV file.
- `/generate`: Display match history in CSV format.
- `/help`: Display this help message.
- `/behind_the_screen`: Thsi will allows you to downlaod the README file **ONLY FOR DEVELOPERS**

developed by Sivabharathi :)
"""
#scraping...
def fetch_live_score():
    try:
        response = requests.get(ESPN_URL)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        team1_name = soup.find_all(class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1')[0].text.strip()
        team2_name = soup.find_all(class_='ds-flex ds-items-center ds-min-w-0 ds-mr-1')[1].text.strip()
        match_info = soup.find(class_='ds-text-tight-xs ds-truncate ds-text-typo-mid3').text.strip()
        match_status = soup.find(class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo').text.strip()
        
        live_score_info = f"**Team_A:** {team1_name}\n" \
                          f"**Team_B:** {team2_name}\n"  \
                          f"**About_match:** {match_info}\n" \
                          f"**Status:** {match_status}\n" \

        return live_score_info
    except Exception as e:
        return str(e)


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/livescore'):
        live_score_info = fetch_live_score()

        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        live_score_with_time = f"{timestamp}:\n" + live_score_info
                          
        live_score_with_timestamp = f"{live_score_with_time}"
        append_to_csv(live_score_with_timestamp)

        await message.channel.send(live_score_info)

  

    elif message.content.startswith('/generate'):
        if "/generate" in message.content.lower():
        
            match_history = fetch_match_history()
            await message.channel.send(file=discord.File('match_history.csv'))

    elif message.content.startswith('/help'):
        await message.channel.send(help_message)

    elif message.content.startswith('/behind_the_screen'):
        if "/behind_the_screen" in message.content.lower():
            
            await message.channel.send(readme_path)
readme_path = '''click this link Note: ONLY FOR DEVELOPERS ' https://github.com/vssivabharathi/amfoss-tasks/blob/main/task-06/README.md'''
def fetch_match_history():
    try:
        with open('match_history.csv', 'r') as file:
            lines = file.readlines()
        return ''.join(lines)
    except FileNotFoundError:
        return "No match history available."

def append_to_csv(data):
    with open('match_history.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data])

if __name__ == '__main__':
    client.run(bot_token)


if __name__=='main':
    live_score = fetch_live_score()
    if live_score.startswith("**Match:"):
        print(live_score)
    else:
        print("No live score available! Try again later.")

