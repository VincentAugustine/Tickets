Explaination
============

This is my first Python project, which is a crawler for the ticket information on the website -- 12306.com
----------------------------------------------------------------------------------------------------------

The whole project contains 2 parts:

*   basic function(finished√)
*   extended function


------------------------------------------------------------------------------------------

Technological Documentation
===========================

Third-party libraries used
--------------------------

### 

*   pprint from pprint
*   station from station
*   docopt from docopt
*   PrettyTable from prettytable
*   ini, Force form colorama

Steps
-----

### 

1.  Anakyze the website(request and response) using F12, and get the important information(request url,parameters) in the "headers", after that, in the "response", check the .json information, then copy it into your code, and you need to find out all the parameter information, and use ".format()" so that all the important parameters can be replaced by yourself. And you need to claim a varianle in order to get the response from the website, then you need to decode by using the method "r.json", next, you should put the parameters you found into variables. Following this, a split and filtration are needed to be done. As a result, till now, you have already picked up all the data you need and stored them all into a dictionary. P.S. A IO is needed to identify the name and the code of the city.(In the file station.py)
2.  When you have finished all the things above, it means that you have collected all the information, and then you need to coolect them and form a table
3.  First, you need to claim a class, which is for all the information. Then, add some properties and behaviors(method) to it. There are two properties - available trains and options, and then you need to claim them.After these, what you need to do is adding method to it.
4.  If all the steps above have been finished, some additions can be set -- color, table by using the "colorama" and "prettytable", so that your result can be more clear. Also, there are details like the time shown should be as clear as possible. In addition, you need to replace all the emtpy cell with "--"
5.  Following this, I added another function -- searching for the price. In order to do this, another analysis is needed. You need to crawl the package for asking for the price. Then, same as the steps above, it is needed to get the parameter and dictionary of price, then show it in the table you have made.
6.  After all these, your basic functions are completed.

Important points in the project
-------------------------------

### 

*   IO 
*   Use of the third party libraries 
*   Analysis of the requests and response in the website 
*   Use of class, property, method