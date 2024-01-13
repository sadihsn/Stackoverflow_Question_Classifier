from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

columns = ["Question", "Summary", "Tags", "Username"]

def get_question_details(row):
    details = row.text.split('\n')
    contents = {}

    try:
        contents["Question"] = details[6]
        contents["Summary"] = details[7]

        # Extract tags into a list
        tag_elements = row.find_elements(By.CLASS_NAME, "post-tag")
        tags = [tag.text for tag in tag_elements]  # Store as a list
        contents["Tags"] = tags

        contents["Username"] = details[9]
    except IndexError as e:
        print(f"Error extracting details: {e}")
    
    return contents

def main():
    webdriver_path = "/Users/sadihossain/Desktop/chromedriver-mac-arm64/chromedriver"  # Replace with your actual path
    question_data = []

    for page_id in range(1,2000):
        service = ChromeService(executable_path=webdriver_path)
        driver = webdriver.Chrome(service=service)
        url = f"https://stackoverflow.com/questions?tab=newest&page={page_id}"
        driver.get(url)

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'questions')))
            question = driver.find_element(By.ID, 'questions')
            rows = question.find_elements(By.CLASS_NAME, 's-post-summary.js-post-summary')
            
            for row in rows:
                question_data.append(get_question_details(row))
        except TimeoutException:
            print(f"Timed out waiting for 'questions' element on page {page_id}")

        driver.close()

    df = pd.DataFrame(data=question_data, columns=columns)
    df.to_csv("Stack_Overflow_data.csv", index=False)

    print(len(question_data))

if __name__ == "__main__":
    main()
