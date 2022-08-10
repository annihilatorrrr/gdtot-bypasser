from os import environ

from gdtot import app

app.run(
    host=environ.get("HOST", "0.0.0.0"),
    port=environ.get("PORT", 8000),
    load_dotenv=True,
    debug=environ.get("DEBUG").lower() == "true",
)
