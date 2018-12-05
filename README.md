# Soundeo Auto

built for a friend :)

## Usage

Clone this repo and change directories into it.

Get virtualenv

```
pip install virtualenv
```

Create a new virtual environment in the repo directory as shown below

```
virtualenv venv
```

Activate the virtual environment

```
source venv/bin/activate
```

Install chromedriver via Homebrew this is needed by Selenium

```
brew cask install chromedriver
```

Install python dependencies in the repo directory

```
pip install -r requirements.txt
```

Create a file called config.json with your credentials as defined below in the repo directory
```
{
    "username": "email@gmail.com",
    "password": "password123"
}
```

Run the script

```
python main.py
```

Deactivate the virtual environment once you're done

```
deactivate
```

