from selenium import webdriver
import csv


driver= webdriver.Chrome('Y:\ITI\Data Preparation\chromedriver.exe')
driver.get('https://www.sos.ca.gov/state-holidays')

Date=driver.find_elements_by_xpath("//tbody/tr/td[1]")
Holiday=driver.find_elements_by_xpath("//tbody/tr/td[2]")

# print(len(Date))
# print(len(Holiday))

# for i in Date:
#     print(i.text)
#
# for i in Holiday:
#     print(i.text)

with open('Y:\ITI\Holidays.csv', 'w+', newline='') as csvfile:
    csvwriter=csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Date','Holiday'])
    for i in range(0,len(Holiday)):
        csvwriter.writerow([Date[i].text,Holiday[i].text])

driver.close()