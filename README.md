# lamdata-imdeja

## Installation

Installation is as simple as 
"pip install -i https://test.pypi.org/simple/ lamdata-deja==1.1" 
After installing you must import the function to you python environment. You can do this by simply typing: 
"from lamdata.deja import obj_lister, NaN_cleaning"

## Usage

This package comes with 2 functions. The first being "NaN_cleaner". This function takes in a dataframe and removes all rows with null values.
The 2nd function also takes in a dataframe. It it referred to as "obj_lister". This function will grab all columns with the "object" data type.