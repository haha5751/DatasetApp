# DatasetApp

This is a sample project that demonstrates the usage of Django, Pandas and Matplotlib to visualize data. 

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The project aims to provide an easy way to visualize air quality data, as well as serve as a good introduction to the Django framework. 
The data was sourced from kaggle and cleaned using a personal Python script. 

## Features

- Feature 1: A user can specify a country.
- Feature 2: A user can select from five air quality metrics. 
- Feature 3: A user will be able to view a graph containing the cities of the country they specified and the selected metric associated with each city. 

## Installation

To install and use this project, follow these steps:

1. Clone the repository: `[git clone https://github.com/haha5751/DatasetApp.git]`
2. Navigate to the project directory: `cd DatasetApp`
3. Install the dependencies: `poetry install`
4. Load the data set into PostgreSQL: `https://www.kaggle.com/datasets/adityaramachandran27/world-air-quality-index-by-city-and-coordinates`
5. A cleaned version of the data set can be found [here](./Data/cleaneddata.zip)
6. Enter in your credentials into settings.py: `DatasetApp/DatasetApp/project/settings.py` under DATABASES
7. Make the migrations: `poetry run python manage.py makemigrations`
8. Execute the migrations: `poetry run python manage.py migrate`
9. Start the application: `poetry run python manage.py runserver`
10. Go to the address provided: `http://XXX.X.X.X:XXXX/` 

## Usage

After installation, you can use the project as follows:

1. Go to the Output page using the navigation bar
2. Enter in a country, follow the guidelines in the Home page
3. Select your air quality metric and click Submit

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [GPL 2](./LICENSE) License. Feel free to use, modify, and distribute it as per the terms of the license.

## Acknowledgements

- Mention any acknowledgements or dependencies used in the project.
- Provide links to external resources or libraries used.

