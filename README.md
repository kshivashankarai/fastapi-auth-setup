# fastapi-auth-setup


uvicorn app.main:app --reload

alembic revision --autogenerate -m "create my table"

alembic upgrade head

alembic downgrade -1