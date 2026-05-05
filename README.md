# Economic Indicators Tracker - India

A Python web scraper and analyzer for Indian economic indicators from the Reserve Bank of India (RBI).

## Project Overview

This project scrapes and analyzes key RBI economic data including:
- **Repo Rate** (RBI's benchmark interest rate)
- **CRR (Cash Reserve Ratio)**
- **SLR (Statutory Liquidity Ratio)**
- **Inflation Data**
- **Foreign Exchange Reserves**
- **Monetary Policy Updates**

## Features (Planned)

- [ ] Scrape RBI official data
- [ ] Store data in CSV/database
- [ ] Analyze trends over time
- [ ] Visualize indicators with charts
- [ ] Track policy changes

## Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/sangone7/econ-ind-tracker.git
cd econ-ind-tracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the scraper:
```bash
python scraper.py
```

## Project Structure

```
econ-ind-tracker/
├── scraper.py           # Main scraping script
├── analyzer.py          # Data analysis functions
├── requirements.txt     # Python dependencies
├── data/               # Folder for storing scraped data
│   └── rbi_data.csv
└── README.md           # This file
```

## Learning Goals

As an economics student learning to code, this project will help you:
- Learn web scraping with Python
- Work with APIs and data
- Understand data manipulation
- Create visualizations
- Apply economic concepts programmatically

## Resources

- [RBI Official Website](https://www.rbi.org.in/)
- [RBI Monetary Policy](https://www.rbi.org.in/web/rbi/monetary-policy)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/)
- [Python Requests Library](https://requests.readthedocs.io/)

## Contributing

This is a personal learning project. Feel free to modify and expand it!

## License

MIT License - feel free to use this for your learning.
