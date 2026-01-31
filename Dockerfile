FROM ubuntu:latest
LABEL authors="caleb"

ENTRYPOINT ["top", "-b"]