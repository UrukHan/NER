# NER service

Сервис для извлечения сущностей в тексте

Input:      "В ЛДПР оценили возможность вступления Рогозина в партию"

Output:     {"ORG":["ЛДПР"],"PER":["Рогозина"],"LOC":[]}

В сервисе используется нейросеть типо BERT предобученный из SentenceTransformer

# Установка и запуск

Для запуска сервиса локально необходимо выполнить команды:

```bash
# Последовательность команд, которая приведет к успеху (как запускать без докера описывать не нужно)
docker build -t ner:latest .
docker run --rm -d --name ner_service -p 1000:1000 ner:latest
docker run --rm -d --gpus 'device=0' --name ner_service -p 1000:1000 ner:latest
```

# Использование

/health_check:   curl -X GET localhost:1000/health

Сервис принимает запрос с текстом и возвращает ответ в виде dict:

Запрос:   curl -X POST -H "Content-Type: application/json" -d "{ \"text\": \"В ЛДПР оценили возможность вступления Рогозина в партию\" }" localhost:1000/predict

Ответ:     {
            "prediction": {"ORG":["ЛДПР"],"PER":["Рогозина"],"LOC":[]}
            }


