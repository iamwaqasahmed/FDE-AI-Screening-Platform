FROM python:3.12-slim

WORKDIR /app

COPY ["Module 02 - Tools the agent can trust/screening_tools", "screening_tools"]
COPY ["Module 03 - Retrieval/screening_retrieval", "screening_retrieval"]
COPY ["Module 04 - The agent/screening_agent", "screening_agent"]
COPY ["Module 06 - Run it in their environment/screening_service", "screening_service"]
COPY data/handover data/handover
COPY data/corpus data/corpus

RUN pip install --no-cache-dir pandas openpyxl

CMD ["python", "-m", "screening_service.run", "--who", "clinic nurse", "--question", "How many eligible people are there?"]
