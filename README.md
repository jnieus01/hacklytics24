# InnSight Chatbot
## Navigate Your Next Stay: Effortless Hotel Discovery with a Chat

## Overview

The InnSight Chatbot is designed to answer queries about hotels, their ratings, and locations. It utilizes a vector database and Traversaal AI's API for insightful, context-rich responses. Utilizing advanced natural language processing and data retrieval techniques, the chatbot offers personalized hotel suggestions based on user queries. This project is a collaboration by Rio Jia (xueyuan.jia@vanderbilt.edu) and Jordan Nieusma (jordan.m.nieusma@vanderbilt.edu).
 
## Features

- **Personalized Hotel Recommendations**: Users can receive hotel suggestions tailored to their specific needs and preferences.
- **Accurate Q&A**: Leverages LangChain and a vector DB for in context learning 
- **Fetches Real Time Data from Ares API**: Leverages the Ares API to retrieve real time data based on user queries.


## Technical Overview

The chatbot is implemented in Python and utilizes several key libraries and APIs to provide its functionality:

- **Intel Developer Cloud**: For its PyTorch GPU Compute Environment and Built In Falcon & GPT4All Models
- **Langchain**: For leveraging advanced language models in processing user queries.
- **Traversaal Ares API**: To fetch real-time web data based on the processed queries.

## File Organization
- `01_EDA.ipynb`: Conducts Exploratory Data Analysis on the raw hotel ratings dataset provided by Traversaal AI 
- `02_Data_Preprocessing.ipynb`: Cleans and preprocesses data, producing `hotel_data_for_vector_db.txt`.
- `hotel_data_for_vector_db.txt`: Processed text file serving as the vector database for the chatbot.
- `03_Hotel_Search_Rag.ipynb`: Implements hotel rating retrieval and chatbot functionality.
- WIP folder contains another Data Preprocessing file where we did some additional data preprocessing like translating other language text to english as well as converting images to text but it didn't make it into the final dataset used for the vector database due to time constraints.

## Setup Instructions
1. Access a JupyterLab session on Intel Developer Cloud (equipped with Falcon and GPT4All).
2. Upload `hotel_data_for_vector_db.txt` and `03_Hotel_Search_Rag.ipynb`.
3. Execute all cells in `03_Hotel_Search_Rag.ipynb`.
4. Interact with InnSight Chatbot in the final cell of the notebook.

### Configuration Options
- Adjust top K, temperature, number of threads, chunk size, overlap size, max tokens.
- Toggle RAG (Retrieval-Augmented Generation) and ARES API as needed.
- Interact through the query box; reset conversation with ‘Clear Conversation.’

## Next Steps
- **UI Implementation**: Develop a user-friendly interface for the chatbot.
- **Deployment**: Host the chatbot on a server for wider accessibility.
- **User Accounts**: Enable multi-user functionality with personalized history and session persistence.
- **Expand Functionality**: Integrate additional features such as personalized recommendations and advanced query handling.

## Acknowledgements
Special thanks to Intel Developer Cloud for the ‘RAG with LangChain’ starter code in the ‘Training’ section, Traversaal AI for the creation of this project, and Data Science @ Georgia Tech for putting on Hacklytics 2024! 

## Contribution

We welcome contributions from the community. If you would like to contribute, please reach out to the team members via email.


