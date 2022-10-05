FROM python:3.9 
ADD . .
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1
CMD python3 main.py 
