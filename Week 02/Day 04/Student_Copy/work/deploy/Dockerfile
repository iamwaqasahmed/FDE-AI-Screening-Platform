# Shell image. Chapter 06 replaces the copy under work/deploy.
# Leave this file in the packet unchanged.
# The last USER line is root. While this file is the image that
# runs, the deploy check says the image runs as root.
FROM python:3.12-slim
WORKDIR /app
COPY app/ /app/
EXPOSE 8080
USER root
CMD ["python", "app.py"]
