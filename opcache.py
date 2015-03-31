import agent_util
import logging
import urllib2

logger = logging.getLogger(__name__)


class OpCachePlugin(agent_util.Plugin):
    textkey = "opcache"
    label = "PHP OpCache"

    @classmethod
    def update_metrics(self, config):
        metric = {}
        r = urllib2.urlopen(config['opcache_url'])
        reply = r.read()
        reply = reply.strip().strip(';').split(';')
        for item in reply:
            if 'hit_rate' in item or ('.php') in item: continue
            else:
                metric_name = item.split(':')[0]
                metric_value = item.split(':')[-1]
                metric["php_opcache." + metric_name] = float(metric_value)
        return metric

    @classmethod
    def get_metadata(self, config):
        status = agent_util.MISCONFIGURED
        msg = 'Missing/incorrect data in [opcache] block!'
	
        if "opcache_url" in config:
            url = config['opcache_url']
            status = agent_util.SUPPORTED
            msg = None
        else:
            return {}

        metadata = {}
        metrics = self.update_metrics(config)

        options = []

        for textkey in metrics:
            metadata[textkey] = {
                    "label": textkey.replace('_',' ').title(),
                    "options": options,
                    "status": status,
                    "error_message": msg
                }
        return metadata

    def check(self, textkey, data, config):
        tmp = self.update_metrics(config)
        if textkey in tmp:
            return tmp[textkey]
        else:
            return None
