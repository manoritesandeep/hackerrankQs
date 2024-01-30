"""
del vs drop()
In Python, the del keyword is used to delete an object or a specific element from a collection.

you cannot pass a list of columns directly to the del keyword to delete multiple columns at once.
The del keyword is designed to delete a single object or element at a time.

However, you can achieve the desired result by using the drop() method in pandas.
The drop() method allows you to specify a list of columns that you want to remove from a dataframe.
"""