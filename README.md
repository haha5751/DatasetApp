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

1. Clone the repository: `[git clone https://github.com/your-username/project-name.git](https://github.com/haha5751/DatasetApp.git)`
2. Navigate to the project directory: `cd DatasetApp`
3. Install the dependencies: `poetry install`
5. Make the migrations: `poetry run python manage.py makemigrations`
6. Execute the migrations: `poetry run python manage.py migrate`
7. Start the application: `poetry run python manage.py runserver`
8. Go to the address provided: `http://XXX.X.X.X:XXXX/` 

## Usage

After installation, you can use the project as follows:

1. Load the data set into PostgreSQL: `https://www.kaggle.com/datasets/adityaramachandran27/world-air-quality-index-by-city-and-coordinates`
2. The data set must have rows containing null values removed: `https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html`
3. Enter in your credentials into settings.py: `DatasetApp/DatasetApp/project/settings.py under DATABASES`
4. Repeat steps 5 to 8 in the installation section

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [GPL 2](./LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.

## Acknowledgements

- Mention any acknowledgements or dependencies used in the project.
- Provide links to external resources or libraries used.

