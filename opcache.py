import agent_util
import logging
import httplib

logger = logging.getLogger(__name__)


class UsersPlugin(agent_util.Plugin):
    textkey = "opcache"
    label = "PHP OpCache"

    def update_metrics(self, config):
        r = httplib.HTTPConnection(self.url, 
    
    @classmethod
    def get_metadata(self, config):
        status = agent_util.MISCONFIGURED
        msg = 'Missing/incorrect data in [opcache] block!'
	
        if "opcache_url" in config:
            url = config['opcache_url']
            stats = agent_util.SUPPORTED
            msg = None

        options = []

        data = {
            "php_opcache." + : {
                "label": "Users unique login count",
                "options": options,
                "status": status,
                "error_message": msg
            },
            "users.total_login_count": {
                "label": "Users total login count",
                "options": options,
                "status": status,
                "error_message": msg
            },
        }
        return data

    def check(self, textkey, data, config):
        query = ''
        if (textkey == 'users.unique_login_count'):
            query = 'who | wc -l'

        if (textkey == 'users.total_login_count'):
            query = 'who |cut -c 1-9 |sort -u |wc -l'

        ret, output = agent_util.execute_command('%s' % query)
        return int(output)

