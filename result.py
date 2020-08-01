def take_input():
    from datetime import datetime
    enter_clientname=input('Enter your client name: ')
    enter_projecttitle=input('Enter your project title: ')
    enter_start_date=input('Enter your datetime yy-mm-dd H:M: ')
    end_time = datetime.now()
    format="%Y-%m-%d %H:%M"
    start_time= datetime.strptime(enter_start_date,format)
    end_time = datetime.now()
    return enter_clientname,enter_projecttitle,start_time,end_time


def working_hours():
    global client_name
    global project_name
    client_name, project_name,start_datetime,end_datetime = take_input()
    working_hours_difference = end_datetime-start_datetime
    work_hours = working_hours_difference.total_seconds()/60**2
    return work_hours

work_hours=working_hours()
def calculate_wages():
    from decimal import Decimal
    #work_hours=working_hours()
    money_per_hour = Decimal('5.0')
    wages_earn = Decimal(work_hours) * money_per_hour
    final_wages = ('%.2f'%wages_earn)
    return final_wages
wage_earn=calculate_wages()
print(f'you have worked for {work_hours} hours and wages earn is ${wage_earn}')

def save_to_csv():
    import pandas as pd
    tracker_data = {'client':[client_name],
           'project title':[project_name],
           'work hours':[work_hours],
           'wage $':[wage_earn]}
    dataset=pd.DataFrame(tracker_data,columns=['client','project title','work hours','wage $'])
    #print(dataset)
    dataset.to_csv('timetracking.csv',sep='\t', header=None, mode='a')
    return dataset
print(save_to_csv())
