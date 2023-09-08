# Use an official Python runtime as a parent image
FROM python:3.12.0b4-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Install the dependencies mentioned in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Command to run the application
# The actual numeric values for UserID and UserHash should be provided during the container run
ENTRYPOINT ["python", "app.py"]

# The CMD directive provides default arguments to the ENTRYPOINT
# They can be overridden by providing arguments in the docker run command
CMD ["UserID", "UserHash"]

