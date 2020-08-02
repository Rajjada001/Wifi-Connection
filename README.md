# Wifi-Connection

### Install Python 3 and Gitbash. Links are available here

- [Download Python](https://www.python.org/downloads/)
- [Download Gitbash](https://git-scm.com/downloads)

#### Open GitBash and go to any folder by running `cd FolderPath`

#### Now run `git clone https://github.com/Rajjada001/Wifi-Connection.git`

#### Now run `code .` It will open visual studio code

#### Open terminal in VS Code,

- run `pip3 install django`
- run `cd .\ConnectToWifi\`

##### Now run the project. You can do that by running this command.

- run `python manage.py runserver`

##### Now go to any browser, copy and paste http://127.0.0.1:8000/ in the url

## New modifications include:

- Stored Wifi SSI name & password in the database
- Added some code in `models.py`
- Created a new file that congratulates the User after logged in.

##### In order to store those details, we have to make migrations after added a class in `models.py`

- Run `python manage.py makemigrations`
- Run `python manage.py migrate`
- Run `python manage.py createsuperuser`

  > Now you need to provide credentials for the superuser.
  >
  > type _Django_ as the username
  >
  > email: django@connect.in
  >
  > password : connect

- Now run `python manage.py runserver` then fill the form, you will see the result.
- You can check your stored values in http://127.0.0.1:8000/admin/tasks/connecttowifi/

![Screenshot (162)](https://user-images.githubusercontent.com/56466485/89096212-811e1480-d3f2-11ea-9d04-e5b2bc7cee17.png)

![Screenshot (163)](https://user-images.githubusercontent.com/56466485/89116532-ba1dbe00-d4b2-11ea-9212-82f7277add67.png)
