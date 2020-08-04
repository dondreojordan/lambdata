Delete .__init__.py.swp, and the setup.py that's in the folder lambdata_dondrejordan.
How you have it now is fine, but usually we only want to import in the __init__ so i would recommend moving all this code into another
py file within the same directory.
In the global scope(so not inside of functions) i see you have a variable column_names = X.columns.
X is never defined so i confused where this comes from.

I do like your clean_values function. My only suggestion there is to add a docstring so i know what's going on.
It is pretty straight forward though.

The clean_header function seems pretty useful.
I would maybe refrain from chaining so much, I know one liners are cool but readability > one liners. To be clear you can still chain just
don't do five in a row, hard to read.
I would use f-strings over the .format method in that function.

Your clean dataetime function seems good, again just docstring.
The only confusion is why did you return those columns, I think you mean to return the dataframe, I think X is a dataframe.

I think you can improve on your dog oop.

I'm gonna have to give it a 1 as is because the pip issues. But it's chill, you can easily fix it and we almost have so you'll for sure improve it.
