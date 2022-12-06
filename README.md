<h1 align="center">Home Learning</h1>

[View the live project here.](https://milestone-p4.herokuapp.com/)

This is an ecommerce site, selling learning curricula to parents and teachers. It is designed to be responsive and accessible on a range of devices, making it easy to navigate for potential customers.

<h2 align="center"><img src="media/homepage_image_small.png"></h2>

## User Experience (UX)

-   ### User stories

    User stories can be found [here](#)

-   ### Design
    -   #### Colour Scheme
        -   White is the predominant colour on the site, creating a clean and clear background.  The rainbow-coloured logo design and multi-coloured pencils in the hero image are eye-catching and represent the different styles of learning:
            - Red is physical
            - Orange is for passion and fun
            - Yellow is creative and emotional
            - Green represents nature and the environment
            - Blue is logical and intellectual
            - Purple throws in a bit of luxury and decadence
    -   #### Typography
        -   Roboto is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. It is a clean font which clearly communicates a feeling of professionalism and authenticity to the user.  Fuzzy Bubble is used as the logo font to offer a friendly and welcoming feel to the company.
    -   #### Imagery
        -   The white background of the hero image allows for a clean and clear layout, with the bold and colourful side image catching the user's attention. The image of pencils is directly linked to the educational content being sold on the site and so is relevant and descriptive.

*   ### Wireframes

    -   [Home](media/home.png)
    -   [About](media/about.png)
    -   [Products](media/products.png)
    -   [Product Details](media/product_details.png)
    -   [Contact](media/contact.png)
    -   [Shopping Bag](media/bag.png)
    -   [Checkout](media/checkout.png)


## Features

-   Responsive on all device sizes

-   Interactive elements

-   Stripe payments

## Future Features

-   A messaging service for logged in users via the Account tab.  When registered users submit a contact form it will be stored in their Account as part of the messaging service.

-   Add a rating input in the reviews form and then calculate an average user rating for each product.


## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://www.javascript.com/)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on buttons throughout the site
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Fuzzy Bubble' and 'Roboto' fonts into the style.css file which are used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/) during the design process.
1. [Kaggle:](https://www.kaggle.com/)
1. [ElephantDQL](https://www.elephantsql.com/)
    - PostgreSQL database
1. [Stripe](https://stripe.com/gb)
    - Stripe is used to manage payments
1. [Heroku](https://www.heroku.com/)
    - Heroku was used to deploy the site
1. [Django](https://www.djangoproject.com/)
    - Django framework.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)
-   Javascript validator

### Testing User Stories from User Experience (UX) Section

    Testing user stories information can be found [here](#)

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Problems Encountered

-  Trying to obtain cards of the same size with the same image dimensions but with good proportions across the range of screen sizes.

-   Contact form was working locally but when posting the form on the deployed app it was generating a 500 error.  After hours of frustration, I contacted Tutor Support, who suggested migrating with a heroku prefix and all was solved.

### Known Bugs

-   On some mobile devices the checkout page layout gets squashed and the +/- buttons are oddly positioned.

## Deployment

Check details to put here!

## Credits

### Code

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

-   [MDN Web Docs](https://developer.mozilla.org/) : For Pattern Validation code. Code was modified to better fit my needs and to match an Irish phone number layout to ensure correct validation. Tutorial Found [Here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/tel#Pattern_validation)

-   Rainbow gradient used for the logo-font class was taken from [We Learn to Code](https://welearncode.com/rainbow-text/)

-   CSS code taken from [Bulma](https://bulma.io/) to size and position font awesome icons

-   Footer positioning inspired by an [article on DEV site](https://dev.to/niorad/keeping-the-footer-at-the-bottom-with-css-grid-15mf0)

### Content

-   All content was written by the developer with inspiration taken from the Code Institute Walkthrough Project.

-   Code Institute ReadMe template used to structure ReadMe.

-   Psychological properties of colours text in the README.md was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)

### Media

-   Website background is a mirrored version of a photo by [Kelly Tungay](https://unsplash.com/@kellitungay?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/learning?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

-   Pencils photo by [Jess Bailey](https://unsplash.com/@jessbaileydesigns?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/learning?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

-   Puzzle photo by [Hans-Peter Gauster](https://unsplash.com/@sloppyperfectionist?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unslpash](https://unsplash.com/s/photos/learning?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

-   Calculator photo by [AnoushkaP](https://unsplash.com/@_purianoushka?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/maths?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

-   Pyramids photo by [Shotaro Hamasaki](https://unsplash.com/ja/@_shography?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/pyramids%27?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

-  Globe Photo by [Amy Humphries](https://unsplash.com/@amyjoyhumphries?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/globe?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)


-  Chemistry Photo by [Raghav Bhasin](https://unsplash.com/@myphotocave?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/chemistry?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
  

-  Computing Photo by [Markus Spiske](https://unsplash.com/@markusspiske?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/science?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

-  Dice Photo by [Jonathan Petersson](https://unsplash.com/@grizzlybear?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/bingo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

- Mystery Photo by [Media Modifier](https://unsplash.com/@mediamodifier?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/detective?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
  
  
  
  
  
  

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.