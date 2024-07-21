import requests


class CountryData:
    def _init_(self, url):
        self.url = url
        self.data = None

    def fetch_data(self):
        try:
            response = requests.get("https://restcountries.com/v3.1/all")
            response.raise_for_status()
            self.data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

    def display_countries_and_currencies(self):
        if self.data:
            for country in self.data:
                name = country.get('name', {}).get('common', 'N/A')
                currencies = country.get('currencies', {})
                for currency_code, currency_info in currencies.items():
                    currency_name = currency_info.get('name', 'N/A')
                    currency_symbol = currency_info.get('symbol', 'N/A')
                    print(f"Country: {name}, Currency: {currency_name}, Symbol: {currency_symbol}")

    def display_countries_with_dollars(self):
        if self.data:
            for country in self.data:
                currencies = country.get('currencies', {})
                for currency_code, currency_info in currencies.items():
                    if 'dollar' in currency_info.get('name', '').lower():
                        print(country.get('name', {}).get('common', 'N/A'))
                        break

    def display_countries_with_euro(self):
        if self.data:
            for country in self.data:
                currencies = country.get('currencies', {})
                for currency_code, currency_info in currencies.items():
                    if 'euro' in currency_info.get('name', '').lower():
                        print(country.get('name', {}).get('common', 'N/A'))
                        break


# Usage
country_data = CountryData()  # Instantiate the CountryData class
country_data.fetch_data()     # Fetch data from the REST API

url = "https://restcountries.com/v3.1/all"
country_data = CountryData(url)
country_data.fetch_data()

print("Countries and their currencies:")
country_data.display_countries_and_currencies()

print("\nCountries using Dollars:")
country_data.display_countries_with_dollars()

print("\nCountries using Euros:")
country_data.display_countries_with_euro()