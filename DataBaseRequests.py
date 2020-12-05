import requests


class DBConnector:
    def __init__(self, URL: str, port: int):
        self.URL = URL
        self.port = port
        self.URL_BASE = "http://" + URL+":"+str(port)+"/v1"

    def getClients(self):
        namespace = 'test'
        setname = 'clients'
        KVS_ENDPOINT = self.URL_BASE + '/scan'

        record_uri = '{base}/{ns}/{setname}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname)
        print(record_uri)
        response = requests.get(record_uri)
        return response.json()['records']

    def setClient(self, key, bins):
        namespace = 'test'
        setname = 'clients'
        userkey = 'key' + str(key)
        KVS_ENDPOINT = self.URL_BASE + '/kvs'
        record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
        response = requests.post(record_uri, json=bins)
        return response.ok

    def editClient(self, key, bins):
        namespace = 'test'
        setname = 'clients'
        userkey = 'key' + str(key)
        KVS_ENDPOINT = self.URL_BASE + '/kvs'
        record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
        response = requests.put(record_uri, json=bins)
        return response.ok

    def getClient(self, key):
        namespace = 'test'
        setname = 'clients'
        userkey = 'key' + str(key)
        KVS_ENDPOINT = self.URL_BASE + '/kvs'
        record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
        response = requests.get(record_uri)
        if response.ok:
            return response.json()['bins']
        else:
            return -1

    def deleteAllClients(self):
        clients = self.getClients()
        for cl in clients:
            key = cl['bins']['ID']
            namespace = 'test'
            setname = 'clients'
            userkey = 'key' + str(key)
            KVS_ENDPOINT = self.URL_BASE + '/kvs'
            record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
                base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
            response = requests.delete(record_uri)
        # print(response.text)
        # print(response.ok)

    def deleteClient(self, key):
        namespace = 'test'
        setname = 'clients'
        userkey = 'key' + str(key)
        KVS_ENDPOINT = self.URL_BASE + '/kvs'
        record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
        response = requests.delete(record_uri)
        # print(response.text)
        # print(response.ok)

    def getSignal(self, key):
        namespace = 'test'
        setname = 'clients'
        userkey = 'key' + str(key)
        KVS_ENDPOINT = self.URL_BASE + '/kvs'
        record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
        response = requests.get(record_uri)
        if response.ok:
            mes = response.json()
            return mes['bins']['Flag']
            # print(response.json())
        else:
            return -1

    def setClientSignal(self, ID, sig):
        bins = self.getClient(ID)
        bins['Flag'] = sig
        namespace = 'test'
        setname = 'clients'
        userkey = 'key' + str(ID)
        KVS_ENDPOINT = self.URL_BASE + '/kvs'
        record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
        response = requests.put(record_uri, json=bins)
        # print(response.text)
        # print(response.ok)
        return response.ok

    def getActiveAndStop(self, key):
        namespace = 'test'
        setname = 'clients'
        userkey = 'key' + str(key)
        KVS_ENDPOINT = self.URL_BASE + '/kvs'
        record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
        response = requests.get(record_uri)
        if response.ok:
            mes = response.json()
            ret = [mes['bins']['Active'], mes['bins']['Stop_on_execute']]
            return ret
            # print(response.json())
        else:
            return -1

    def getActiveStopSignal(self, key):
        namespace = 'test'
        setname = 'clients'
        userkey = 'key' + str(key)
        KVS_ENDPOINT = self.URL_BASE + '/kvs'
        record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
        response = requests.get(record_uri)
        if response.ok:
            mes = response.json()
            ret = [mes['bins']['Active'], mes['bins']['Stop_on_execute'], mes['bins']['Flag']]
            return ret
            # print(response.json())
        else:
            return -1

    def getActive(self, key):
        namespace = 'test'
        setname = 'clients'
        userkey = 'key' + str(key)
        KVS_ENDPOINT = self.URL_BASE + '/kvs'
        record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
        response = requests.get(record_uri)
        if response.ok:
            mes = response.json()
            return mes['bins']['Active']
            # print(response.json())
        else:
            return -1

    def getStop(self, key):
        namespace = 'test'
        setname = 'clients'
        userkey = 'key' + str(key)
        KVS_ENDPOINT = self.URL_BASE + '/kvs'
        record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
        response = requests.get(record_uri)
        if response.ok:
            mes = response.json()
            return mes['bins']['Stop_on_execute']
            # print(response.json())
        else:
            return -1

    def checkKeyClient(self, key):
        namespace = 'test'
        setname = 'clients'
        userkey = 'key'+str(key)
        KVS_ENDPOINT = self.URL_BASE + '/kvs'
        record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
        response = requests.get(record_uri)
        if 'message' in response.json():
            if (response.json()['message']) == 'Record not found':
                return False
        else:
            return True

    def changeFlagNull(self, ID):
        bins = self.getClient(ID)
        bins['Change_fl'] = 0
        namespace = 'test'
        setname = 'clients'
        userkey = 'key' + str(ID)
        KVS_ENDPOINT = self.URL_BASE + '/kvs'
        record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
        response = requests.put(record_uri, json=bins)
        # print(response.text)
        # print(response.ok)
        return response.ok

    def changeFlagTrue(self, ID):
        bins = self.getClient(ID)
        bins['Change_fl'] = 1
        namespace = 'test'
        setname = 'clients'
        userkey = 'key' + str(ID)
        KVS_ENDPOINT = self.URL_BASE + '/kvs'
        record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
        response = requests.put(record_uri, json=bins)
        # print(response.text)
        # print(response.ok)
        return response.ok

    def signalFlagNull(self, ID):
        bins = self.getClient(ID)
        bins['Flag'] = 0
        bins['Change_fl'] = 1
        namespace = 'test'
        setname = 'clients'
        userkey = 'key' + str(ID)
        KVS_ENDPOINT = self.URL_BASE + '/kvs'
        record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
        response = requests.put(record_uri, json=bins)
        # print(response.text)
        # print(response.ok)
        return response.ok

    def deactivateClient(self, ID):
        bins = self.getClient(ID)
        bins['Active'] = 0
        bins['Change_fl'] = 1
        namespace = 'test'
        setname = 'clients'
        userkey = 'key' + str(ID)
        KVS_ENDPOINT = self.URL_BASE + '/kvs'
        record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
        response = requests.put(record_uri, json=bins)
        # print(response.text)
        # print(response.ok)
        return response.ok

    def activateClient(self, ID):
        bins = self.getClient(ID)
        bins['Active'] = 1
        bins['Change_fl'] = 1
        namespace = 'test'
        setname = 'clients'
        userkey = 'key' + str(ID)
        KVS_ENDPOINT = self.URL_BASE + '/kvs'
        record_uri = '{base}/{ns}/{setname}/{userkey}'.format(
            base=KVS_ENDPOINT, ns=namespace, setname=setname, userkey=userkey)
        response = requests.put(record_uri, json=bins)
        # print(response.text)
        # print(response.ok)
        return response.ok