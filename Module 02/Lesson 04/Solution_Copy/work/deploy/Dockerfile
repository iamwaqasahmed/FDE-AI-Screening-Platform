# Non-root image. Chapter 06 replaces the work copy with this file.
# Leave the packet shell unchanged.
# The last USER line is the unprivileged account. The shell still
# ends on root.
FROM python:3.12-slim
WORKDIR /app
COPY app/ /app/
EXPOSE 8080
USER 1000
CMD ["python", "app.py"]
