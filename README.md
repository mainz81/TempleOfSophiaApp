# Temple of Sophia v0.1 🔮

Private local Streamlit writing sanctuary with OpenAI Responses API.

## Quick Deploy to Vercel (as requested)

I've prepared the repo for you.

**Direct link to import & deploy on Vercel (connects to your GitHub):**

https://vercel.com/new/import?s=https://github.com/mainz81/TempleOfSophiaApp

Steps after clicking:
1. Log in with your GitHub (the one owning this repo).
2. Vercel will detect the project.
3. Add these Environment Variables (in the Vercel dashboard before or after deploy):
   - `OPENAI_API_KEY` = your sk-... key
   - `OPENAI_MODEL` = gpt-5.5 (or gpt-4o etc.)
4. Deploy!

**Important note:** Streamlit needs a running Python web server. Vercel is serverless, so the full interactive experience might have limitations or not start the server properly. If it doesn't work, tell me and I'll instantly set it up on Render.com or Streamlit Cloud (both excellent for this and free).

## Local Development

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# edit .env
streamlit run app.py
```

All the chambers, ToC, Sophia modes, archive, vault, exports, Memory Codex etc. are included. Built with love for you.

Enjoy the Temple! 🙏