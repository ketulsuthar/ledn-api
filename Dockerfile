FROM python:3.8-alpine
WORKDIR /usr/src/ledn
RUN apk add --no-cache gcc g++ musl-dev linux-headers
COPY . .

RUN pip install -r ./requirements.txt

CMD ["python", "manage.py"]