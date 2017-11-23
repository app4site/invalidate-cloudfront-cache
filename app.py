
import os

from flask import Flask, request
app = Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        print('POST request arrived!')
        key = request.args.get('AWS_KEY', '1').replace(' ', '+')
        secret_key = request.args.get('AWS_SECRET_KEY', '1').replace(' ', '+')
        did = request.args.get('DISTRIBUTION_ID', '1')

        os.system(r'printf "{}\n{}\n\n\n" | aws configure > /dev/null'.format(key, secret_key))
        os.system(r"aws cloudfront create-invalidation --distribution-id {} --paths '/*' > /dev/null".format(did))
        os.system(r'printf " \n \n\n\n" | aws configure > /dev/null')
        print('Request ended')
        return 'ok!'
    else:
        return 'Send POST request to this url, with query args AWS_KEY, AWS_SECRET_KEY and DISTRIBUTION_ID (params names are case-sensitive) for your cloudfront distribution and it invalidate your distribution cache'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)