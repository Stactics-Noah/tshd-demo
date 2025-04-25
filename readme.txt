# Django Chatbot Demo

A minimal, self‑contained **Django 5** project that showcases how to build a server‑rendered chatbot interface without any JavaScript.  
Messages are streamed to OpenAI’s Chat Completion API and the entire conversation is stored in the user’s session cookie, so you can deploy this app with **no database at all**.

---

## ✨ Key features

* **Pure‑backend stack** – Python + Django only. No JS, no frontend frameworks.
* **Clean UI** – Simple HTML & CSS give you a neat, centered chat window that works on any device.
* **Stateless deployment** – Session cookies keep each browser tab’s chat history. No models, migrations or DB.
* **OpenAI integration** – Easy drop‑in call to the [`openai`](https://pypi.org/project/openai/) package.
* **100 % open‑source** – Copy, learn, hack, and extend as you wish.

![screenshot](docs/screenshot.png)

---

## 🔧 Prerequisites

| Tool | Tested version | Notes |
|------|---------------|-------|
| Python | `3.11` | Any 3.10 + should work |
| Django | `5.x` | Installed via `requirements.txt` |
| pip / venv | — | Recommended for isolation |
| OpenAI account | — | Needed for API key |

> **Tip:** On Windows PowerShell replace `source .venv/bin/activate` with `.venv\Scripts\activate`.

---

## 🚀 Quick start

```bash
# 1 – Clone & enter
$ git clone https://github.com/your‑fork/chatbot_project.git
$ cd chatbot_project

# 2 – Create virtualenv & install deps
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt

# 3 – Add your OpenAI key (Unix‑like shells)
$ export OPENAI_API_KEY="sk‑…"

# 4 – Run migrations (creates sqlite3 even if unused)
$ python manage.py migrate

# 5 – Fire up the dev server
$ python manage.py runserver

# 6 – Visit http://127.0.0.1:8000/ and start chatting!
```

On Windows CMD/PowerShell use `set OPENAI_API_KEY=…`.

> If you prefer **hard‑coding the key** you can paste it in `chat/views.py` where the comment reads `# 🔑 IMPORTANT — provide your own key here`.

---

## 📁 Project structure explained

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

### Why no `models.py`?

Chat history lives in `request.session` (signed cookie). For anything heavier than a demo you’d add a model to persist messages per user.

---

## 🖥️ App walk‑through

1. **Form display ⇢ POST**  
   * `GET /` renders `index.html` with an empty `ChatForm` and the current `history`, an array of `{role, content}` dicts.
2. **Validation**  
   * `ChatForm` ensures the message is a non‑empty string.
3. **Call OpenAI**  
   * `openai.ChatCompletion.create()` is called with the full `history` list (user + assistant turns).  
   * Adjust `MODEL_NAME` or provide extra parameters (e.g. `temperature`) as you like.
4. **Persist & redirect**  
   * The assistant’s reply is appended to `history` and stored back in the session.  
   * We `redirect()` to `GET` (Post/Redirect/Get) so the browser URL stays clean and refreshes won’t re‑POST.
5. **Render**  
   * Template loops messages, assigns CSS classes `msg user` / `msg assistant` for colour coding.

---

## 🎨 Styling notes

* The CSS keeps everything centered with a subtle drop‑shadow and rounded corners.
* `.chat-box` is capped at 400 px height with `overflow-y: auto` for scroll.
* No JavaScript is required: Django’s CSRF token + normal form submission does the job.

Feel free to replace `styles.css` with Bootstrap/Tailwind if you want richer UI.

---

## 🔒 Security & production checklist

| Item | Demo value | Production advice |
|------|------------|-------------------|
| `DEBUG` | `True` | Set `False` + define `ALLOWED_HOSTS` |
| `SECRET_KEY` | Hard‑coded | Load from env variable |
| OpenAI key | In env or code | **Never** commit the real key |
| CSRF | Enabled | Keep it; use HTTPS |
| Sessions | Cookie‑based | Consider signed‐cookie size limits or DB sessions |
| Static files | Served by Django | Use WhiteNoise or real web server |
| Gunicorn | — | `gunicorn chatbot_project.wsgi` (add `--workers 3`) |

---

## ⚙️ Environment variables

| Variable | Purpose |
|----------|---------|
| `OPENAI_API_KEY` | Secret key for OpenAI API (preferred) |
| `OPENAI_MODEL` | Override the default model name |
| `DJANGO_SECRET_KEY` | Override dev secret |

You can inject them via your `.env`, docker compose, or hosting panel.

---

## 🚢 Deployment pointers

* **Heroku / Fly.io / Render** – all support buildpacks that install Python, collect static with `whitenoise`, and expose a WSGI server.
* **Docker** – add a `Dockerfile` like:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt \ \
    && python manage.py collectstatic --noinput
ENV DJANGO_SETTINGS_MODULE=chatbot_project.settings \
    PYTHONUNBUFFERED=1
CMD gunicorn chatbot_project.wsgi:application --bind 0.0.0.0:$PORT --workers 3
```

* **Static files** – run `python manage.py collectstatic` during build or startup.

---

## 🛠️ Extending the project

| Idea | How to implement |
|------|-----------------|
| Persist chats per user | Add `ChatSession` + `Message` models and store user ID |
| Add streaming responses | Use Django Channels + Server‑Sent Events |
| Markdown rendering | Pipe assistant replies through `markdown` library |
| Prompt engineering | Prepend system messages or tools API calls |
| Authentication | `django.contrib.auth` + login form |
| Rate limiting | Django Ratelimit or Redis sliding window |

---

## 🧪 Running tests (optional)

The demo has no tests yet. If you add models or utils, hook up **pytest‑django**:

```bash
pip install pytest pytest-django
pytest
```

---

## 🤝 Contributing

1. Fork the repo and create your branch: `git checkout -b feature/XYZ`
2. Commit your changes with clear messages.
3. Push to GitHub and open a PR.

All contributions (docs, code, issues) are welcome!

---

## 📜 License

MIT – do whatever you like, just keep the copyright notice.

---

### Author

**Your Name** – [@yourhandle](https://github.com/yourhandle)

---

Happy chatting 🚀

