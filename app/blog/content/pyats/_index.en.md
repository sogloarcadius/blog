---
title: "Cisco pyATS & Genie Abstraction Engine & SSH Proxy"
description: ""
date: 2020-06-28T08:56:58+02:00
lastmod: 2020-06-28T08:56:58+02:00
draft: false
type: "docs"
icon: "ti-book"
keywords: ["automation", "network", "pyats", "genie", "cisco"]
weight: 1
---

## Introduction

Cisco made available to developpers his internal network testing library for free.

pyATS is a network device agnostic test and automation solution with building blocks to allow developpers to 

- Configure network devices
- Parse network devices commands output
- Run tests (reusable test cases like pytest/unittest)
- etc... 

For more detail on what the library can do, please refer to the official documentation on Cisco DEVNET.

- [pyATS Getting Started](https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/intro/introduction.html#what-is-the-pyats-ecosystem)

It is important to understand that pyATS is the core engine and it is integrated with different modules to give the end user a high level abstraction to interact with network devices. An important library is **genie** which gives access to parsers, device configuration objects, tests modules and other features.

pyATS by design allow the use of custom connection plugin, so it is easy to extend it to support a new device. **Unicon** is the main connection library for telnet, ssh,...  and it supports many vendors devices and of course you can contribute to the plugins development.

Check the following links to get more details on the pyATS ecosystem :

* [Devnet Page](https://developer.cisco.com/pyats/)
* [Documentations Links](https://developer.cisco.com/docs/pyats/#!introduction)
* [pyATS Getting Started](https://developer.cisco.com/docs/pyats-getting-started/)
* [pyATS Developper Guide](https://developer.cisco.com/docs/pyats-development-guide/)
* [pyATS Code Documentation](https://developer.cisco.com/docs/pyats/api/)
* [Genie Documentation](https://developer.cisco.com/docs/genie-docs/)
* [Unicon](https://pubhub.devnetcloud.com/media/unicon/docs/user_guide/introduction.html)
* [Unicon Plugins](https://github.com/CiscoTestAutomation/unicon.plugins)


## Genie Abstraction Engine & SSH Proxy


pyATS provides a Command Line Interface which can be used with a testbed file or you can create a python script to implement your own logic by using the python objects.

If you are new to pyATS, please go through the documentation to take hands on tutorials and there are a lot of ressources on internet to help you get started.

In this post, i am focusing on the configuration of the SSH Proxy using a python script and giving details on the different python objects used.

First confirm you install pyats and genie, for example using python pip

```bash

$ pip install pyats[full]

```

Now create your python script and follow the instructions below.


```py

from pyats.topology import Testbed
from pyats.topology.credentials import Credentials
from genie.conf.base.device import Device

```

Three main import is needed :

* **Testbed** is the object to create a topology. Topology objects are just like Testbed YAML files but using python objects. It allows us to use a custom input file different than the [official format](https://pubhub.devnetcloud.com/media/pyats/docs/topology/schema.html#topology-schema). We can parse our custom file and use python to create the expexted format by pyATS.

* **Credentials** object to create a username/password entries.

* **Device** object to create device objects to be added to the topology object. Notice here, i am importing Device object from genie module. In fact `genie Device` object inherits `pyats Device` object and enable specific features based on the device parameters (os, series, ...) for example to access genie parsers.

In fact Cisco defines an abstraction library that allow to dynamically select the correct classes (parsers, connections, configurations) based on the user input (tokens : os, series, platform, ...). 
For details on this abstraction library, read the documentation which provide valuable information on the [Genie Abstraction package](https://pubhub.devnetcloud.com/media/genie-docs/docs/abstract/index.html). 

Genie parsers, most of the times define default *token(s)* to use from the *Base Device class*.

Because we are defining our topology programmatically, we better make sure Genie know how to select the correct parsers.

This can be done by adding a custom key value pair to the device object. This is how we tell genie the field (token) to use to select our parser (Abstract Lookup).

```yaml

# https://pubhub.devnetcloud.com/media/genie-docs/docs/abstract/lookup_class.html#integration-with-topology

device:
    my-example-device:
        type: router
        os: iosxe
        series: asr1k
        custom:
            abstraction:
                order: ["os", "series", "context"]
                context: yang
```


For more detail on the Search Algorithm (Parser Selection), please refer to the official documentation of [Genie Abstraction package](https://pubhub.devnetcloud.com/media/genie-docs/docs/abstract/concept.html#search-algorithm)

After importing the required object, we can create our devices and add them to a topology 

```py

topology = Testbed(name="topology")


proxy_ssh_command = "ssh -l {login} -p {port} -vrf GREEN {ip}"
proxy_device = Device(
    name=proxy_hostname,
    credentials=Credentials(dict(default=dict(username=proxy_username,password=proxy_password))),   
    alias=proxy_hostname,
    type=proxy_type,
    os=proxy_os,
    series=proxy_series,
    connections={
        'defaults': {
            'class': 'unicon.Unicon',
            'alias': 'default',
            'via': 'green',
        },
        'green': {
                    "arguments": dict(init_config_commands=[], init_exec_commands=[]),
                    "command": proxy_ssh_command.format(login=proxy_username, port=proxy_port, ip=proxy_management_ip)
                }
    }
)

topology.add_device(proxy_device)


target_device = Device(
        name=target_hostname,
        credentials=Credentials(dict(default=dict(username=target_username,password=target_password))),
        type=target_type,
        os=target_os,
        series=target_series,
        custom={'abstraction': {'order': ["os"]} }, # could be ["os", "series"] or ["os", "platform"] or custom field value as described above
        connections={'default': dict(ip=target_management_ip,
                                    arguments=dict(init_config_commands=[], init_exec_commands=[]),
                                    protocol='ssh',
                                    port=target_port,
                                    proxy=[proxy_hostname,] # Expect string or list of string which reference a device name in topology
                                )
                    }
)


topology.add_device(target_device)

```


Notice, that pyATS allow us to create different connections for a device and we can specify the one to use during the connection using the **via**.
For more information on the different ways to configure your connections refer to the [documentation](https://pubhub.devnetcloud.com/media/pyats/docs/topology/schema.html#production-yaml-schema).

We can use the command key option to override the default ssh command used by the connection plugin to connect to the device for example to use SSH options or specify a VRF if using a router as a Jump host (SSH Proxy). By the way the default command used by unicon to connect to devices will not work on Cisco routers (default unicon.Unicon ssh command "ssh -l target_username target_management_ip -p 22").


Unicon Connection plugins support the use of proxy. In the connection(s), we can specify one proxy or a list of proxy to use to get to the target device.
Find more information on the possible configurations options on [unicon documentation](https://pubhub.devnetcloud.com/media/unicon/docs/user_guide/proxy.html#connection-through-proxies). 

Be aware, that the proxy key expect a string or list of string. Do not try to pass him a Device object(s), pyATS is unable to detect it. I have done the testing and didn't work that way.

Make sure your proxy(ies) and target device are linked to the same topology(testbed object) and that you specify the exact proxy name(s) configured in the topology.


Now, you can connect to the device and access all the features of pyats and genie.

```py

target_device.connect(log_stdout=log_stdout, connection_timeout=connection_timeout, learn_hostname=learn_hostname, settings=dict(
            GRACEFUL_DISCONNECT_MAX_WAIT_SEC=graceful_disconnect_max_wait_sec, POST_DISCONNECT_WAIT_SEC=post_disconnect_wait_sec))


target_device.execute(command)

target_device.parse(command)

target_device.configure(config)

target_device.disconnect()

target_device.destroy()

```

