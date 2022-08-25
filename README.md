# UFC Data Science Project

This project is a composite tool that contains:
* A scraper and retriver of UFC data from [the UFC stats archive](http://ufcstats.com/) and the [MMA decisions archive](http://www.mmadecisions.com). Periodically uploads all data into a PostGres SQL warehouse.
* A Python package to easily query the warehouse for specific datasets and support projects involving UFC data.
* An example showcasing a [classification neural network]() that predicts fight outcomes based on actions taken by fighters.

## Installation

Install the `ufcdata` package in the `root\code` directory.

## Requirements

All requirements are captured in the [`requirements.txt`]() file in the root directory.

## Usage

Once the PostGres warehouse has been setup, the server can be queried as with the following example:

```python
from ufcdata.query import DatabaseQuery
from ufcdata.tools import query_to_df

# Query for all round scores with a KO

query = DQ.engine.execute('SELECT * from rounds')
df_all_rounds = query_to_df(query)

df_fights_finished = df_all_fights.loc[(df_all_fights['method'].str.contains('KO'))

```

