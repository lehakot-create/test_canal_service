FROM python:alpine

WORKDIR /my_bot

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]

#docker build -t bot .
#docker run --rm -d -v pwd:/my_bot/ bot