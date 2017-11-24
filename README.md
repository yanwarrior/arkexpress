## arkexpress

Client library for communicating with of the Ark Express for Delivery Shipping.

### Notes

```
This is still an early release and does not provide access to all the
functionality of the Ark Express API NOAH.  Currently, only submitting
track delivery.
```

### Links

* `Ark Express website <https://track.ark-xpress.com/cp/>`_

### Installation
Open your terminal and type the following command:

```
$ python setup.py install
```

### Quick Start
Simple example to use:

```
>>> from arkexpress import ark
>>> 
>>> arks = ark.ArkExpress(service=ark.ArkExpress.SERVICE_SHIPMENT)
>>> shipment = arks.service(
   ...     grant_type='<client_grandtype>',
   ...     client_id='<client_id>',
   ...     secret_key='<secret_key>',
   ...     waybill='000412017113433212')     
>>>
>>> shipment.get_info()
```

This output:

```
[{'reference_no': None,
  'status': 'success',
  'track_trace': [{'code': '110',
    'datetime': '2017-11-23 22:54:12.250315',
    'description': 'WAYBILL CREATED'},
   {'code': '220',
    'datetime': '2017-11-23 23:49:26.345582',
    'description': 'RECEIVED AT ORIGIN STATION'},
   {'code': '440',
    'datetime': '2017-11-24 06:13:36.039816',
    'description': '1ST DELIVERY ON PROGRESS'},
   {'code': '450',
    'datetime': '2017-11-24 09:42:31',
    'description': 'DELIVERED'}],
  'waybill': '00041201711211515'}]
```

