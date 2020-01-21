#!/bin/bash

docker build -t sentiment_clf .

docker run -i --rm sentiment_clf
