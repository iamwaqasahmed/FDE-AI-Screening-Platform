FROM python:3.12-slim

WORKDIR /app

COPY screening_tools screening_tools
COPY screening_retrieval screening_retrieval
COPY screening_agent screening_agent
COPY screening_service screening_service
COPY data/handover data/handover
COPY data/corpus data/corpus

RUN pip install --no-cache-dir pandas openpyxl

CMD ["python", "-m", "screening_service.run", "--who", "clinic nurse", "--question", "How many eligible people are there?"]
