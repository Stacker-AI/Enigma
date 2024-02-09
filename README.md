# Enigma Project

The Enigma project will enhance the privacy and security by filtering personal information before sending it to the Langchain/OpenAI API. 

## Components
The project comprises the following main components:

1. **FastAPI Backend**
2. **Angular Frontend**
3. **Langchain/OpenAI API**

## Setup

1. Clone the repository from [GitHub](https://github.com/Stacker-AI/Enigma/)

2. Install dependencies for both the backend and frontend. Navigate to the respective directories (`backend` and `frontend`) and run:
   - Frontend
    ```
    npm install
    ```
    - Backend
    ```
    pip install -r requirements.txt
    ```

4. Configure environment variables:
    - Add API keys for the Langchain/OpenAI in `.env` file.

5. Start the backend server. Navigate to the `backend` directory and run:
    ```
    python main.py
    ```

6. Start the frontend server. Navigate to the `frontend` directory and run:
    ```
    ng serve
    ```

7. Access the application in your browser at `http://localhost:4200`.


## Contributing
Contributions to the Enigma project are welcome! Please fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).