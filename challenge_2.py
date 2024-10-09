from bs4 import BeautifulSoup
import json, requests

# URL of the webpage to scrape
url = "https://www.microfocus.com/en-us/products?trial=true"

def parse_products(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = []

    # Find all product blocks (adjust the selector based on actual HTML structure)
    product_blocks = soup.find_all('a', class_='block-header')

    for header in product_blocks:
        # Extract Product Name
        product_name = header.get_text(strip=True)
        starting_letter = product_name[0]

        # Navigate to the parent block to find related information
        product_block = header.find_parent('div', class_='product-block')

        if not product_block:
            continue  # Skip if the structure doesn't match

        # Extract Description
        description_div = product_block.find('div', class_='description')
        if description_div:
            description = description_div.find('p').get_text(strip=True)
        else:
            description = ''

        # Extract Free Trial / Demo Request URL
        trial_link = product_block.find('a', class_='uk-button uk-button-primary', target='_blank')
        if trial_link:
            free_trial_url = trial_link.get('href')
        else:
            free_trial_url = ''

        # Extract Support Link URL
        support_link = product_block.find('a', class_='uk-link uk-text-bold', target='_blank')
        if support_link:
            support_url = support_link.get('href')
        else:
            support_url = ''

        # Extract Community Link URL
        community_links = product_block.find_all('a', class_='uk-link uk-text-bold uk-margin-small-right', target='_blank')
        community_url = ''
        for link in community_links:
            if 'community' in link.get('href', '').lower():
                community_url = link.get('href')
                break

        product_info = {
            'Product Name': product_name,
            'Starting Letter': starting_letter,
            'Description': description,
            'Free Trial / Demo Request URL': free_trial_url,
            'Support Link URL': support_url,
            'Community Link URL': community_url
        }

        products.append(product_info)

    return products

if __name__ == "__main__":
    # Get the page content
    response = requests.get(url)
    html_content = response.text

    products_list = parse_products(html_content)
    print(json.dumps(products_list, indent=4))