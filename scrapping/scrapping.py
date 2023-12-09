#
import re
import time
import pandas as pd

#
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService

#
usa_cities = pd.read_csv("../files/data/usa_cities.csv")
usa_states = pd.read_csv("../files/data/usa_states.csv")


# This function takes a state and the corresponding url and returns a list of dicts with each state's touristic attractions
def scrape_state_attractions(state: str, url: str, report=True) -> list:

    states_attractions = [] # to store data while scrapping
    failed_states = [] # to store errors while scrapping

    # Instanciate and configurate driver
    chrome_options = selenium.webdriver.chrome.options.Options()
    #chrome_options.add_argument('--headless') # unables GUI
    chrome_options.add_argument('--disable-infobars') # unables images loading
    driver = webdriver.Chrome(options=chrome_options)

    # Connect to url and wait to load
    driver.get(url)
    time.sleep(5)

    # Find amount of pages for the city
    try:
        for _ in range(10):
            # Find each attraction box
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.85);") # scroll to load page and buttons
            wait = WebDriverWait(driver, 10) # 
            attraction_divs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "jemSU"))) # find each attraction box

            for div in attraction_divs:
                try:
                    url = div.find_element(By.CLASS_NAME ,"BMQDV")
                    parts = div.text.split("\n")
                    if 15 > len(parts) > 2 and url:
                        if parts[0] == '2023':
                            del parts[0]
                            states_attractions.append({"state_id": usa_states[usa_states["state"] == state]["state_id"].iloc[0], "attraction": parts[0], "categories": parts[2], "reviews_url": url.get_attribute('href')})
                except:
                    pass

            next_page_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div/section[40]/div/div[1]/div/div[1]/div[2]')
            next_page_button.click()
            
    except:
        failed_states.append(state)
        if report:
            print(f"{state} state added to failed states.") # Console report

    # Close browser and return list with hotels data
    driver.quit()
    return states_attractions



# This function takes a state and the corresponding url and returns a list of dicts with each state's touristic attractions
def scrape_attractions_attribute(urls: str, report=True) -> list:
    
    attributes = [] # to store data while scrapping
    failed_urls = [] # to store errors while scrapping

    # Instanciate and configurate driver
    chrome_options = selenium.webdriver.chrome.options.Options()
    chrome_options.add_argument('--headless') # unables GUI
    chrome_options.add_argument('--disable-infobars') # unables images loading
    driver = webdriver.Chrome(options=chrome_options)

    for i, url in enumerate(urls):
        print(f'{i+1}/{len(urls)}')
        try:         
            # 
            driver.get(url)
            time.sleep(5)
            #
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.85);") # scroll to load page and buttons
            path_element = driver.find_element(By.CLASS_NAME, 'oPZZx')
            html = path_element.get_attribute("outerHTML")
            matches = re.search(r'center=([\d.-]+),([\d.-]+)', html)
            #
            if matches:
                attributes.append({"url": url, "latitud": matches.group(1), "longitude": matches.group(2)})
            else:
                attributes.append({"url": url, "latitud": matches.group(1), "longitude": matches.group(2)})
                
        except:
            attributes.append({"url": url, "latitud": None, "longitude": None})

    return attributes



