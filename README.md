 Band Member Quiz (Flask Web App)

A small Flask web application that deploys a personality-style quiz and assigns users to a member of the band King Gizzard and the Lizard Wizard based on their answers. The app colectse results across users and displays live statistics.

Link to webpage: https://astroturfing.pythonanywhere.com



 Features

- Multi-question quiz with radio-button inputs  
- Server-side scoring logic in Python  
- Result pages rendered dynamically with Jinja2  
- Persistent global statistics stored in a JSON file  
- Percentage breakdown of results across all users  
- Randomized song recommendation based on quiz outcome
- Custom CSS "lava lamp" animations and HTML
- Deployed and publicly accessible  

Stack

- Python  
- Flask  
- Jinja2  
- HTML / CSS  
- JSON (for lightweight persistence)



How It Works

1. Users fill out a multi-question HTML form.
2. The form submits data via `POST` to a Flask route.
3. Each answer contributes to a score for one of several outcomes.
4. The highest-scoring outcome is selected.
5. A global results counter (stored in `results.json`) is updated.
6. The result page displays:
   - the user’s outcome
   - a randomly selected song
   - aggregate statistics across all users



Persistent Statistics

The app maintains a `results.json` file that tracks:
- Total number of submissions
- Number of times each outcome was selected

These values are used to compute and display percentage statistics on the result pages.



