# Flash cards

## DESCRIPTION
Flash cards is a simple Django application tailored to meet the needs of users who want to remember what they think seems important.The site allows users to keep the flash cards, delete , update and create new flash cards.


#### By:
* Mark Ndonye
* Maureen Wairimu

## Behavior Driven Development (BDD)

Behavior                 |Input                            |Output                             |
|------------------------|----------------------------------|----------------------------------|
|The landing page loads  |Users scroll | Users see available posts|
|Sign in to the app to see flashcards |Users sign in/ register |Users are directed to the sign up or login page form|
|The flash card loads  |Users click on the delete or update flash card they createde|Users see their updated or deleted flash card on the landing page|
|The landing page loads  |Users click on submit card and write their flash card|Flash card will be uploaded and displayed to landing page|
|The flash card loads  |Users click on flashcard  |User sees when the flash card was created and when it was last updated|
|The flash card loads  |Users click on a selected category they want |Users Flashcards are organized according to subjects/courses|

### Technology /Prerequisites
* DJANGO web framework.
* pip
* sqlite or Postgres

## Setup Instructions

<ol>
<li> Clone this repo: git clone <code> https://github.com/ndonyemark/Flash.git</code> </li>
<li>The repo comes in a zipped or compressed format. Extract to your prefered location and open it.</li>
<li> Create a virtual environment and activate it.
<pre>
<code>
pip install virtualenv
source virtual/bin/activate
</code></pre>
</li>
<li> Install all the requirements <code> pip install -r requirements.txt</code></li>
<li> On your terminal,Create database aaward using the command :<code>CREATE DATABASE flash; and update settings.py </code>
</li>
<li> Migrate the database using the command : <code> python3.6 manage.py migrate </code> </li>
<li> Run <code>python3 manage.py runserver</code> to serve the app.</li>
<li> Use the navigation bar menu to navigate and explore the app.</li>
</ol>

## Live link: https://flashcards0.herokuapp.com/

## Technologies Used
* HTML - HTML dictates the structure of webpages.
* CSS & Bootstrap - CSS determines the appearance of webpages. The styling language was used to add background images and colors and style the site's content.
* Python  - The language was used to create classes, testcases, and functions to retrieve data
* [Django](https://www.djangoproject.com/) -  Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.


## Support and contact details
You are free to suggest and improve the code. To make your changes:
* Fork the repo
* Create a new branch
* Create, add, commit, and push your changes to the branch
* Create a pull request
* You can also contact the creators via email: ndonyemark@gmail.com , murimimaureen8@gmail.com

## Running the tests
Use the command given below to run automated tests.
<code> python manage.py test flash </code>

## Known Bugs
* None at the moment

## License

[MIT License](LICENSE.md)
Copyright (c) 2020 **Mark Ndonye**, **Maureen Wairimu**

