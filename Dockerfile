FROM python:3.8

RUN apt-get update -qq
RUN mkdir /myapp

WORKDIR /myapp

COPY requirements.txt /myapp/requirements.txt

RUN pip install -r requirements.txt

COPY ./ /myapp

# Add a script to be executed every time the container starts.
COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["/usr/bin/entrypoint.sh"]
EXPOSE 8000

# Start the main process.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]