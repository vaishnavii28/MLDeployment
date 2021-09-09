FROM python:3.6-slim
COPY ./dash_app_v4.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./trained_costs_model.pkl /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "dash_app_v4.py"]
