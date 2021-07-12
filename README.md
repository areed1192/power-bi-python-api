# Unofficial Power Bi Python API

## Table of Contents

- [Overview](#overview)
- [Resources](#resources)
- [Setup](#setup)
- [Usage](#usage)
- [Support These Projects](#support-these-projects)

## Overview

Version: **0.1.2**

Power BI is a business analytics service by Microsoft. It aims to provide interactive
visualizations and business intelligence capabilities with an interface simple enough
for end users to create their own reports and dashboards. It is part of the Microsoft
Power Platform. This library allows you to use the Power BI Rest API from python. Along
with providing the different endpoints, it will also handle the authentication process
for you.

## Resources

- [Power BI App Registration Portal](https://dev.powerbi.com/Apps)
- [Power BI Rest API Documentation](https://docs.microsoft.com/en-us/rest/api/power-bi/)

## Setup

**Setup - Requirements Install:**

For this particular project, you only need to install the dependencies, to use the project. The dependencies
are listed in the `requirements.txt` file and can be installed by running the following command:

```console
pip install -r requirements.txt
```

After running that command, the dependencies should be installed.

**Setup - Local Install:**

If you are planning to make modifications to this project or you would like to access it
before it has been indexed on `PyPi`. I would recommend you either install this project
in `editable` mode or do a `local install`. For those of you, who want to make modifications
to this project. I would recommend you install the library in `editable` mode.

If you want to install the library in `editable` mode, make sure to run the `setup.py`
file, so you can install any dependencies you may need. To run the `setup.py` file,
run the following command in your terminal.

```console
pip install -e .
```

If you don't plan to make any modifications to the project but still want to use it across
your different projects, then do a local install.

```console
pip install .
```

This will install all the dependencies listed in the `setup.py` file. Once done
you can use the library wherever you want.

**Setup - PyPi Install:**

To **install** the library, run the following command from the terminal.

```console
pip install python-power-bi
```

**Setup - PyPi Upgrade:**

To **upgrade** the library, run the following command from the terminal.

```console
pip install --upgrade python-power-bi
```

## Usage

Here is a simple example of using the `powerbi` library.

```python
from pprint import pprint
from configparser import ConfigParser
from powerbi.client import PowerBiClient

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('config/config.ini')

# Get the specified credentials.
client_id = config.get('power_bi_api', 'client_id')
redirect_uri = config.get('power_bi_api', 'redirect_uri')
client_secret = config.get('power_bi_api', 'client_secret')

# Initialize the Client.
power_bi_client = PowerBiClient(
    client_id=client_id,
    client_secret=client_secret,
    scope=['https://analysis.windows.net/powerbi/api/.default'],
    redirect_uri=redirect_uri,
    credentials='config/power_bi_state.jsonc'
)

# Initialize the `Dashboards` service.
dashboard_service = power_bi_client.dashboards()

# Add a dashboard to our Workspace.
dashboard_service.add_dashboard(name='my_new_dashboard')

# Get all the dashboards in our Org.
pprint(dashboard_service.get_dashboards())
```

## Support These Projects

**Patreon:**
Help support this project and future projects by donating to my [Patreon Page](https://www.patreon.com/sigmacoding). I'm
always looking to add more content for individuals like yourself, unfortuantely some of the APIs I would require me to
pay monthly fees.

**YouTube:**
If you'd like to watch more of my content, feel free to visit my YouTube channel [Sigma Coding](https://www.youtube.com/c/SigmaCoding).

**Questions:**
If you have questions please feel free to reach out to me at [coding.sigma@gmail.com](mailto:coding.sigma@gmail.com?subject=[GitHub]%20Fred%20Library)
