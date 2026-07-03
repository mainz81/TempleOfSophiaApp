# Temple of Sophia v0.1

A private writing sanctuary for book creation with Streamlit, OpenAI Responses API, hierarchical ToC, etc.

## Deploy to Vercel

1. Make sure this repo is connected to your GitHub.
2. Go to https://vercel.com/new/import
3. Select this repository (TempleOfSophiaApp)
4. Vercel will detect it as Python project.
5. Add Environment Variables in the dashboard:
   - OPENAI_API_KEY = sk-...
   - OPENAI_MODEL = gpt-5.5 (or your model)
6. Deploy.

**Note:** Streamlit apps work best on platforms that support long-running servers (like Streamlit Cloud or Render). Vercel is serverless, so the full interactive app may have limitations or require additional setup (e.g. using a custom server). If the deploy doesn't serve the UI, let me know and we'll use a better platform.

## Local Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# edit .env with key
streamlit run app.py
```