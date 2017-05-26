# Auditory Cortex
The primary auditory cortex is the part of the temporal lobe that processes auditory information in humans, other vertebrates and in [Matilda](http://matilda.edwardleoni.com).

In boring terms, this is a minimalist Python app that handles speech-to-text.


## Installation
### Old School
```
pip install -r requirements.txt
export FLASK_APP=/app/app.py; export OWM_TOKEN=$OWM_API_KEY; flask run --host=0.0.0.0 --port=5000
```

### Docker
#### Build
`docker build . -t auditory`

#### One-off run
`docker run --name auditory-cortex -p 5003:5000 auditory`
