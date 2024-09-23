FROM python:3.12-slim-bookworm as base_layer
RUN mkdir /app
COPY /src /app
RUN pip3 install -r /app/requirements.txt --no-cache-dir

FROM base_layer AS top_layer
COPY --from=base_layer /app /app
WORKDIR /app
CMD ["python3", "main.py"]