#!/usr/bin/env python
# coding: utf-8
import json
import logging
from datetime import datetime
from flask import Flask, request

import utils

app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.info = print


@app.route('/', methods=['GET'])
def mentionbot():
    logger.info('Entered Get')

    return "Bot Manager Alert Receiver"


@app.route('/', methods=['POST'])
def webhook():
    logger.info(datetime.now(), '_' * 80)

    payload = json.loads(request.data)

    logger.info('received webhook: {}'.format(utils.PP(payload)))
    logger.info(datetime.now(), '*' * 80)
    return "", 200


def main():
    app.run(host='0.0.0.0', port=5001)


if __name__ == '__main__':
    main()
