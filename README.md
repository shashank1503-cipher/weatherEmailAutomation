# Weather Email Automation App

> Assignment Submission for Xtreme Technologies.

![image](https://user-images.githubusercontent.com/54381338/148017526-dfc2c797-d7f5-4274-8ed0-b00fb9b2c0f9.png)

## Requirements  (Prerequisites)

Tools and packages required to successfully install this project.
For example:

* Python 3.6.5 and up [Install](https://www.python.org/downloads/)

## Installation

A step by step list of commands / guide that informs how to install an instance of this project.

* Clone the project

    ```git clone project-url```

* Install virtualenv to create virtual environment

    ```pip install virtualenv```

* Create and activate virtualenv

    ```virtualenv venv```

    ```cd venv/scripts/activate```

* Change Directory to base directory of django project

    ```cd..```
    ```cd..```

* Install Requirements

    ```pip install -r requirements.txt```

## Screenshots

Main Page to get input

![Input Page](https://user-images.githubusercontent.com/54381338/148014781-ce87eadf-ca00-4104-9b10-f2ec40bc950b.png)

Email Sent Confirmation Page

![Email Sent Confirmation](https://user-images.githubusercontent.com/54381338/148014908-dc7c0a11-da6b-4e25-a32d-60ac1d25a708.png)

Email

![Email](https://user-images.githubusercontent.com/54381338/148015070-5a05255b-6e8d-4c68-a1e6-69f3ba1d7636.png)

Django Admin Page

![Django Admin Page](https://user-images.githubusercontent.com/54381338/148015745-e7bbb7c0-8437-4dab-af6b-fb0bc00e1995.png)

Error Handling

* SMTP Error
    ![SMTP_Error](https://user-images.githubusercontent.com/54381338/148015404-ac567224-4063-49f9-85d2-edac046a34c8.png)
* Bad Header Error
    ![BadHeaderError](https://user-images.githubusercontent.com/54381338/148015554-2b23c585-81e2-4bdd-8c84-e22f4e5d091d.png)

## Features

The project uses OpenweatherMap API to get the weather data for a specific city and sends the temperature to the given mail using Django's inbuilt Email Service. Noticeable features about the codebase:

* Robust Code
* Use of Environment Variables to store secret_keys for added security advantage

## Usage example

The project is deployed using Heroku.
Application can be used by visiting the following link
[Deployment](https://weather-email-automation.herokuapp.com/)

## Tech Stack / Built With

1. [Django](https://www.djangoproject.com/) - Python based Framework

## How to Contribute

This Repository is currently not accepting any contributions.

## Authors

Shashank Kumar Srivastava  – shashank.srivastava25sks@gmail.com

You can find me here at:
[Github](https://github.com/shashank1503-cipher)
[LinkedIn](https://www.linkedin.com/in/shashank-srivastava-a72899201/)

## Credits

This project uses [OpenWeatherMap](https://openweathermap.org/api) to fetch current weather data.
