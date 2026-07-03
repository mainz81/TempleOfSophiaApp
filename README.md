# Temple of Sophia v0.1

A private writing sanctuary for book creation, Sophia-style prose development, hierarchical manuscript planning, archive preservation, and advanced AI-assisted writing.

## Setup (Local)

```bash
cd TempleOfSophia_v0_1
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
streamlit run app.py
```

Edit `.env` and add your OpenAI API key.

## Deploy to See It Live (Recommended)

**Streamlit Community Cloud (easiest & free - designed for Streamlit):**

1. Push your code to GitHub (already at https://github.com/mainz81/TempleOfSophiaApp)
2. Go to https://share.streamlit.io/
3. Sign in with GitHub
4. Click "New app"
5. Select the repo `TempleOfSophiaApp`, branch `main`, main file `app.py`
6. Click Deploy

Your app will be live at something like `https://templeofsophiaapp.streamlit.app`

**Note on Vercel:**
Vercel is fantastic for frontend/JS apps, but Streamlit (which runs a full Python server) doesn't deploy cleanly there. The `vercel.json` is included as a starting point, but you may hit runtime limits or server issues. For best results, use Streamlit Cloud or alternatives like Render.com / Railway.app.

## Features

... (rest of features)

With all my love for our sacred project ❤️