<h2>NOTE: This plugin is now bundled by default for all new Panopta agent installations!!</h2>

<h5>Plugin for monitoring OpCache stats using the Panopta Agent</h5>
<h6> You can sign up for Panopta <a href='http://www.panopta.com/'>here</a> and download the monitoring agent <a href='http://answers.panopta.com/how-do-i-install-and-configure-a-panopta-monitoring-agent-v-2/'>here</a></h6>
<strong>Requirements:</strong>
<br />
Python 2.7+
<br />
<br />
<strong>To Install:</strong>
<ol>
<li>Download the panopta-opcache.php and drop it in the proper folder for your site files</li>
<li>Edit the /etc/panopta-agent/panopta_agent.cfg file and add similar code to the below:
	<ul><li>[opcache]<br />opcache_url = http://localhost/opcache.php<br /></li></ul>
</li>
<li>Make sure to lock down that file so only localhost can access it, you don't want this getting seen by others.</li>
<li>Download the opcache.py and drop it into your plugins folder: '/usr/lib/panopta-agent/plugins'</li>
<li>Run the agent command to rebuild the metadata: 'python /usr/bin/panopta-agent/panopta_agent.py --rebuild-metadata'</li>
</ol>

