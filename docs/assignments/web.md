**Introduction**

In this assignment, we provide an insecure website, and your job is to
attack it by exploiting two common classes of vulnerabilities: SQL
injection and cross-site request forgery (CSRF). 

**Target Website**

A startup named **BUNGLE!** is about to launch its first product --- a
web search engine --- but their investors are nervous about security
problems. Unlike the Bunglers who developed the site, you know a thing
or two about web security, so the investors have hired you to perform a
security evaluation before it goes live.

**BUNGLE!** is available for you to test at
[https://capp30350.cs.uchicago.edu/](https://capp30350.cs.uchicago.edu/){target="_blank"
rel="noopener"}

The site is written in Python using the [Bottle web
framework](https://bottlepy.org/). Although Bottle has built-in
mechanisms that help guard against some common vulnerabilities, the
Bunglers have circumvented or ignored these mechanisms in several
places.

In addition to providing search results, the site accepts logins and
tracks users' search histories. It stores usernames, passwords, and
search history in a MySQL database. Before being granted access to the
source code, you reverse engineered the site and determined that it
replies to five main URLs:

-   **Main page** (`/`) The main page accepts `GET` requests and
    displays a search form. When submitted,this form issues
    a `GET` request to `/search`, sending the search string as the
    parameter "q".\
    If no user is logged in, the main page also displays a form that
    gives the user the option of logging in or creating an account. The
    form issues `POST` requests to /login and /create.
-   **Search results** (`/search`) The search results page accepts GET
    requests and prints the search string, supplied in the "q" query
    parameter, along with the search results. If the user is logged in,
    the page also displays the user's recent search history in a
    sidebar. Note: Since actual search is not relevant to this project,
    you might not receive any results.
-   **Login handler** (`/login`) The login handler
    accepts `POST` requests and takes plaintext "username" and
    "password" query parameters. It checks the user database to see if a
    user with those credentials exists. If so, it sets a login cookie
    and redirects the browser to the main page. The cookie tracks which
    user is logged in; manipulating or forging it is not part of this
    project.
-   **Logout handler** (`/logout`) The logout handler
    accepts `POST` requests. It deletes the login cookie,if set, and
    redirects the browser to the main page.
-   **Create account handler** (`/create`) The create account handler
    accepts `POST` requests and receives plaintext "username" and
    "password" query parameters. It inserts the username and password
    into the database of users, unless a user with that username already
    exists. It then logs the user in and redirects the browser to the
    main page.

Note: The password is neither sent nor stored securely; however, none of
the attacks you implement should depend on this behavior. You should
choose a password that other groups will not guess, but never use an
important password to test an insecure site (in general, you shouldn\'t
reuse any passwords)!

**Guidelines**

**Browser**: We suggest you use Firefox and take advantage of its web
developer tools. Different browser versions have slight variations in
their behavior that may affect your CSRF attacks. 

[SQL Tutorial](http://sqlzoo.net/wiki/SQL_Tutorial)

[SQL Statement
Syntax](https://dev.mysql.com/doc/refman/5.6/en/sql-syntax.html)

[Introduction to
HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Introduction)
