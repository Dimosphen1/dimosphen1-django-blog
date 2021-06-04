<h1>DIMOSPHEN1/ blog</h1>

<b>Video Demo:</b> [YouTube](https://youtu.be/jGaT-Iw0lgQ) <br>
<b>Website:</b> [DIMOSPHEN1/ blog](https://dimosphen1-blog.herokuapp.com/)
<br>
<p>A blog application where users can run CRUD operations over different posts
of their authorship. Flows for registered and non-registered users are
separated, with options to:</p>
<p><ol>
  <li>Create a new account, log in, reset the password for unsigned users;</li>
  <li>Create, delete and update posts and update profile info, log out,
upload the personal image to change the default one from user
profile for logged-in users;</li>
  <li>Read posts, navigate through the paginated list of all posts (5 posts
per page), and read 'about page' with additional information for all
users.</li>
</ol></p>
<p>Permissions and authorization are implemented with the Django
authentication system and LoginRequeredMixin for class-based views,
login_requered decorator for function-based views.</p>
<br>
<p>The project is written on Django web framework for python and is deployed to Heroku. For production, the relational PostgreSQL database was used. Overall, the project has four folders. The folder 'blog' contains a blog application with logic regarding the functioning of the blog. In the urls.py file, you can see special URLs for navigating users throughout the web application. For this application, I used class-based views with nicely encapsulated logic for running CRUD operations.</p>
<p>In contrast to the 'blog' application, the 'users' application used function-based views that allow procced POST and GET requests for creating and updating user's profiles.</p>
<p>One of the most interesting parts of the program is generating a special link that is used for resetting a password. It can be found in the django_project directory in the urls.py file. Here in the following path: <i>path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm')</i> you can see how Django generates unique uidb64 and token using build-in functionality. </p>
<p>Amazon S3 bucket was used to store and update user's images. Each user by logging in has his/her default image, which they can correct later.</p>

<span><i>Tools & Technologies:</i> Python, Django, django-crispy-forms, sqlite3, Pillow,
HTML, CSS, bootstrap.</span>
<br>
<br>
<span><b>PS:</b> More information about the project can be found on the <i>about</i> page on the website)</span>
