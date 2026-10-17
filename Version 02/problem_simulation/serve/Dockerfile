# Build from the problem_simulation folder: docker build -f serve/Dockerfile -t hartland-serve .
FROM python:3.13-slim

WORKDIR /app
COPY serve/requirements.txt serve/requirements.txt
RUN pip install --no-cache-dir -r serve/requirements.txt

COPY simulation simulation
COPY serve serve

ENV HARTLAND_DATA=/data \
    HARTLAND_CLOCK=2026-10-01 \
    HARTLAND_WEEK=1 \
    SYSTEM=all \
    PORT=8800

EXPOSE 8800
CMD ["sh", "-c", "python -m serve --system \"$SYSTEM\" --host 0.0.0.0 --port \"$PORT\""]
