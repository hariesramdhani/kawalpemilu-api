import json
import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

def get_province_elements(driver):
    return driver.find_elements(By.CSS_SELECTOR, ".lokasi > .hierarchy")

def get_counts_elements(driver):
    return driver.find_elements(By.CSS_SELECTOR, "span.ng-star-inserted")

def parse_counts(counts):
    parsed_counts = []
    pattern = re.compile(".*<!---->.*")
    for count in counts:
        content = count.get_attribute('innerHTML')
        if pattern.match(content.strip()):
            parsed_counts.append(content.replace("<!---->", "").strip())
    return parsed_counts

def extract_data(provinces, counts):
    index = 0
    for province in provinces:
        provinces[province]["paslon_1_ratio"] = float(counts[index].replace("%", ""))
        provinces[province]["paslon_1_count"] = int(counts[index+1].replace(",", ""))
        provinces[province]["paslon_2_ratio"] = float(counts[index+2].replace("%", ""))
        provinces[province]["paslon_2_count"] = int(counts[index+3].replace(",", ""))
        provinces[province]["paslon_3_ratio"] = float(counts[index+4].replace("%", ""))
        provinces[province]["paslon_3_count"] = int(counts[index+5].replace(",", ""))
        provinces[province]["cakupan_ratio"] = float(counts[index+6].replace("%", ""))
        provinces[province]["cakupan_count"] = counts[index+7]
        provinces[province]["cakupan_jaga_ratio"] = float(counts[index+8].replace("%", ""))
        provinces[province]["cakupan_jaga_count"] = counts[index+9]
        index += 10

def main():
    driver = uc.Chrome(headless=True, use_subprocess=True)
    driver.get('https://kawalpemilu.org/h/')

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".lokasi > .hierarchy")))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.ng-star-inserted")))
        
        provinces = {}
        for element in get_province_elements(driver):
            content = element.get_attribute('text')
            if re.match("^[A-Za-z ]+$", content.strip()):
                provinces[content.strip()] = {}

        counts = parse_counts(get_counts_elements(driver))
        
        extract_data(provinces, counts)
        
        with open(f'../data/provinces_data.json', 'w') as json_file:
            json.dump({"data": provinces, "timestamp":time.time()}, json_file) 
        
    finally:
        driver.quit()

if __name__ == '__main__':
    main()