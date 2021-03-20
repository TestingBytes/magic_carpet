# Magic Carpet

![Magic Carpet](/images/magic_carpet_logo.jpg)

Powered by Genie

![Genie](/images/genie.png)

And the pyATS framework

![pyATS](/images/pyats.png)

Welcome! 

Magic Carpet is a Cisco "show" command transformation tool that uses the Cisco Genie parsers and the Cisco pyATS Python library and automatically generates, at scale, better documentation from the output. 

A Nice JSON file (command_output.json)

A Nice YAML file (command_output.yaml)

A CSV spreadsheet (command_output.csv)

A Markdown file (command_output.md)

An HTML page (comand_output.html)

In seconds. 

## Genie and pyATS

The main Genie documentation guide:

https://developer.cisco.com/docs/genie-docs/

The main pyATS documentation guide:
https://developer.cisco.com/docs/pyats/

The Cisco's Test Automation Solution

![CTAS](/images/layers.png)

The Cisco Test Automation GitHub repository

https://github.com/CiscoTestAutomation

Here are the pyATS documentation guides on Testbed files and Device Connectivity:

Testbed and Topology Information: https://pubhub.devnetcloud.com/media/pyats/docs/topology/index.html

Device Connection: https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/quickstart/manageconnections.html

Testbed File Example: https://pubhub.devnetcloud.com/media/pyats/docs/topology/example.html

Device Connections: https://developer.cisco.com/docs/pyats/#!connection-to-devices

Secret Strings (how I encrypted the enable secret in my testbed file): https://pubhub.devnetcloud.com/media/pyats/docs/utilities/secret_strings.html

### Simply a better way; a magical way; to collect and transform network state information

Install pyATS

```console
pip install pyats[full]
```

Update the testbed file to reflect your devices.

Ensure SSH connectivity and run the pyATS job

```console
pyats run job IOS_XE_magic_carpet_job.py --testbed-file testbed/testbed.yaml
```

### IOS-XE Tests
Tested on Cisco Catalyst 4500X-16 03.11.03a.E

Tested on Cisco Catalyst 3850-12X48U Gibraltar 16.12.04

Tested on Cisco Catalyst 9300-48UXM Gibraltar

#### The World's First Talking Network is Powered by Magic Carpet 

<iframe width="560" height="315" src="https://www.youtube.com/embed/yyWnvzc0vlA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>