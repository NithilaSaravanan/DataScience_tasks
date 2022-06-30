
(base) nithila@ip-172-31-57-162:~/projects/homework_4$ vim nyc_dash/main.py 
(base) nithila@ip-172-31-57-162:~/projects/homework_4$ bokeh serve --address='*' --port=8080 --allow-websocket-origin=100.25.177.227:8080 --auth=auth.py nyc_dash
2020-10-13 03:28:47,508 Starting Bokeh server version 2.2.1 (running on Tornado 6.0.4)
2020-10-13 03:28:47,509 User authentication hooks provided (no default user)
2020-10-13 03:28:47,512 Bokeh app running at: http://*:8080/nyc_dash
2020-10-13 03:28:47,512 Starting Bokeh server with process id: 1764
2020-10-13 03:28:50,872 WebSocket connection opened
2020-10-13 03:28:50,873 ServerConnection created
^C
Interrupted, shutting down
(base) nithila@ip-172-31-57-162:~/projects/homework_4$ vim nyc_dash/main.py 

from bokeh.plotting import figure, curdoc
from bokeh.models import Select, ColumnDataSource,CustomJS
from bokeh.layouts import column
import pandas as pd
import os

#Loading the dataset
df1 = pd.read_csv(os.path.join(os.path.dirname(__file__), "df1.csv"))#df1 is the zip, month, average level data
df2 = pd.read_csv(os.path.join(os.path.dirname(__file__),"df2.csv"))#df2 is the month and average level data
df1 = df1[df1['zip']!=83]
options = list(df1.zip.unique())
options = [str(x) for x in options]

source11 = ColumnDataSource(df1[df1.zip == int(options[0])])
source12 = ColumnDataSource(df1[df1.zip == int(options[1])])
source2 = ColumnDataSource(df2)



#Drop downs
select1 = Select(title="Select first zipcode (zip 1)", value=options[0], options=options)
select2 = Select(title="Select second zipcode (zip 2)", value=options[1], options=options)


def change1(attr,old,new):
    zip1 =int(new)
    zip1df = ColumnDataSource(df1[df1.zip == zip1])
    source11.data = dict(zip1df.data)

def change2(attr,old,new):
    zip2 = int(new)
    zip2df = ColumnDataSource(df1[df1.zip ==zip2])
    source12.data = dict (zip2df.data)

#zip1 = change1()
#zip2 = change2()


#Plotting
p =figure(plot_height = 650 ,plot_width = 1000, title="Comparing average response times for 311 complaints across zipcodes in NYC")

p.line(x='month', y='hours', line_width=2,line_dash="4 4",color='black', source=source2,line_cap='round', legend_label=' across all zips')
p.line(x='month', y='hours', line_width=2,color='green', source=source11,line_cap ='round', legend_label=' for zip 1')
p.line(x='month', y='hours', line_width=2,color='orange', source=source12,line_cap='round', legend_label=' for zip 2')


#Formatting
p.title.text_font_size = "20px"
p.xaxis.ticker = [1,2,3,4,5,6,7,8,9,10,11,12]
p.legend.location = "top_right"
p.legend.title = 'Average reponse time'
p.legend.title_text_font_style = "bold"
p.legend.title_text_font_size = "12px"
p.background_fill_color = "gray"
p.background_fill_alpha = 0.1
p.outline_line_width = 1
p.outline_line_alpha = 1
p.outline_line_color = "black"

p.yaxis.axis_label = "Average Response Time (in Hours)"
p.xaxis.axis_label = "Months (2020)"

"nyc_dash/main.py" 67L, 2205C                                                                                                                                                           1,1           Top
