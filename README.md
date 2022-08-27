# UFC Data Science Project

![TDA analysis of MLP Classification model](img/title.png)
*Pictured above - a TDA network of predicted fight outcomes based on the data retrieved using this tool. Refer to the project [notebook](https://github.com/neelgokhale/UFCData-Project/blob/master/code/ML_Model.ipynb).*

This project is a composite tool that contains:

### Python Package `ufcdata`

[`go to package ->`](https://github.com/neelgokhale/UFCData-Project/tree/master/code/ufcdata)

* A scraper and retriever of UFC data from [the UFC stats archive](http://ufcstats.com/) and the [MMA decisions archive](http://www.mmadecisions.com). Periodically uploads all data into a PostGres SQL warehouse.
* A Python package to easily query the warehouse for specific datasets and support projects involving UFC data.

### Classification Network

[`go to notebook ->`](https://github.com/neelgokhale/UFCData-Project/blob/master/code/ML_Model.ipynb)

An example showcasing a comparison of several classification neural networks that predict fight outcomes based on actions taken by fighters using the data sourced by `ufcdata`.

## Installation

Download the `ufcdata` package in the `root\code` directory.

## Requirements

All requirements are captured in the [`requirements.txt`](https://github.com/neelgokhale/UFCData-Project/blob/master/requirements.txt) file in the root directory.

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