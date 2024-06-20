FROM python:3.11-slim

LABEL Name=OPDT Version=1.0

WORKDIR /app
ADD . /app

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

COPY scripts/docker_entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
