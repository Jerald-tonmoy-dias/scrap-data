# Baseball Stats Scraper

A practice web scraping project that extracts baseball game statistics from an HTML page using BeautifulSoup and saves the data as a CSV file.

## How it works

1. **Fetch** — Downloads `baseball_stats.html` from a local HTTP server using `requests`.
2. **Parse** — Uses BeautifulSoup to find the `<tbody>` and iterate through each `<tr>` row.
3. **Extract** — Pulls `game_id`, team names, expected runs, over/under, and moneyline favorite from the `<td>` cells into a list of dictionaries.
4. **DataFrame** — Converts the structured data into a pandas DataFrame for easy manipulation.
5. **Export** — Saves the cleaned data to `sports_statistics.csv`.

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `pandas`

Install with:

```bash
pip install requests beautifulsoup4 pandas
```

## Usage

```bash
python main.py
```

The script prints the HTML, the DataFrame, and its shape, then writes `sports_statistics.csv`.

## Output

| GameID | Team 1 | Team 2 | Expected Runs (Team 1) | Expected Runs (Team 2) | Over/Under | Moneyline Favorite |
|--------|--------|--------|------------------------|------------------------|------------|-------------------|
| 1 | Chicago Firebirds | San Francisco Waves | 4.5 | 3.8 | 8.5 | Chicago Firebirds |
| 2 | New York Knights | Miami Sharks | 5.2 | 4.1 | 9.0 | New York Knights |
| ... | ... | ... | ... | ... | ... | ... |
