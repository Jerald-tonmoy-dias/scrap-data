# Step 3.1: Fetch HTML Content
# Please be careful to follow instructions on how to run the program; 
# the Run menu or right-click > Run options do not work in the simulated environment. 
# Ensure you have run the terminal command to install the correct libraries using pip.
# You must use the terminal window as directed in Step 3.
### YOUR CODE HERE ###
import requests
from bs4 import BeautifulSoup

# Fetch the webpage content
url = "http://127.0.0.1:5500/baseball_stats.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Print the HTML content to inspect
print(soup.prettify())
# Step 3.2: Extract the Required Data
rows = soup.find('tbody').find_all('tr')
game_data = []
for row in rows:
    cols = row.find_all('td')
    game_data.append({
        'game_id': int(cols[0].text),
        'team_1': cols[1].text,
        'team_2': cols[2].text,
        'expected_runs_team_1': float(cols[3].text),
        'expected_runs_team_2': float(cols[4].text),
        'over_under': float(cols[5].text),
        'moneyline_favorite': cols[6].text
    })

# Step 4.1: Convert to a DataFrame
import pandas as pd

df = pd.DataFrame(game_data)

print(df)
print(df.shape)

# Step 5.1: Save to a CSV File
# Save the DataFrame to a CSV file named sports_statistics.csv
### YOUR CODE HERE ###