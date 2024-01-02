# ChatPDF App

This is a sample ChatPDF app built using Langchain.

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/jaikanthjay46/langchain-sample-app.git
    ```

2. Navigate to the project directory:

    ```shell
    cd ChatPDF
    ```

3. Create and activate a virtual environment:

    ```shell
    python3 -m venv venv
    . ./venv/bin/activate
    ```

4. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```



## Usage


### Replace book.pdf with your PDF
```
curl https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf -o book.pdf
```

### Run queries on book.pdf

```
. ./venv/bin/activate 
python main.py
```


## License

This project is licensed under the [MIT License](./LICENSE).