# This function takes a list of cities and returns a dataframe with each hotel's data
def scrape_cities_hotels(cities: list, state: str, report=True, interfase=True) -> list:
    cities_hotels = [] # to store data while scrapping
    failed_cities = [] # to store errors while scrapping
    # Instanciate and configurate driver
    chrome_options = selenium.webdriver.chrome.options.Options()
    chrome_options.add_argument('--headless') if not interfase else None
    chrome_options.add_argument('--disable-infobars') # unables image loading
    driver = webdriver.Chrome(options=chrome_options)
    
    # Iterate over each city and scrape data into cities_hotels list
    for i, city in enumerate(cities):
        try:
            print(f'{i+1}/{len(cities)} - {city}')
            # Connect to url and wait to load
            counter = 0
            driver.get(f"https://www.booking.com/searchresults.es.html?ss={city}&ssne={city}&ssne_untouched={city}&label=bin859jc-1DCAMo7AE4mgNIClgDaAyIAQGYAQq4ARfIAQzYAQPoAQH4AQKIAgGoAgO4AtamjqsGwAIB0gIkNjY3NWU0MzUtZDQ2Yy00MGI3LWE3M2ItYzQ5YTQ3YmJhY2M52AIE4AIB&sid=867675c0a6ac4ae450c754b639211fc5&aid=357028&lang=es&sb=1&src_elem=sb&src=searchresults&dest_id={city}&dest_type=city&checkin=2024-05-12&checkout=2024-05-18&group_adults=2&no_rooms=1&group_children=0&offset={counter}")
            time.sleep(5)
            # WARNING this part is not working, the pop-up card must be closed manually
            #close pop-up card 
            #boton = driver.find_element(By.XPATH, '//*[@id="b2searchresultsPage"]/div[44]/div/div/div/div[1]/div[1]/div/button')
            #boton.click()
            # Find amount of pages for the city
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.85);") # scroll to load page and buttons
            pages = driver.find_elements(By.CLASS_NAME, "b16a89683f") # find list of pages
            n_pages = int(pages[len(pages)-2].text) # read last page button
            # Iterate over each page to scrape data
            for page in range(n_pages):
                # Find each hotel box
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.85);") # scroll to load page and buttons
                wait = WebDriverWait(driver, 10) # 
                hotel_divs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "c82435a4b8"))) # find each hotel box
                # Iterar over each box to scrape name, price, average score and url
                for div in hotel_divs: 
                    try:
                        # Find data
                        name_and_price_elements = div.find_elements(By.CLASS_NAME, "f6431b446c") # find name and price
                        url_element = div.find_element(By.CLASS_NAME, "a78ca197d0") # find url
                        score_element = div.find_element(By.CLASS_NAME, "a3b8729ab1") # find avg_score
                        # Store data in cities_hotels list
                        if len(name_and_price_elements) == 2 and url_element and score_element: 
                            name = name_and_price_elements[0].text
                            price = name_and_price_elements[1].text
                            url = url_element.get_attribute('href')
                            avg_score = score_element.text
                            #parts = n_reviews.text.split(" ")
                            cities_hotels.append({"state": state, "city": city,"name": name, "avg_score": avg_score, "price": price, "reviews_url": url})
                    except Exception as e:
                        pass
                if report:
                    print(f"    Pagina {page+1}/{n_pages} scrapped - {len(cities_hotels)} total hotels finded.") # Console report
                # Go to next page if not last page
                if page+1 < n_pages:
                    if page+1 == 2: # Handle error
                        counter += 25
                        driver.get(f"https://www.booking.com/searchresults.es.html?ss={city}&ssne={city}&ssne_untouched={city}&label=bin859jc-1DCAMo7AE4mgNIClgDaAyIAQGYAQq4ARfIAQzYAQPoAQH4AQKIAgGoAgO4AtamjqsGwAIB0gIkNjY3NWU0MzUtZDQ2Yy00MGI3LWE3M2ItYzQ5YTQ3YmJhY2M52AIE4AIB&sid=867675c0a6ac4ae450c754b639211fc5&aid=357028&lang=es&sb=1&src_elem=sb&src=searchresults&dest_id={city}&dest_type=city&checkin=2024-05-12&checkout=2024-05-18&group_adults=2&no_rooms=1&group_children=0&offset={counter}")
                    else: 
                        buttons = driver.find_elements(By.CLASS_NAME, "b16a89683f") # find list of pages
                        buttons[len(buttons)-1].click() # click last page button
        except Exception as e:
            failed_cities.append(city)
            print(f"{city} city added to failed cities.") if report else None
    
    # Transform
    cities_hotels = pd.DataFrame(cities_hotels)
    cities_hotels = cities_hotels.drop_duplicates(subset=['reviews_url'])
    # Process avg_score
    cities_hotels['avg_score'] = cities_hotels['avg_score'].replace(',', '.')
    cities_hotels['avg_score'] = cities_hotels['avg_score'].replace('[^\d.]', '', regex=True)
    cities_hotels['avg_score'] = pd.to_numeric(cities_hotels['avg_score'], errors='coerce')
    # Process price
    for i, row in cities_hotels.iterrows():
        price = row['price']
        price = price.replace('$', '')
        price = price.replace(' ', '')
        if price.count(".") == 1:
            cities_hotels.at[i, 'price'] = price
        elif price.count(".") == 2:
            first_dot_index = price.find('.')
            cities_hotels.at[i, 'price'] = price[:first_dot_index] + price[first_dot_index+1:]
        else:
            print(price)
    cities_hotels['price'] = pd.to_numeric(cities_hotels['price'], errors='coerce')
    
    # Close browser and return list with hotels data
    driver.quit()
    cities_hotels.to_csv(f"../files/data/booking/{state.lower()}_hotels.csv", index=False)
    return cities_hotels



