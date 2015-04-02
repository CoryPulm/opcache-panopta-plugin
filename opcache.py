import agent_util
import logging
import urllib2

logger = logging.getLogger(__name__)


class OpCachePlugin(agent_util.Plugin):
    textkey = "opcache"
    label = "PHP OpCache"

    @classmethod
    def update_metrics(self, config):
        # Make initial call to opcache.py using url set in config
        metric = {}
        r = urllib2.urlopen(config['opcache_url'])
        reply = r.read()
        reply = reply.strip().strip(';').split(';')
        for item in reply:
            if 'time' in item: continue
            # So we can strip out the duplicate entries from the metadata like the duplicate free/used_memory stats
            # did this because the first metric it returns is the actual correct one, the second is the default
            elif item.split(':')[0] in  metric.keys(): continue
            else:
                metric_name = item.split(':')[0]
                metric_value = item.split(':')[-1]
                metric[metric_name] = float(metric_value)
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
            # Adjusting for MB since it outputs in bytes
            if 'memory' in textkey or 'buffer' in textkey:
                return float(tmp[textkey]/1048576)
            else:
                return tmp[textkey]
        else:
            return None

