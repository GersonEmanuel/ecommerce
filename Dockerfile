
FROM python: 3.12

WORKDIR .

COPY requirements.txt .
RUN pip install --no-cache-dir - requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]