def scrape_hotels_attributes(urls, ids, report=True):

    hotels_attributes = pd.DataFrame(columns=[
        "hotel_id", "direction", "description", "attributes", 
        "latitude", "longitude", "scores"
    ])

    # Instanciate and configurate driver
    chrome_options = selenium.webdriver.chrome.options.Options()
    chrome_options.add_argument('--headless') # unables GUI
    chrome_options.add_argument('--disable-infobars') # unables images loading
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')  # deshabilita carga de imágenes
    driver = webdriver.Chrome(options=chrome_options)
    
    for i in range(len(urls)):

        print(f"{i+1}/{len(urls)}")
        driver.get(urls[i])

        try: # Obtener dirección
            direccion_element = driver.find_element(By.CLASS_NAME, "hp_address_subtitle")
            direccion_texto = direccion_element.text
        except Exception as e:
            print(f"Error obteniendo dirección para el hotel con ID {ids[i]}: {str(e)}")
            direccion_texto = None

        try: # Obtener descripción
            descripcion_element = driver.find_element(By.CLASS_NAME, "b3efd73f69")
            descripcion_texto = descripcion_element.text
        except Exception as e:
            print(f"Error obteniendo descripción para el hotel con ID {ids[i]}: {str(e)}")
            descripcion_texto = None

        try: # Obtener atributos (limitado a 10)
            list_items = driver.find_elements(By.CLASS_NAME, "a8b57ad3ff")[:10]
            attributes_set = set()  # Usamos un conjunto para evitar duplicados
            for li in list_items:
                attribute = li.text
                if attribute not in attributes_set:
                    attributes_set.add(attribute)
            attributes_list = list(attributes_set)  # Convertir el conjunto a lista
        except Exception as e:
            print(f"Error obteniendo atributos para el hotel con ID {ids[i]}: {str(e)}")
            attributes_list = None

        try: # Obtener latitud y longitud
            map_element = driver.find_element(By.ID, 'hotel_sidebar_static_map')
            lat_lng_attribute = map_element.get_attribute('data-atlas-latlng')
            lat, lng = map(float, lat_lng_attribute.split(','))
        except Exception as e:
            print(f"Error obteniendo latitud y longitud para el hotel con ID {ids[i]}: {str(e)}")
            lat, lng = None, None

        score_list = []
        try: # Scores
            scores = driver.find_elements(By.CLASS_NAME, 'b817090550')
            for score_element in scores:
                score = score_element.text
                score = score.replace(",", ".")
                parts = score.split("\n")
                if len(parts) == 2:
                    score_list.append({f"{parts[0]}": parts[1]})
        except Exception as e:
            print(f"Error {type(e).__name__} obteniendo scores para el hotel con ID {ids[i]}")
            score_list = None
        
        # Create dataframe to concat
        attributes = pd.DataFrame({
            "hotel_id": [ids[i]],
            "direction": [direccion_texto],
            "description": [descripcion_texto],
            "attributes": [attributes_list],
            "latitude": [lat],
            "longitude": [lng],
            "scores": [score_list]})
        hotels_attributes = pd.concat([hotels_attributes, attributes], ignore_index=True, sort=False)

    driver.quit()
    return hotels_attributes



