# Poker Ranking

Dynamic ranking graph for family poker games

## How to Use

1. Download most recent weekly points data from [here](https://docs.google.com/spreadsheets/d/1ZUaSyorHHX9ci0DR-rGFN5yJTStb6uxLbUk5eMtkY4A/edit?usp=sharing) and save it as `poker_points.csv`. Make sure date is in yyyy-mm-dd format.

2. Run the Python script to create weekly ranking data (`rank.csv`). You need to have `pandas` installed in the Python environment.
    > python process_data.py

3. Open the Sandbox [project](https://codesandbox.io/s/poker-ranking-ybzvi7), it should automatically create a project copy for you.

4. Copy contents in `rank.csv` to replace those in `test.csv` in Sandbox.

5. Save changes, the video demo should auto-refresh.

## References

Original GitHub project [repo](https://github.com/Jannchie/Historical-ranking-data-visualization-based-on-d3.js).
