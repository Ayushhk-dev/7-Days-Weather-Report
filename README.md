<div align="center">

# 🌦️ Weather Forecasting

**Type a city. Get the last week's temperatures as a table, a chart, and a CSV.**

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-data-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-charts-11557c)
![API](https://img.shields.io/badge/Open--Meteo-no%20API%20key-2ea44f)

</div>

---

## ✨ Features

- 🔎 **City search**: enter any city name and it is converted to latitude and longitude automatically
- 🌡️ **Past 7 days of weather**: daily max and min temperature in °C
- 📊 **Graphs and charts**: a clean line chart of max vs. min temperature, saved as a PNG
- 📁 **CSV export**: the data is saved as a `.csv` file you can open in Excel or reuse elsewhere
- 🔑 **No API key needed**: uses the free [Open-Meteo](https://open-meteo.com/) APIs

---

## 📸 Examples

<table>
  <tr>
    <th align="center">Delhi</th>
    <th align="center">Mumbai</th>
  </tr>
  <tr>
    <td><img src="Delhi_chart.png" alt="Delhi temperature chart" width="100%"></td>
    <td><img src="Mumbai_chart.png" alt="Mumbai temperature chart" width="100%"></td>
  </tr>
  <tr>
    <td align="center"><a href="data/Delhi_weather.csv">📄 Delhi_weather.csv</a></td>
    <td align="center"><a href="data/Mumbai_weather.csv">📄 Mumbai_weather.csv</a></td>
  </tr>
</table>

**Sample output:**

<table>
  <tr>
    <th align="center">Delhi</th>
    <th align="center">Mumbai</th>
  </tr>
  <tr>
    <td valign="top">
      <table>
        <tr><th>date</th><th>max_temp</th><th>min_temp</th></tr>
        <tr><td>2026-10-13</td><td>32.3</td><td>23.4</td></tr>
        <tr><td>2026-10-14</td><td>32.5</td><td>23.7</td></tr>
        <tr><td>2026-10-15</td><td>25.4</td><td>19.7</td></tr>
        <tr><td>2026-10-16</td><td>28.6</td><td>20.5</td></tr>
        <tr><td>2026-10-17</td><td>29.4</td><td>20.8</td></tr>
        <tr><td>2026-10-18</td><td>29.5</td><td>20.1</td></tr>
        <tr><td>2026-10-19</td><td>29.8</td><td>19.8</td></tr>
        <tr><td>2026-10-20</td><td>29.8</td><td>19.7</td></tr>
      </table>
    </td>
    <td valign="top">
      <table>
        <tr><th>date</th><th>max_temp</th><th>min_temp</th></tr>
        <tr><td>2026-10-13</td><td>38.2</td><td>27.4</td></tr>
        <tr><td>2026-10-14</td><td>37.6</td><td>27.3</td></tr>
        <tr><td>2026-10-15</td><td>37.6</td><td>27.6</td></tr>
        <tr><td>2026-10-16</td><td>37.1</td><td>26.9</td></tr>
        <tr><td>2026-10-17</td><td>36.1</td><td>27.0</td></tr>
        <tr><td>2026-10-18</td><td>35.7</td><td>27.2</td></tr>
        <tr><td>2026-10-19</td><td>36.7</td><td>27.1</td></tr>
        <tr><td>2026-10-20</td><td>35.2</td><td>27.5</td></tr>
      </table>
    </td>
  </tr>
</table>

---

## 🚀 Getting Started

**1. Clone the repo**

```bash
git clone https://github.com/<your-username>/weather-forecasting.git
cd weather-forecasting
```

**2. Install the libraries**

```bash
pip install requests pandas matplotlib
```

**3. Run it**

```bash
python weather.py
```

Then type a city name when asked:

```
Enter city name: Delhi
```

---

## 📂 What You Get

After each run, the script creates:

```
weather-forecasting/
├── weather.py
├── <city>_chart.png        # temperature chart
└── data/
    └── <city>_weather.csv  # date, max_temp, min_temp
```

---

## 🛠️ How It Works

1. Takes the city name you type
2. Looks up its coordinates with the Open-Meteo Geocoding API
3. Fetches daily max/min temperatures for the past week from the Open-Meteo Weather API
4. Builds a Pandas DataFrame, plots it with Matplotlib, and saves the chart and CSV

---

## 📝 Notes

- If a city name is shared by several places (e.g. Paris), the top search match is used.
- If the city isn't found, the script prints a message and exits.

---

<div align="center">

Made with Python 🐍 · Weather data by [Open-Meteo](https://open-meteo.com/)

</div>
