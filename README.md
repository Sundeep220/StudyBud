# StudyBud

`StudyBud` is an online platform for learners to come together and share their knowledge about any thing like technology, problem, project etc with each other.

- Before running this project: 

  -> Create a virtual environment, in Windows command is as follows: \
    `pythom -m venv env` \
   -> To activate: \
     `env/Scripts/activate`

- To run this project do the following:

    Pre-requisites: Python, pip and django should be installed in your system. All the coding is done using VScode.
    1. To install the dependencies: \
       `pip install -r requirements.txt` 
    2. Make the migrations:\
        `python manage.py makemigrations` 
    3. Migrate the tables: \
        `python manage.py migrate` 
    4. Create a superuser for your project: \
        `python manage.py createsuperuser`   
        This will prompt you to enter username, email and password for the superuser.  
    5. Run the server using: \
        `python manage.py runserver`
        
        
- Application go through: \
  -> Login or register site. \
  -> View the dashboard designed sshowing all the rooms and topics as well as recent activities by users on each rooms with latest activity as first. \
  -> Create your own room wiht any topic or join the room entering in chat of room. \
  -> View all the messages in chat and either delete your message or view profile of users sending the message. \
  -> View or update your user profile.
  
  
- Home page: 

![home](https://user-images.githubusercontent.com/93663329/201783900-4a3e8427-65f7-4987-9415-3a000ca422b4.png)


- Topics page:

![topics](https://user-images.githubusercontent.com/93663329/201783944-5dcc32b4-167e-4daa-9b04-89c1a75747c1.png)


- Room page:

![room](https://user-images.githubusercontent.com/93663329/201783979-ec742f61-0ee4-4ec7-b2fe-6f5f883ba262.png)


- Create/update room page:

![create-room](https://user-images.githubusercontent.com/93663329/201784006-c29f08f9-560b-4426-ad5c-0e3d3d6b8ce0.png)


- User profile page: 


![profile](https://user-images.githubusercontent.com/93663329/201784032-b1800ec1-81f2-4011-8b6d-49e4ced7b7c2.png)


-Deletion page:


![delete-room](https://user-images.githubusercontent.com/93663329/201784054-63bde7f0-c768-43fb-8c9b-e98816fd7723.png)



  
  
  
  
  
  
