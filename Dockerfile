FROM python:3.7.9-slim
RUN apt update
RUN pip install python-telegram-bot
RUN pip install scikit-learn
RUN pip install numpy
RUN pip install pandas
RUN pip install plotly
RUN apt install git -y
RUN pip install kaleido
RUN pip install pyyaml