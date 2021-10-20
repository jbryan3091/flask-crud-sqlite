# Istall SO Alpine
FROM python:3-alpine


# Install Python3, pip3 and upgrade it
RUN apk add --no-cache python3-dev \
    && pip install --upgrade pip

# Create folder App
WORKDIR /app

# Copy all files in previous folder
COPY . /app

RUN apk add --no-cache musl-dev gcc libffi-dev g++

# Run pip3 to install all requirements obtained using "pip freeze > requirements.txt"
RUN pip install -r requiriments.txt

ENTRYPOINT FLASK_APP=/app/app.py flask run --host=0.0.0.0
#CMD [ "python", "app.py" ]