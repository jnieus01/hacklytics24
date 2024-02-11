# Travel Recommendations Chatbot

## Overview

The Travel Recommendations Chatbot is designed to simplify the process of finding hotel recommendations for travelers. Utilizing advanced natural language processing and data retrieval techniques, the chatbot offers personalized hotel recommendations based on user queries. This project is a collaboration by Rio Jia (xueyuan.jia@vanderbilt.edu) and Jordan Nieusma (jordan.m.nieusma@vanderbilt.edu).
 
## Features

- **Personalized Hotel Recommendations**: Users can receive hotel suggestions tailored to their specific needs and preferences.
- **Easy Integration**: Built with flexibility in mind, the chatbot can be easily integrated into various platforms to assist users in finding their next stay.
- **User-Friendly Interface**: The chatbot is designed with a straightforward and interactive interface, ensuring a smooth user experience.

## Technical Overview

The chatbot is implemented in Python and utilizes several key libraries and APIs to provide its functionality:

- **Langchain**: For leveraging advanced language models in processing user queries.
- **Traversaal Ares API**: To fetch real-time web data based on the processed queries.

### Core Functions

1. **Fetching Data from Ares API**: A function is implemented to communicate with the Ares API, retrieving current hotel data based on user queries.
2. **Processing User Queries**: Utilizes the Langchain library to understand and process natural language inputs from users.

## Setup and Installation

To run the chatbot locally, you need to install the required dependencies:

```bash
pip install gradio
pip install langchain==0.0.335
```

## Usage

After installing the dependencies, you can start the chatbot by executing the main script in the Jupyter notebook. The web interface can then be accessed through the provided URL to start interacting with the chatbot.

## Contribution

We welcome contributions from the community. If you would like to contribute, please reach out to the team members via email.

## License

This project is open-sourced under the MIT license.
