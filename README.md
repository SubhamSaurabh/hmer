# hmer Installation Instruction
Before installing the project, make sure to have your local system have python 3.6 and pip3 installed. Make sure to install git also. Then follow the following instructions. 
- ## Creating virtual environment
    - ```bash
        python3 -m virtualenv env 
        ```
    - ```bash
        cd env 
        ```
- ## Activating environment
    - For windows
        - ```bash
            cd Script
            ```

        -  ```bash
            ./activate
            ```
    
    - For Linux
        - ```bash
            Source bin/activate
            ```

- ## Getting the project
    - Making a directory
        ```bash
        mkdir hmer
        ```
    - Go to the created directory
        ```bash
        cd hmer
        ```
    - Initialize the project
        ```bash 
        git init
        ```
    - Pull the project
        ```bash
        git pull https://github.com/SubhamSaurabh/hmer
        ```

- ## Installing all the requirements
    - ```bash
        pip3 install -r requirements.txt 
        ```



