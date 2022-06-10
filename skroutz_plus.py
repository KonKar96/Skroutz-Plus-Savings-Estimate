from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import os


def find(xpath):
    try:
        element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        element.location_once_scrolled_into_view
        return element
    except Exception as e:
        return None


def main(driver):
    orders_over_twenty = 0
    driver.get("https://www.skroutz.gr/account/orders?tab=ecommerce_orders")
    print("{}[2J{}[;H".format(chr(27), chr(27)))
    while True:
        element = find("//div[@class='order-list-card ']")
        if element != None:
            print("Logged in!")
            break
        print("Waiting for log in...")

    order_urls = []
    while True:
        orders = driver.find_elements(
            By.XPATH,
            "//div[@class='order-list-card ']",
        )
        for order in orders:
            try:
                order.find_element(By.XPATH, ".//span[@class='delivered icon']")
                order_urls.append(
                    order.find_element(
                        By.XPATH, ".//a[.='Λεπτομέρειες']"
                    ).get_attribute("href")
                )
            except Exception:
                continue

        try:
            print("Searching for next page...")
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(text(),'Επόμενη')]")
                )
            )
            find("//a[contains(text(),'Επόμενη')]").click()
        except Exception:
            print("No more pages.")
            break

    total_items = 0
    total_spent = 0
    for order_url in order_urls:
        driver.get(order_url)
        print(find("//h1[@class='page-title']").text)
        items = driver.find_elements(By.XPATH, "//div[@class='suborder-wrap']")
        for item in items:
            try:
                item.find_element(
                    By.XPATH, ".//p[@class='suborder-delivered-label icon']"
                )
                total_items += 1
                price = float(
                    item.find_element(
                        By.XPATH, ".//p[@class='suborder-item-numeric']/span[last()]"
                    )
                    .text.replace("€", "")
                    .replace(",", ".")
                    .replace(" ", "")
                )
                if price >= 20.0:
                    orders_over_twenty += 1
                total_spent += price
            except Exception:
                continue
    print("{}[2J{}[;H".format(chr(27), chr(27)))
    print(f"Total orders found : {len(order_urls)}")
    print(f"Total items checked : {total_items}")
    print(f"Items equal/over 20 Euros : {orders_over_twenty}\n")
    print(
        f"With the (NEW) 17 Euros subscription you would earn in shipping : {orders_over_twenty * 3 - 17} Euros \n"
    )
    print(
        f"With the (NEW) 20 Euros subscription you would earn in shipping : {orders_over_twenty * 3 - 20} Euros \n"
    )
    print(
        f"""Rough estimate of the (OLD) 17 Euros subscription :
    (Total items * 3 euros shipping)
    Total spent : {total_spent}
    Shipping earned : {(total_items * 3) - 17}
    """
    )
    return


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1020,720")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        f"--user-data-dir=C:\\Users\\{os.getlogin()}\\AppData\\Local\\Google\\Chrome\\User Data"
    )
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    main(driver)
    driver.quit()
