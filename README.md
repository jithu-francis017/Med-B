

# Med-B and Token Generator

Welcome to my Personal AI Health Assistant and Token Generator repository! This project is built using Django and Python, and has two main components: a web application that allows you to store all your medical data in one place, and a token generator GUI that optimizes queues in hospital OP ticket counters.

## Med-B

The web application component of this project allows you to keep track of all your medical data in one place. You can enter details such as your medications, allergies, medical history, and more, and the Personal AI Health Assistant will use this information to provide personalized health advice and reminders.

### Features

- Secure login and registration system
- Personalized dashboard with summary of medical data
- Input forms for entering and updating medical data
- Reminders for medications and appointments
- AI-powered health advice and recommendations
- and much more!

### Getting Started

To get started with the Personal AI Health Assistant, you'll need to have Python and Django installed on your machine. You can download the latest version of Python [here](https://www.python.org/downloads/) and the latest version of Django [here](https://www.djangoproject.com/download/).

Once you have Python and Django installed, clone this repository to your local machine using:

```
git clone https://github.com/jithu-francis017/Med-B.git
```

Then, navigate to the repository directory and run the following commands:

```
python manage.py migrate
python manage.py runserver
```

You can then access the Personal AI Health Assistant by visiting `http://localhost:8000` in your web browser.

## Token Generator

The token generator component of this project is a GUI application written in Python that optimizes queues in hospital OP ticket counters. It generates unique tokens for each patient.

### Features

- GUI interface for easy use
- Optimizes queue based on various factors
- Generates unique tokens for each patient
- Saves the waiting time for each patient data.
- and much more!

### Getting Started

To get started with the Token Generator, you'll need to have Python installed on your machine. You can download the latest version of Python [here](https://www.python.org/downloads/).

Once you have Python installed, clone this repository to your local machine using:

```
git clone https://github.com/jithu-francis017/Med-B.git
```

Then, navigate to the repository directory and run the following command:

```
python TokenSystem.py
```

You can then use the Token Generator GUI to optimize queues in hospital OP ticket counters.

## Contributions

Contributions to this project are welcome! If you would like to contribute, please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
