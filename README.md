# Wifi pro plug proxy
Proxy to read data from Wifi Plug Pro (EASun, Powland, ISolar) inverters.

The project contains example setups for Home Assistant mqtt device, and Kubernetes deployment with Prometheus.

## Pre-requirements

Configure DNS setting to point ```ess.eybond.com``` to your proxy.

## Simple setup

Update or comment mqtt settings. 
Prometheus metrics can be accessed on port 5000.

```
    pip install -r .\requirements.txt
    python main.py

    or

    docker-compose up -d
```