We created a very simple spike. We wrote a mongo post model.

create/name creates a post with the default title and author =name
show displays all author names

For purpose of the spike we created a default user in the create view itself. That is the commented code. Ideally, this would be a seperate manage.py task.

So what you need to do is:
(After installing django and mongoengine on your box)


1.uncomment the first 3 lines of code in create view and do 

python manage.py runserver


2 . hit /create/xyz
    User jill will get created in mongo

3. hit /show
you will be redirected to the login page
login with username jill
password jill

4. You will be taken to the show page where xyz will be displayed

5. hit /admin
(This is django's admin app)

Jill's credentials can be used to log in but some template error is thrown
