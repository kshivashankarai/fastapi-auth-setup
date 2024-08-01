# fastapi-auth-setup


uvicorn app.main:app --reload

alembic revision --autogenerate -m "create my table"

alembic upgrade head

alembic downgrade -1


pytest --log-cli-level=INFO