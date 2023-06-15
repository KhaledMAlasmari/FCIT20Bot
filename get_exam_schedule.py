import requests
import pandas as pd


# this function will return json file that contain all the information of the schedule
def get_exam_schedule():

    response = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vRbuH_vaKHql1sWp6wBmDYKIqv2L6fNvV2d7v7bnP14FtaDZn3gkBl1xTjrCP061XwF1K8VmiiJSZdH/pubhtml?gid=0&single=true")


    tables = pd.read_html(response.text)

    desired_table = tables[0]


    ##desired_table.to_csv("./data/output.csv", index=False)
    df = tables[0]

    data_list = {}

   



    # I did add this becase the Schedule format is piece of shit 
    date = ''
    for i in range(3, len(df)):
        if not str.isnumeric(df.iloc[i,1]):
            date = df.iloc[i,1]

        data_list[df.iloc[i, 2]]=[str(df.iloc[i, 3]),df.iloc[i, 4],df.iloc[i, 5],date]
    
    print(data_list.get("CPIS-312"))
    return data_list


get_exam_schedule()