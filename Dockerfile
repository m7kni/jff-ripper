# Use an official Python runtime as a parent image
FROM python:3.11-slim-bookworm

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install ffmpeg
RUN apt-get -qq update && apt-get -qq dist-upgrade --yes && apt-get install --yes --no-install-recommends ffmpeg && apt-get -qq purge && apt-get -qq clean && rm -rf /var/lib/apt/lists/*

# Install the dependencies mentioned in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Command to run the application
# The actual numeric values for UserID and UserHash should be provided during the container run
ENTRYPOINT ["python", "app.py"]

# The CMD directive provides default arguments to the ENTRYPOINT
# They can be overridden by providing arguments in the docker run command
CMD ["UserID", "UserHash"]

