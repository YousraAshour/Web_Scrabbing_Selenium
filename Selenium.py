from selenium import webdriver
import csv
# driver = webdriver.Chrome("Y:\ITI\Data Preparation\chromedriver.exe")
# driver.get('https://www.amazon.com/s?i=specialty-aps&bbn=16225009011&rh=n%3A%2116225009011%2Cn%3A281407&ref=nav_em__nav_desktop_sa_intl_accessories_and_supplies_0_2_5_2')
# products= driver.find_elements_by_xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']")
# prices= driver.find_elements_by_xpath("//a[@class='a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")

driver=webdriver.Chrome("Y:\ITI\Data Preparation\chromedriver.exe")
driver.get('https://www.amazon.eg/s?k=samsung&rh=p_89%3Asamsung&language=en&ref=SQEG-WEB-SR301')

products = driver.find_elements_by_xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']")
prices = driver.find_elements_by_xpath("//span[@class='a-price-whole']")

for i in products:
    print(i.text)

for i in prices:
    print(i.text)

print(len(products))
print(len(prices))


with open('Y:\ITI\Amazon_products.csv', 'w', encoding='utf-8', newline='') as csvfile:
    csvwriter= csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['المنتجات', 'Price'])
    if len(products) <= len(prices) :

        for i in range(0,len(products)):
            csvwriter.writerow([products[i].text, prices[i].text])
        for i in range(len(products),len(prices)):
            csvwriter.writerow(["NULL", prices[i].text])

    else :
        for i in range(0,len(prices)):
            csvwriter.writerow([products[i].text, prices[i].text])
        for i in range(len(prices),len(products)):
            csvwriter.writerow([products[i].text,"NULL"])



driver.close()