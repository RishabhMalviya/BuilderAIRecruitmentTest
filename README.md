# Builder.ai Recruitment Test
***NOTE***: All instructions are Windows specific. 

## Setting up
1. Go to the folder where this package is extracted:
    ```buildoutcfg
    cd .\path\to\this\package\
    ```

2. Create and source a new `venv` if you want:
    ```buildoutcfg
    python -m venv .\venv
    .\venv\Scripts\activate.bat
    ```

3. Install all requirements through `pip`:
    ```buildoutcfg
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

## Running the Local Server
To run the local server, you will have to run the Flask app. 
Run the following commands from the root directory of this package 
(where `app.py` is):

    set FLASK_APP=app.py
    flask run

The open a browser and type in the `http://127.0.0.1/` in the 
address bar to check everything is working. You should see the
following response on the screen:

    Up and running!

The Flask app is designed to run the relevant code in response
to requests to URLs of the kind 
`http://127.0.0.1:5000/map/<input_file>`. Here, `<input_file>` must
be the name of a `.txt` file that is present in the 
`sample_input_data` directory (present under the root directory).
Make sure to omit the extension `.txt` from the filename.

Some sample inputs are already provided under this directory. Based
on this, an example API call would be:

    http://127.0.0.1/map/shortest_path_exists
    
## Running the Test Cases
To run the test cases, `cd` into the `pathfinder` package and
issue the relevant command:
    
    cd .\pathfinder
    python -m pytest