# Auditory Cortex
The primary auditory cortex is the part of the temporal lobe that processes auditory information in humans, other vertebrates and in [Matilda](http://matilda.edwardleoni.com).

In boring terms, this is a minimalist Python app that handles speech-to-text.


## Installation
As this is directly tied to Google Speech Cloud, you will need a service account key file from https://console.cloud.google.com/iam-admin/serviceaccounts/project?project=MY_PROJECT. Google will give you a json file, name it `matilda.json` and put in the root folder.

### Docker
#### Build
`docker build . -t auditory`

#### One-off run
`docker run --name auditory-cortex -p 5003:5000 auditory`