# This function takes a list of hotel's urls and returns a panads dataframe with all the reviews
def scrape_hotels_reviews(ids: list, urls: list, report=True, interfase=False) -> list:
    
    hotel_reviews = pd.DataFrame(columns=["nationality", "acommodation", "stay", "company", "review_title", "good_review", "bad_review", "url"])

    chrome_options = selenium.webdriver.chrome.options.Options()
    chrome_options.add_argument('--headless') if not interfase else None
    chrome_options.add_argument('--disable-infobars') # disables image loading
    driver = webdriver.Chrome(options=chrome_options) 

    for i in range(len(urls)):

        driver.get(urls[i]) # acces to url
        time.sleep(5) # wait to load
        
        try:
            # Open reviews section with retry
            attempts = 0
            while attempts <= 5:
                try:
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.45);")
                    buttons = driver.find_elements(By.CLASS_NAME, 'a83ed08757')
                    for b in buttons:
                        if b.text == "Leer todos los comentarios":
                            b.click()
                            attempts = 5
                except Exception as e:
                    print("Error clicking the button to open the reviews section. Retrying...")
                    driver.get(urls[i])
                    time.sleep(1)
                    attempts += 1

            # Find the amount of pages
            attempts = 0
            while attempts <= 5:
                try:
                    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "c-pagination")))
                    pagination = driver.find_element(By.CLASS_NAME, "c-pagination")
                    pages = pagination.find_elements(By.CLASS_NAME, "bui-pagination__item")
                    n_pages = int(pages[-2].text) if pages else 1
                    print(f"Number of pages: {n_pages}") if report else None
                    attempts = 5
                except Exception as e:
                    print("Error finding the number of pages. Retrying...")
                    time.sleep(1)
                    attempts += 1
                    
        except Exception as e:
            print(f"Error while opening the reviews section and finding the number of pages: {e}")
            n_pages = 2  # Set a default value in case of failure

        for page in range(n_pages):
            time.sleep(2)
            review_list = driver.find_element(By.CLASS_NAME, 'review_list')
            review_blocks = review_list.find_elements(By.CLASS_NAME, 'review_list_new_item_block')
            for block in review_blocks:

                try: # obtein user information
                    user_information_element = block.find_elements(By.CLASS_NAME, "bui-list__item")
                    if len(user_information_element) == 3:
                        acommodation = user_information_element[0].text
                        print(acommodation) if report else None
                        try:
                            stay, date = user_information_element[1].text.split(' ·  ')
                            print(stay) if report else None
                            print(date) if report else None
                        except Exception as e:
                            stay = None
                            date = None
                        company = user_information_element[2].text
                        print(company) if report else None
                    elif len(user_information_element) == 2:
                        try:
                            stay, date = user_information_element[0].text.split(' ·  ')
                            print(stay) if report else None
                            print(date) if report else None
                        except Exception as e:
                            stay = None
                            date = None
                        company = user_information_element[1].text
                        print(company) if report else None
                    else:
                        acommodation = None
                        stay = None
                        date = None
                        company = None
                        print(f"ERROR WHILE SCRAPPING USER INFORMATION: {len(user_information_element)} elements founded, excepction must be handled")
                        for element in user_information_element:
                            print(element.text)
                        print("-------------------------------------------------------------------------------------------------------------------")
                except Exception as e:
                    acommodation = None
                    stay = None
                    date = None
                    company = None
                    print(f"ERROR: WHILE SCRAPING USER INFORMATION - {type(e).__name__}: {e}")

                try: # obtein user nationality
                    nationality_element = block.find_elements(By.CLASS_NAME, "bui-avatar-block__subtitle")
                    nationality = nationality_element[0].text
                    print(nationality) if report else None
                except Exception as e: 
                    nationality =  None
                    print("ERROR: WHILE SCRAPPING USER NATIONALITY")

                try: # obtein review title
                    review_title_element = block.find_element(By.CLASS_NAME, "c-review-block__title")
                    review_title = review_title_element.text
                    print(review_title) if report else None
                except Exception as e:
                    review_title =  None
                    print("ERROR: WHILE SCRAPPING TITLE REVIEW")

                try: # obtein positive and bad reviews
                    reviews_element = block.find_elements(By.CLASS_NAME, "c-review__body")
                    if len(reviews_element) == 1:
                        good_review =  reviews_element[0].text
                        print(good_review) if report else None
                        bad_review =  None
                    elif len(reviews_element) == 2:
                        good_review =  reviews_element[0].text
                        print(good_review) if report else None
                        bad_review =  reviews_element[1].text
                        print(bad_review) if report else None
                    elif len(reviews_element) == 4:
                        good_review =  reviews_element[0].text
                        print(good_review) if report else None
                        bad_review =  reviews_element[2].text
                        print(bad_review) if report else None
                    else:
                        good_review =  None
                        bad_review =  None
                        print(f"ERROR WHILE SCRAPPING POSITIVE AND NEGATIVE REVIEWS: {len(reviews_element)} elements founded, excepction must be handled")
                        for element in reviews_element:
                            print(element.text)
                        print("-------------------------------------------------------------------------------------------------------------------")
                except Exception as e:
                    good_review =  None
                    bad_review =  None
                    print("ERROR: WHILE SCRAPPING POSITIVE AND NEGATIVE REVIEWS")
            
                # add data to dataframe
                review = pd.DataFrame({
                    "hotel_id": [ids[i]],
                    "nationality": [nationality],
                    "acommodation": [acommodation],
                    "stay": [stay],
                    "date": [date],
                    "company": [company],
                    "review_title": [review_title],
                    "good_review": [good_review],
                    "bad_review": [bad_review]})
                hotel_reviews = pd.concat([hotel_reviews, review], ignore_index=True)

            # Go to next page
            if page+1 < n_pages:
                next_page_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pagenext'))) 
                next_page_button.click() 
            
    driver.quit()
    return hotel_reviews