# Santas Helpers

Santas Helpers is a simple website that helps kids send their christmas letters over to santa.

User's can register to join the site and view lists created by all other users if they need some inspiration. They can also go to create and view their own lists. Users are also able to edit and delete their own lists at any time with ease!

Users can also use the search function to find the lists made by certain users by writing their username into the search bar. Parents looking to see what their kids have sent to santa will have an easy way to take a peak!

 
![An images showing the website being responsive across multiple devices](santashelpers/static/images/santas-helpers-responsive.png "Resonsive site")


[You can visit the Santas Helpers website here](https://santashelpers-bddb45353cba.herokuapp.com)
------

## Table of Contents

### [User Experience (UX)](#user-experience-ux)
* #### [User Stories](#user-stories)
* #### [WireFrames](#wire-frames) (View the repository [here](https://github.com/Wxrren/win-a-car/tree/main/assets/images/wireframes))
* #### [Design](#design-1)

### [Features](#features-1)
* #### [Existing Features](#existing-features-1)
* #### [Features Left to Implement](#features-left-to-implement-1)

### [Bugs](#bugs-1)

### [Testing](#testing-1)
* #### [Validation Results](#validation-results-1)
* #### [Manual Testing](#manual-testing-1)
* #### [Lighthouse Report](#lighthouse-report-1)

### [Technologies Used](#technologies-used-1)

### [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used-1)

### [Deployment and local development](#deployment-and-local-development-1)
* #### [GitHub Pages](#github-pages-1)
* #### [Forking the GitHub Repository](#forking-the-github-repository-1)
* #### [Local Clone](#local-clone-1)

### [Credits](#credits-1)

### [Acknowledgements](#acknowledgements-1)
------

## User Experience (UX)

There is a clear navigation in the nav bar which directs you on where to view your individual lists where you can also create your own lists. Then navbar also clearly directs you to the search function where you can search for individual users.

The website is designed to be simple so that ypung children can use it to make their christmas lists. For this reason I kept the pages plane with content central of the screen. User's card's appear in the middle of the screen with flashing + icons and instructions on the top of the page indicating to click the + to view the list. The edit and delete buttons are attached to the cards to make it easier.

To make the user experience easy - I wanted the site to have:

* A simple and easy registration and sign up form.
* A simple nav bar for children to get around the site easily.
* A simple UI. I wanted minimal buttons appearing on the screen to make it less cluttered focussing only on what they need to view lists or make their own.


## User Stories
To determine which approach to take with site features I determined the goals of different users from first time through to frequent users.

### User

* First time User Goals
    * As a user I want to understand the main purpose of the site immediately and have a fast way to get involved.
    * As a user I want to understand how I can create lists or view other peoples easily.
    * As a user I want to be able to easily navigate the site.
    
* Returning User Goals
    * As a user I want to be get straight into the action and sign in easily.
    * As a user I want to be able to easily edit my lists or delete old ones.
    
* Frequent User Goals
    * As a user I want to be able to get started quickly
    * As a user I want to see a simple and easy website with no added bloat since the last attempt.

## Wire Frames

When designing this website I intended to have a very minimal design that didn't distract from the main purpose.

I chose to keep simple and clean pages and make usage of modals for viewing lists to stop users having to go back and forth to different pages for user's lists and also for deleting lists to make sure accidental deletion doesn't happen.

### Wireframe for Desktop, Tablet and Mobile.


<details>
<summary>Landing Page Wireframe.</summary>

![Landing page for website.](santashelpers/static/images/wireframe-landing-page.png "Landing Page")

</details>

<details>
<summary>Registration page Wireframe.</summary>

![Registration page for website.](santashelpers/static/images/wireframe-register-page.png "Registration page")

</details>

<details>
<summary>Sign in page Wireframe.</summary>

![Sign in page for website.](santashelpers/static/images/wireframe-sign-in-page.png "Sign in page")

</details>

<details>
<summary>Main page Wireframe.</summary>

![Main page for website.](santashelpers/static/images/wireframe-main-page.png "Main page")

</details>

<details>
<summary>My lists page Wireframe.</summary>

![My lists page for website.](santashelpers/static/images/wireframe-my_lists-page.png "My lists page")

</details>

<details>
<summary>Add/edit list page Wireframe.</summary>

![add/edit list page for website.](santashelpers/static/images/wireframe-add-and-edit-list-page.png "add/edit list page")

</details>

<details>
<summary>Delete modal Wireframe.</summary>

![Delete modal for website.](santashelpers/static/images/wireframe-delete-modal.png "Delete modal page")

</details>

<details>
<summary>Search Page Wireframe.</summary>

![Search Page for website.](santashelpers/static/images/wireframe-search-page.png "Search page")

</details>


## Design

### Colour

The colour scheme I wanted for the website kept the theme of simple and clean. I also wanted to continue the christmas theme so I chose a series of red's, green's and amber yellow's. I used images for the navbar and footer of a christmas wreath containing those colours and a amber yellow text so that it looks like christmas lights.

For the background I chose a white page with an image of christmas trees that maintain the 3 core colours.

* Main colours used on the website:
    * Text Colour: #ffc107 - This was chosen as a nice standout colour from the greens and reds. I also aimed for it to look like christmas lights among the wreath.. 
    * Modals and button colours: #f44336, #1b5e20,  - This was to keep with the theme of christmas. It also helped represent postive or negative actions such a green for edit and red for delete.

### Typography

* For the fonts I worked with the fonts on materialise - These fonts are -apple-system, BlinkMacSystemFont ,"Segoe UI", Roboto ,Oxygen-Sans ,Ubuntu,Cantarell ,"Helvetica Neue", sans-serif. This covers a range of devices such as iOS, windows, android ETC.

I changed the font weight, to make it bolder and more readable. The result was a text that looked fitting for a kids christmas themed website.

### WireFrames

I created my wireframes using balsamiq wireframes. I found this simple and effective for assessing the sites appearance as it had a variety of ready available tools representing different parts of a website so I was able to design it how I envisioned it.

## Features
* View other peoples christmas lists.
* Create, view, edit and delete christmas lists of your own
* Responsive on all device sizes.

### Existing Features

#### Dark Mode Toggle

![Dark mode toggle shown by a moon and text](assets/images/dark-mode-toggle-feature.png "Dark mode toggle")


* The toggle is fixed to the top right of the page at all times.
* Once clicked the background will turn black and cards will change to a pink and green colour, text will turn white and buttons will turn green. 
* On light mode the logo is a moon. In dark mode the logo is a sun.
* Text changes from "Dark mode" to "Light mode" when toggled between.
* Easily accessible for the user, can be toggled at anytime.

#### Main Feature - Card game

![An image showing the main feature of the website.](assets/images/website-lightmode.png "Main website")

* Main game, when pressing play a modal will pop up wishing the player luck and letting them know to hit next turn after selecting 3 cards.
* Each card has an array of 9 images which will be called at random when the card is selected.
* The play button will change to "Next turn!" after the first attempt is made.
* Matches counter will count as each card selected matches the previous card. This is done by running 2 loops and checking if the card from the inner loop matches the card from the outer loop.
* Each time 3 cards are selected the game will automatically refresh the page. Progress is saved in local storage so when the page refreshed it increments how many attempts have been taken so far.
* If more than 5 attempts are taken a modal wil a game over screen will pop up promting you to restart as seen below.

![An image showing the game over screen](assets/images/restart-modal-feature.png "game over")

#### Email API
![An image showing an email response](assets/images/email-query-feature.png "query")
![An image showing an email response](assets/images/email-win-feature.png "comgratulations")
* An automatic response email that would confirm to users they will have their query responded to. It also provides a contact number to escalate. This email will be received when the form within the "Contact us" modal form seen below is completed. The data taken from user input is passed into the email API. This is done by creating a global variable for contact form data and defining it within each mail function.
![An image showing a form requesting an email and query](assets/images/contact-us-modal-feature.png "query form")
* The email win feature is set up the same way as above. When a user selected 3 cards and matches 3 in a row a game winning modal will pop up requesting their name and email address. From here an email will be sent confirming the prize and how to claim.
![An image showing a form requesting an email and query](assets/images/game-winner-modal-feature.png "winner form")

#### Rules modal
![An image showing a pop up displaying the rules](assets/images/rules-modal-feature.png "rules")
* A simple modal that pops up when the button is clicked.
* Displays the rules to the player before they close it to get started on playing the game.

## Features Left to Implement

* Payment
   
    * To go more with the gambling sort of nature of the game I would like to make the first 5 attempts free to play and make it so that upon game loss users would have to pay to enter again and get another 5 attempts.

* Different Themes

    * I would like to create a few pages with similar games but different themes, maybe a western theme with desert like colours and cowboy images. Different themes to make it more intersting and appealing to users.

* Different games
    * I would like the option to add different game modes of things like guess the box. You would see the prize enter the box and the boxes would then quickly moves around the screen, you would have 3 attempts to select the correct box. 

    ## Bugs

| Problem         | Action           | Status  |
| ------------------------------------------------|:--------------------------------------:| -----:|
| Modals within if statements for win/loss conditions not pop up.| Global variables getting the id's of the modal created allowing them to be accessed withing any function. From here I selected a classlist with a class made on CSS but not in the HTML tags allowing it to only be open on meeting the condition and selecting the correct class.| Fixed |
|  Conditional modals not closing using the buttons and onclick function in the HTML tags. | Within the if statement that selects the modal create another if statement checking that variable's class list contains the same one that's used to open the modal. If it does it will select the close modal class made in CSS and make an onclick event listener so that when the close button is selected it will apply the "close" class removing modal from the screen     |   Fixed |
| Email API not sending user input details.| When set emails with names and texts manually written with strings the emails would send, however, in order for users to receive emails directly to them I needed to connect the form contact values but this would not work or send emails to users. In order to fix this I had to create a global variable. I then passed an argument called "contactForm" into the send email function and within the function created an object containing the name and email address from the contact form where the users data was collected from the form inputs. This would allow email JS to send an email to the user directly with my created template. |    Fixed |
| Cards still flipping even when 3 cards are selected.| With a simple if statement if the selected cards length are >=3 I put "return;" to make the function exit early and stop other cards being selected.     |    Fixed |
Cards still counting as attempts when more than 3 cards are selected.| Similar to previous fix. If the selected cards length are >=3 I put "return;" to make the function exit early and stop other cards being selected and stop it from tracking as more than one attempt.    |    Fixed |
Page refreshing instantly on 3rd card selection before users can see thier cards.| Used javascript "setTime()" function to create a timer delay before the page is refreshed.    |    Fixed |

## Testing

Testing consisted of using the W3C Markup and CSS Validator to go through each page of the project and validate that the code has no errors. They can be located below: 

* [W3C Markup Validator:](https://validator.w3.org/)
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
* [JSHint](http://jshint.com/)

### Validation Results

<details>
<summary>index Page</summary>

![HTML checker showing no errors on the index page.](assets/images/html-validator.png "index")

</details>

<details>
<summary>CSS</summary>

![HTML checker showing no errors on the CSS Stylesheet.](assets/images/css-validator.png "CSS")

</details>

<details>
<summary>Javascript</summary>

![HTML checker showing no errors on the javascript Stylesheet.](assets/images/javascript-validation.png "Javascript")
* NOTE: jshint shows undefinined variables and unused variables. These variables are actually functions that are being called elsewhere. It is also an email.js API file that jshint is not recognising. Other than this, no other errors are present.

</details>

<details>
<summary>Javascript hover file</summary>

![HTML checker showing no errors on the javascript Stylesheet.](assets/images/javascript-hover-validation.png "Javascript")
* NOTE: jshint shows undefinined variables and unused variables. These variables are actually functions that are being called elsewhere. It is also an email.js API file that jshint is not recognising. Other than this, no other errors are present.

</details>

<details>
<summary>Javascript contact modal file</summary>

![HTML checker showing no errors on the javascript Stylesheet.](assets/images/javascript-contact-modal-validation.png "Javascript")
* NOTE: jshint shows undefinined variables and unused variables. These variables are actually functions that are being called elsewhere. It is also an email.js API file that jshint is not recognising. Other than this, no other errors are present.

</details>

<details>
<summary>Javascript rules modal file</summary>

![HTML checker showing no errors on the javascript Stylesheet.](assets/images/javascript-rules-modal-validation.png"Javascript")
* NOTE: jshint shows undefinined variables and unused variables. These variables are actually functions that are being called elsewhere. It is also an email.js API file that jshint is not recognising. Other than this, no other errors are present.

</details>

<details>
<summary>Javascript dark mode file</summary>

![HTML checker showing no errors on the javascript Stylesheet.](assets/images/javascript-toggle-validation.png "Javascript")

</details>



### Manual Testing

* The website was tested on Google Chrome, Opera GX and Safari browsers.
* The website was tested on a Desktop, Laptop, Tablet and x2 phones - one android and one apple.
* Google Dev tools was used to test the responsiveness of the site on different screens.

### Tests performed

| Test        | Status           | 
| ------------- |:-------------:| 
| Emails to user send following input details.      | Pass | 
| Mobile and tablet versions of the game are responsive and work exactly as the desktop version works.    | Pass      |
| Modals pop up on screen when buttons are pressed or conditions such as starting the game, losing game and winning the game are met | Pass      |
| Site works correctly on Android mobile device. | Pass      |
| Site works correctly on Apple mobile device. | Pass      |
| Site works correctly on Apple tablet device. | Pass      |
| Dark mode toggles to a black background with different colour cards and then back to light mode when toggled again | Pass      |
| Page refreshes and correctly counts each attempt made| Pass      |
| Matches are correctly counted and winning by getting 3 is possible  | Pass      |
| Cards can only be selected a maximum of 3 times and it doesn't increase as further attempts if you try to select more | Pass      |
Page refreshed 0.5 miliseconds after 3 cards are selected | Pass      |
Hover functions work as intended for buttons and toggles| Pass      |

--- 

### Lighthouse Report

* Mobile Results

<details>
<summary>Home Page</summary>

![Lighthouse scores for index page on mobile.](assets/images/lighthouse-validation-mobile.png "Index mobile")

</details>

* Desktop Results

<details>
<summary>Home Page</summary>

![Lighthouse scores for index page on mobile.](assets/images/lighthouse-validation-desktop.png "Index desktop")

</details>

## Technologies Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)

## Frameworks, Libraries & Programs Used

* [Visual Studio Code](https://code.visualstudio.com) 
    * Used to write the code/README.

* [Git](https://git-scm.com)
    *  Tracking changes in my course code and pushing them to github.

* [Github](https://github.com)
    * To store my code/files and deploy my website.

* [Google Fonts](https://fonts.google.com)
    * Used for importing my main font for the website

* [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    * Used for making web development faster. My usage was for card columns + forms.

* [Icons8](https://icons8.com/icons)
    * Hamburger icon for mobile Nav bar toggler.

* [Am I Responsive](https://ui.dev/amiresponsive)
    * Mock picture for README file.

## Deployment and local Development.

*  ### GitHub Pages

I used GitHub to deploy the live version of the website. To do this I had to: 

1.  Log in to GitHub and locate the GitHub win a car [Repository](https://github.com/Wxrren/win-a-car)
2.  Locate the "Settings" button at the top of the repository as shown here:

![An image showing the repository page with settings highlighted.](assets/images/repository-settings-location.png "Settings")

3. look down the "Code and automation" area until you find ["Pages"](https://github.com/Wxrren/win-a-car/settings/pages) as shown below:

![An image showing the repository page with pages highlighted.](assets/images/site-link-github-pages.png "Pages")

4. Under "Source", click the dropdown menu "None" and select "Main" and click "Save".

5. The page will automatically refresh.

6. Scroll back to locate the now-published [site link](https://wxrren.github.io/win-a-car/) in the "GitHub Pages" section as seen below:

![An image showing the repository page with pages highlighted.](assets/images/site-link-github-pages.png "Site Link")

* ### Forking the GitHub Repository

Forking the repository allows you to make a copy of the original repository on my GitHub account to view and change without affecting the original repository. To achieve this, follow these steps:

1. Log in to GitHub and locate the GitHub GamerLeague [Repository](https://wxrren.github.io/win-a-car/)
2. At the top of the Repository(above the about section) locate "Fork" button.

![An image showing the repository page with Fork highlighted.](assets/images/fork-location.png "Fork Location")

3. Once complete you should have a copy of the original repository in your GitHub account.

* ### Local Clone

1. Log in to GitHub and locate the GitHub GamerLeague [Repository](https://wxrren.github.io/win-a-car/)
2. Above the list of files, click  Code.

![An image showing the repository page with Fork highlighted.](assets/images/code.png "clone")

3. Click on the code button, select clone with any of the options provided (These options are HTTPS, SSH or GitHub CLI) and copy the link shown.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be created.
6. Type **GIT CLONE**, and then paste the URL you copied earlier.
7. Press Enter to create your local clone.

## Credits

### Images:

* Sun and moon logo taken from [youtube tutorial](https://www.youtube.com/watch?v=9LZGB3OLXNQ)
* Oranges picture taken from [grocerbasket.co.uk](https://grocerybasket.co.uk/product/large-orange-class1-per-kg/)
* Strawberry picture taken from [Pinterest](https://www.pinterest.co.uk/pin/605241637399137511/)
* Watermelon picture taken from [cleanpng.com](https://www.cleanpng.com/png-watermelon-seedless-fruit-dry-taste-3788605/)
* Car picture taken from [milesperhr.com](https://milesperhr.com/2023-bmw-m5-competition-review/)
* Grapes picture taken from [organicseeds4you.com](https://www.organicseeds4you.com/ru/home/black-grape-seeds-vitis-vinifera.html)
* Corn picture taken from [Pinterest.com](https://in.pinterest.com/pin/corn-png-images--577023771027355824/)
* Chilli picture taken from [pngtree.com](https://pngtree.com/so/chilli)
* Blueberry picture taken from [luckyberry.co.il](https://luckyberry.co.il/en/our-fruits/)
* Apple picture taken from [Amazon](https://www.amazon.co.uk/Red-Apples-10-kg-10/dp/B0B7QN4H7R)

### Content and Resources

* All content was written by myself.
* Information on how to make a darkmode toggle was learned from a [youtube tutorial](https://www.youtube.com/watch?v=9LZGB3OLXNQ). I used a different method to achieve this with an event listener and additional features such as changing text. I also targeted in the body in a different way.
* Information on flexbox was provided by: [Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/).
* Information on CSS Grid was provided by: [Complete Guide Grid](https://css-tricks.com/snippets/css/complete-guide-grid/).
* README Template provided by [Code Institute](https://github.com/Code-Institute-Solutions/SampleREADME) & [Markdown Template](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables).
* Bootstrap was used to help with the card columns + forms. I used[Bootstrap.com](https://getbootstrap.com/docs/5.0/getting-started/introduction/).
* To help with queryselectors,, modals, local storage, parseint and timeout I used [w3schools](https://www.w3schools.com/css/css3_2dtransforms.asp)
* For the email API I used [email.js](https://www.emailjs.com)
* I created this project inline with the course content of [Code Institure](https://codeinstitute.net/full-stack-software-development-diploma/?utm_term=code%20institute&utm_campaign=CI+-+UK+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=1578649861&hsa_grp=62188641240&hsa_ad=635720257674&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQiAwP6sBhDAARIsAPfK_wZpFDXlxByAgIRT2S39rCz7auVaNWgJ2FF7efFEtX-oT-_qhvkTSiIaApIBEALw_wcB)

## Acknowledgements

* My mentor Mitko Bachvarov for providing helpful feedback and a link to CSS modals guides on W3 schools.
* Emily for her support during the project process, assistance with testing and advice on the written portion.
* Ethan and Olivia for their support with testing the site is working as intended.