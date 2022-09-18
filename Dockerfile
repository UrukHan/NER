FROM nvidia/cuda:11.1.1-cudnn8-runtime-ubuntu18.04

ENV LC_ALL=C.UTF-8
ENV LANG=c.UTF-8

FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install gdown && \
    mkdir -p /app && \
    mkdir -p /app/ner_model && \
    gdown "https://drive.google.com/uc?export=download&confirm=no_antivirus&id=10YS52vjKFmv3TBh5Tfsew7UPXlMyvUDu" -O /app/ner_model/ner_model.zip && \ 
    unzip /app/ner_model/ner_model.zip -d /app/ner_model/ && \
    rm /app/ner_model/ner_model.zip && \
    pip install -r requirements.txt && \
    pip install uvloop && \
    pip install torch==1.10.2+cu113 torchvision==0.11.3+cu113 torchaudio==0.10.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

COPY . /app

CMD ["uvicorn", "app.main:app", "--app-dir=./", "--reload", "--workers=1", "--host=0.0.0.0", "--port", "1000", "--use-colors", "--loop=uvloop"]

