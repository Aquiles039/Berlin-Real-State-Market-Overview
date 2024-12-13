import pandas as pd
import random

# Define Berlin neighborhoods and property types
berlin_neighborhoods = ['Mitte', 'Friedrichshain-Kreuzberg', 'Prenzlauer Berg', 'Neukölln', 'Charlottenburg-Wilmersdorf', 'Schöneberg', 'Tempelhof-Schöneberg', 'Steglitz-Zehlendorf', 'Spandau', 'Marzahn-Hellersdorf', 'Lichtenberg', 'Treptow-Köpenick', 'Reinickendorf']
property_types = ['Apartment', 'House']

def generate_berlin_real_estate_data(num_entries):
    data = {'Property ID': [],
            'Property Type': [],
            'Location': [],
            'Size': [],
            'No of rooms': [],
            'Year Built': [],
            'Floor level': [],
            'Building Condition': [],
            'Price': [],
            'Rent': [],
            'Property Tax': [],
            'Maintenance Cost': [],
            'HOA Fees': [],
            'Mortgage Interest Rate': [],
            'Average Price per Square Meter': [],
            'Price Change': [],
            'Rental Yield': [],
            'Days on Market': []}

    for i in range(num_entries):
        # Generate basic property information
        data['Property ID'].append(i + 1)
        data['Property Type'].append(random.choice(property_types))
        data['Location'].append(random.choice(berlin_neighborhoods))
        data['Size'].append(random.randint(30, 150))
        data['No of rooms'].append(random.randint(1, 4))
        data['Year Built'].append(random.randint(1900, 2023))
        data['Floor level'].append(random.randint(1, 5))
        data['Building Condition'].append(random.choice(['Excellent', 'Good', 'Fair', 'Poor']))

        # Calculate price based on location and property type
        if data['Location'] in ['Mitte', 'Prenzlauer Berg', 'Friedrichshain-Kreuzberg']:
            location_multiplier = 1.5
        else:
            location_multiplier = 1.0

        if data['Property Type'] == 'House':
            type_multiplier = 1.5
        else:
            type_multiplier = 1.0


        print(data['Size'])
        size_multiplier = data['Size'][-1] / 90  # Adjust this factor as needed
        price_multiplier = location_multiplier * type_multiplier *size_multiplier

        price = round(random.randint(150000, 800000) * price_multiplier)
        # ... (rest of the code remains the same)

        price = round(random.randint(150000, 800000) * price_multiplier)
        data['Price'].append(price)

        # Calculate rent based on price and location
        rent_multiplier = 0.05  # A rough estimate of rent-to-price ratio
        data['Rent'].append(round(price * rent_multiplier / 12))

        # Other fields, considering Berlin's real estate market
        data['Property Tax'].append(round(price * 0.015))  # Assuming 1.5% property tax
        data['Maintenance Cost'].append(round(price * 0.01))
        data['HOA Fees'].append(round(data['Rent'][-1] * 0.1))
        data['Mortgage Interest Rate'].append(round(random.uniform(2.5, 4.5), 2))
        data['Average Price per Square Meter'].append(round(price / data['Size'][-1]))
        data['Price Change'].append(round(random.uniform(-5, 10), 2))
        data['Rental Yield'].append(round((data['Rent'][-1] * 12) / price * 100, 2))
        data['Days on Market'].append(random.randint(30, 120))

    return pd.DataFrame(data)

# Generate 100 data points
df = generate_berlin_real_estate_data(1000)
print(df)

# Save to CSV
df.to_csv('berlin_real_Faker_estate_data_.csv', index=False)