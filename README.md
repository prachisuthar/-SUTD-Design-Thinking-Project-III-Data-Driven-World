# 2D-Final

## Instructions on running Flask app on Vocareum's terminal:

Run the following terminal commands in sequence.

1. Move into the project folder:

    - Run `pwd` to make sure that you are in the /work subfolder in Vocareum

    - Run `cd 2D-Final` to enter the project directory.

1. Activate virtual environment using this code:

    ```
    source virtenv/bin/activate
    ```
    
2. Install required dependencies for the project:
```
    python -m pip install -U --force-reinstall -r requirements.txt
```

3. Run Flask app on Vocareum:
```
    sed -i -e 's/\r$//' runflaskvoc.sh
    
    chmod a+x ./runflaskvoc.sh
    
    ./runflaskvoc.sh
    
```
​
4. Go to myserver.vocareum.com to find the deployed web-app.