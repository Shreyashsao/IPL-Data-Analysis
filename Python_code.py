#WEB SCRAPPING FOR IPL MATCH ANALYTICS

#importing webdriver, keys, by and options from selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time    #importing time for browser to get sleep within specific time
import pandas as pd  #pandas will be helpful to create dataframe to get exported to csv


#creating empty array list as per the data description
s = []
mn = []
v = []
dt=[]
mw=[]
ft=[]
st=[]
lnk=[]

#Selecting driver as chrome
driver = webdriver.Chrome()

#We have to scrap data for all the seasons so applying loop in the url link to acess all the seasons from 2008 till 2023
for i in range(2008,2024,1):
    #selecting ipl browser url and using f string to navigate through different ipl seasons
    driver.get(f'https://www.iplt20.com/matches/results/{i}')     #
    time.sleep(1)

    #scrapping the webpage using xpath in Selenium
    session = driver.find_element('xpath', "//div[@class='col-lg-2 col-md-2 col-sm-6'][3]/div/div[@class='cSBDisplay ng-binding']")
    match_no= driver.find_elements('xpath',"//div[@class='vn-schedule-head']/div/span[@class='vn-matchOrder ng-binding ng-scope']")
    venue=driver.find_elements("xpath", "//div[@class='w50 fl']/span/p")
    date_time= driver.find_elements("xpath", "//div[@class='w50 fl']/div")
    match_won=driver.find_elements("xpath","//div[@class=' w20 tl pr50']/div")
    first_team=driver.find_elements("xpath","//div[@class='vn-shedTeam']")
    second_team=driver.find_elements("xpath","//div[@class='vn-shedTeam vn-team-2']")
    link=driver.find_elements("xpath","//div[@class='vn-ticnbtn']/a")

    #applying nested loop to extract elements of the above data lists
    for j in range(59):
        s.append(session.text)    #session will be same for webpage and will change according to the navigated webpage

        #using try except to handle exceptions if needed
        #appending the extracted elements to the empty array lists respectively
        try:
            mn.append(match_no[j].text)

        except Exception:
            mn.append("unavailable")

        try:
            v.append(venue[j].text)
        except Exception:
            v.append("unavailable")

        try:
            dt.append(date_time[j].text)
        except Exception:
            dt.append("unavailable")

        try:
            mw.append(match_won[j].text)
        except Exception:
            mw.append("unavailable")

        try:
            ft.append(first_team[j].text)
        except Exception:
            ft.append("unavailable")

        try:
            st.append(second_team[j].text)
        except Exception:
            st.append("unavailable")

        try:
            lnk.append(link[j].get_attribute('href'))
        except Exception:
            lnk.append("unavailable")

#printing the appended lists and their lengths for reference
print(len(s),s)
print(len(mn),mn)
print(len(v), v)
print(len(dt), dt)
print(len(mw), mw)
print(len(ft),ft)
print(len(st),st)
print(len(lnk),lnk)

#creating a dictionary as variable 'd'
d={'Season_year':s, 'Match_number':mn, 'Venue':v, 'Date&Time':dt, 'Winning team': mw, 'First team': ft, 'Second team':st, 'link':lnk}

#creating a dataframe using pandas
df=pd.DataFrame(d)
print(df)

#finaly converting dataframe into dataset of csv format for further data analysis.
df.to_csv("ipl_scrap_dataset.csv",index=False)
