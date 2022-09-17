FROM python:3.9-alpine3.13
LABEL maintainer="kliff"
# output from python would be print onto console to see log immedentaly 
#  """ Setting PYTHONUNBUFFERED to a non-empty value different from 0 ensures that the python output i.e. 
#  the stdout and stderr streams are sent straight to terminal (e.g. your container log) without being first buffered and 
# that you can see the output of your application (e.g. django logs) in real time."""

ENV PYTHONUNBUFFERED 1 
# Pass our application to docker as a image?
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

#  First: run a ENV on docker image, (safeguard reason) 
# 2nd: update pip manager
#  3rd: install packages from requirements\
# 4th: remove tmp directiory to remove extra depencies (keep it lightweight)
# 5th: add a new user in image otherwise it will run as root user(no restrictions), we will disable password, the name of the user is 'django-user'
# ARG is revelant when using docker config

#Line 27 we install deps for progressql as temp to be removable to keep app lightweight

ARG DEV=false 
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user


# Run automatically from path

ENV PATH="/py/bin:$PATH"
# run as user
USER django-user 