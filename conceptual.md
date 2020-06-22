### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  - JavaScript is a web browser language, Python is not
  - Python is an Object Oriented Programming language
  - Python comes with it's own libraries that can be imported
  - JavaScript uses 2 or 4 spaces, Python best practive is 4 spaces
  - Indentation is not an issue with JS, Indentation is **very** important in Python
  - JS uses _camelCase_ as a naming convention, Python uses _lower_snake_case_
  - JS uses keywords to declare variables, Python does not
  - JS does not differentiate between floats and integers, Python does
  - JS equality uses "==" or "===", Python uses "==" or "is"

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.

  1. using the dict.get(x, default) method
  2. using the dict.setdefault(default) method

- What is a unit test?

  - A test on an individual component in a large multi-component app

- What is an integration test?

  - A test that checks if some or all the parts of the component work together

- What is the role of web application framework, like Flask?

  - Web applications handle web requests, CRUD methods
  - They produce dynamic HTML
  - Connect to databases
  - Handle forms
  - Authentication
  - Handles cookies and sessions

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  - Depending on the user input, it would be better to have a dynamic route using a URL query param, since it would be dynamically generated rather than manually typing the url everytime.

- How do you collect data from a URL placeholder parameter using Flask?

  - We collect the data by passing it on the the function, and then using the request method.

- How do you collect data from the query string using Flask?

  - By using the request.args.get method inside the function.

- How do you collect data from the body of the request using Flask?
  - By using the request.data, either request.args, request.form, request.files, request.values or request.get_json()

* What is a cookie and what kinds of things are they commonly used for?
  - Cookies are a way to store small bits of data on the client side (browser). These are name/string-value pairs.

- What is the session object in Flask?

  - Session is a type of dict that contain infor for the current browser. They are signed, so users cannot modify them, and they preserve the type of data.

- What does Flask's `jsonify()` do?

  - jsonify parses the returned data as a json object.

- What was the hardest part of this past week for you?

  - the gap between the course videos vs the course assignments. I feel the course videos either don't cover all the material required to complete the assignment, or I need more smaller assignments leading up to the end of unit assignment.

  What was the most interesting?

  - learning Python and Flask.
