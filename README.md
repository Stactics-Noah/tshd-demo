# Django Chatbot Demo
A minimal, self‑contained **Django 5** project that showcases how to build a server‑rendered chatbot interface without any JavaScript. Messages are streamed to OpenAI’s Chat Completion API and the entire conversation is stored in the user’s session cookie, so you can deploy this app with **no database at all**

## 🚀 Quick start
1. Install python and make sure to add it to your path variable when installing: https://www.python.org/downloads/
2. Install git and make sure to add it to your path variable when installing: https://git-scm.com/downloads
3. Create or navigate to folder where you want to put the project
4. run `git clone https://github.com/Stactics-Noah/tshd-demo` to download the repo to this folder
5. Open code editor of choice and open the folder tshd-demo (vscode recommended)

6. Open command prompt in this folder (in the folder where ther epo is which is called tshd-demo)
7. Create new virtual by running `python -m venv .venv`
8. Activate the virtual env on windows by running `.venv\Scripts\activate` or activate the environment on mac an linux by running `source .venv/bin/activate`
9. Install the requirements by running `pip install -r requirements.txt`

11. in the root of the project copy the `.env.example` file and rename it to `.env`, then change`<your-azure-api-key>` to the azure api key provided
10. install mirgations for development server by running `python manage.py migrate`

12. run the development server by running `python manage.py runserver`
13. Go to the development server by opening the browser and navigating to http://localhost:8000

14. Change code in the function `chat_view` in the file `chat/views.py` and observe the changes in behavior
---

## Project structure

```
chatbot_project/                ← repo root
├── manage.py                   ← Django CLI entry‑point
├── requirements.txt            ← pinned deps
│
├── chatbot_project/            ← Django “project” package
│   ├── settings.py             ← minimal settings; only staticfiles + sessions
│   ├── urls.py                 ← routes root → chat.urls
│   └── wsgi.py                 ← WSGI entry for prod hosting
│
└── chat/                       ← our single Django “app”
    ├── views.py                ← form handling + OpenAI call
    ├── forms.py                ← single‑field ChatForm
    ├── urls.py                 ← exposes path("")
    ├── templates/
    │   └── chat/index.html     ← base template – loops through history
    └── static/
        └── chat/styles.css     ← vanilla CSS for a tidy look
```

### Author
**Noah Bouwhuis** – [@Stactics-Noah](https://github.com/Stactics-Noah/tshd-demo/)

