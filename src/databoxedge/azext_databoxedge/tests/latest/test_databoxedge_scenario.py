# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from .. import try_manual, raise_if, calc_coverage
from azure.cli.testsdk import ResourceGroupPreparer
from azure.cli.testsdk import StorageAccountPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup
@try_manual
def setup(test, rg, rg_3, rg_2):
    pass


# EXAMPLE: DataBoxEdgeDevicePut
@try_manual
def step_databoxedgedeviceput(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge device create '
             '--location "eastus" '
             '--sku name="Edge" tier="Standard" '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("location", "eastus", case_sensitive=False),
                 test.check("sku.name", "Edge", case_sensitive=False),
                 test.check("sku.tier", "Standard", case_sensitive=False),
                 test.check("name", "{myDevice}", case_sensitive=False),
             ])


# EXAMPLE: UserPut
@try_manual
def step_userput(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge user create '
             '--name "user1" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}" '
             '--encrypted-password encryption-algorithm="None" encryption-cert-thumbprint="blah" value="Password@1" '
             '--user-type "Share"',
             checks=[])


# EXAMPLE: RolePut
@try_manual
def step_roleput(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge role create '
             '--name "IoTRole1" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}" '
             '--role "{{\\"kind\\":\\"IOT\\",\\"properties\\":{{\\"hostPlatform\\":\\"Linux\\",\\"ioTDeviceDetails\\":{'
             '{\\"authentication\\":{{\\"symmetricKey\\":{{\\"connectionString\\":{{\\"encryptionAlgorithm\\":\\"AES256'
             '\\",\\"encryptionCertThumbprint\\":\\"348586569999244\\",\\"value\\":\\"Encrypted<<HostName=iothub.azure-'
             'devices.net;DeviceId=iotDevice;SharedAccessKey=2C750FscEas3JmQ8Bnui5yQWZPyml0/UiRt1bQwd8=>>\\"}}}}}},\\"d'
             'eviceId\\":\\"iotdevice\\",\\"ioTHostHub\\":\\"iothub.azure-devices.net\\"}},\\"ioTEdgeDeviceDetails\\":{'
             '{\\"authentication\\":{{\\"symmetricKey\\":{{\\"connectionString\\":{{\\"encryptionAlgorithm\\":\\"AES256'
             '\\",\\"encryptionCertThumbprint\\":\\"1245475856069999244\\",\\"value\\":\\"Encrypted<<HostName=iothub.az'
             'ure-devices.net;DeviceId=iotEdge;SharedAccessKey=2C750FscEas3JmQ8Bnui5yQWZPyml0/UiRt1bQwd8=>>\\"}}}}}},\\'
             '"deviceId\\":\\"iotEdge\\",\\"ioTHostHub\\":\\"iothub.azure-devices.net\\"}},\\"roleStatus\\":\\"Enabled'
             '\\",\\"shareMappings\\":[]}}}}"',
             checks=[])


# EXAMPLE: SharePut
@try_manual
def step_shareput(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge share create '
             '--name "smbshare" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}" '
             '--description "" '
             '--access-protocol "SMB" '
             '--azure-container-info container-name="testContainerSMB" data-format="BlockBlob" '
             'storage-account-credential-id="/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.D'
             'ataBoxEdge/dataBoxEdgeDevices/{{myDevice}}/storageAccountCredentials/{myStorageAccountCredentials}" '
             '--data-policy "Cloud" '
             '--monitoring-status "Enabled" '
             '--share-status "Online" '
             '--user-access-rights access-type="Change" user-id="/subscriptions/{subscription_id}/resourceGroups/{rg}/p'
             'roviders/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{{myDevice}}/users/{myUser}"',
             checks=[])


# EXAMPLE: OrderPut
@try_manual
def step_orderput(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge order create '
             '--device-name "{myDevice}" '
             '--contact-information company-name="Microsoft" contact-person="John Mcclane" '
             'email-list="john@microsoft.com" phone="(800) 426-9400" '
             '--shipping-address address-line1="Microsoft Corporation" address-line2="One Microsoft Way" '
             'address-line3="Redmond" city="WA" country="USA" postal-code="98052" state="WA" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: TriggerPut
@try_manual
def step_triggerput(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge trigger create '
             '--name "trigger1" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}" '
             '--file-event-trigger custom-context-tag="CustomContextTags-1235346475"',
             checks=[])


# EXAMPLE: StorageAccountPut
@try_manual
def step_storageaccountput(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge storage-account create '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}" '
             '--description "It\'s an awesome storage account" '
             '--data-policy "Cloud" '
             '--storage-account-credential-id "/subscriptions/{subscription_id}/resourceGroups/{rg_3}/providers/Microso'
             'ft.DataBoxEdge/dataBoxEdgeDevices/{myDevice}/storageAccountCredentials/{myStorageAccountCredentials2}" '
             '--storage-account-status "OK" '
             '--name "{sa}"',
             checks=[])


# EXAMPLE: BandwidthSchedulePut
@try_manual
def step_bandwidthscheduleput(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge bandwidth-schedule create '
             '--name "bandwidth-1" '
             '--device-name "{myDevice}" '
             '--days "Sunday" '
             '--days "Monday" '
             '--rate-in-mbps 100 '
             '--start "0:0:0" '
             '--stop "13:59:0" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: SACPut
@try_manual
def step_sacput(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge storage-account-credentials create '
             '--name "{myStorageAccountCredentials}" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}" '
             '--account-key encryption-algorithm="AES256" encryption-cert-thumbprint="2A9D8D6BE51574B5461230AEF02F162C5'
             'F01AD31" value="lAeZEYi6rNP1/EyNaVUYmTSZEYyaIaWmwUsGwek0+xiZj54GM9Ue9/UA2ed/ClC03wuSit2XzM/cLRU5eYiFBwks2'
             '3rGwiQOr3sruEL2a74EjPD050xYjA6M1I2hu/w2yjVHhn5j+DbXS4Xzi+rHHNZK3DgfDO3PkbECjPck+PbpSBjy9+6Mrjcld5DIZhUAeM'
             'lMHrFlg+WKRKB14o/og56u5/xX6WKlrMLEQ+y6E18dUwvWs2elTNoVO8PBE8SM/CfooX4AMNvaNdSObNBPdP+F6Lzc556nFNWXrBLRt0v'
             'C7s9qTiVRO4x/qCNaK/B4y7IqXMllwQFf4Np9UQ2ECA '
             '--account-type "BlobStorage" '
             '--alias "{myStorageAccountCredentials}" '
             '--ssl-status "Disabled" '
             '--user-name "{myUser2}"',
             checks=[])


# EXAMPLE: ContainerPut
@try_manual
def step_containerput(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge container create '
             '--data-format "BlockBlob" '
             '--name "{myContainer}" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}" '
             '--storage-account-name "{sa_2}"',
             checks=[
                 test.check("dataFormat", "BlockBlob", case_sensitive=False),
             ])


# EXAMPLE: ContainerGet
@try_manual
def step_containerget(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge container show '
             '--name "{myContainer}" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}" '
             '--storage-account-name "{sa_2}"',
             checks=[
                 test.check("dataFormat", "BlockBlob", case_sensitive=False),
                 test.check("name", "{myContainer}", case_sensitive=False),
             ])


# EXAMPLE: SACGet
@try_manual
def step_sacget(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge storage-account-credentials show '
             '--name "{myStorageAccountCredentials}" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ContainerListAllInDevice
@try_manual
def step_containerlistallindevice(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge container list '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}" '
             '--storage-account-name "{sa_2}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: BandwidthScheduleGet
@try_manual
def step_bandwidthscheduleget(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge bandwidth-schedule show '
             '--name "bandwidth-1" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: OperationsStatusGet
@try_manual
def step_operationsstatusget(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge operation-status show '
             '--name "159a00c7-8543-4343-9435-263ac87df3bb" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: StorageAccountGet
@try_manual
def step_storageaccountget(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge storage-account show '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}" '
             '--name "{sa}"',
             checks=[])


# EXAMPLE: NetworkSettingsGet
@try_manual
def step_networksettingsget(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge device get-network-setting '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: UpdateSummaryGet
@try_manual
def step_updatesummaryget(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge device get-update-summary '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: TriggerGet
@try_manual
def step_triggerget(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge trigger show '
             '--name "trigger1" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: SACGetAllInDevice
@try_manual
def step_sacgetallindevice(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge storage-account-credentials list '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: AlertGet
@try_manual
def step_alertget(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge alert show '
             '--name "159a00c7-8543-4343-9435-263ac87df3bb" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ShareGet
@try_manual
def step_shareget(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge share show '
             '--name "smbshare" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: OrderGet
@try_manual
def step_orderget(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge order show '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: UserGet
@try_manual
def step_userget(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge user show '
             '--name "user1" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: RoleGet
@try_manual
def step_roleget(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge role show '
             '--name "IoTRole1" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: JobsGet
@try_manual
def step_jobsget(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge job show '
             '--name "159a00c7-8543-4343-9435-263ac87df3bb" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: BandwidthScheduleGetAllInDevice
@try_manual
def step_bandwidthschedulegetallindevice(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge bandwidth-schedule list '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: StorageAccountGetAllInDevice
@try_manual
def step_storageaccountgetallindevice(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge storage-account list '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: TriggerGetAllInDevice
@try_manual
def step_triggergetallindevice(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge trigger list '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: OrderGetAllInDevice
@try_manual
def step_ordergetallindevice(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge order list '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: AlertGetAllInDevice
@try_manual
def step_alertgetallindevice(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge alert list '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ShareGetAllInDevice
@try_manual
def step_sharegetallindevice(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge share list '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: NodesGetAllInDevice
@try_manual
def step_nodesgetallindevice(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge node list '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: RoleGetAllInDevice
@try_manual
def step_rolegetallindevice(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge role list '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: UserGetAllInDevice
@try_manual
def step_usergetallindevice(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge user list '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: DataBoxEdgeDeviceGetByName
@try_manual
def step_databoxedgedevicegetbyname(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge device show '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("location", "eastus", case_sensitive=False),
                 test.check("sku.name", "Edge", case_sensitive=False),
                 test.check("sku.tier", "Standard", case_sensitive=False),
                 test.check("name", "{myDevice}", case_sensitive=False),
             ])


# EXAMPLE: DataBoxEdgeDeviceGetByResourceGroup
@try_manual
def step_databoxedgedevicegetbyresourcegroup(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge device list '
             '--resource-group "{rg}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: DataBoxEdgeDeviceGetBySubscription
@try_manual
def step_databoxedgedevicegetbysubscription(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge device list '
             '-g ""',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: ListSkus
@try_manual
def step_listskus(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge sku list',
             checks=[])


# EXAMPLE: ListAvailableSkus
@try_manual
def step_listavailableskus(test, rg, rg_3, rg_2):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: OperationsGet
@try_manual
def step_operationsget(test, rg, rg_3, rg_2):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: ContainerRefresh
@try_manual
def step_containerrefresh(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge container refresh '
             '--name "{myContainer}" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}" '
             '--storage-account-name "{sa_2}"',
             checks=[])


# EXAMPLE: CreateOrUpdateSecuritySettings
@try_manual
def step_createorupdatesecuritysettings(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge device create-or-update-security-setting '
             '--name "{myDevice}" '
             '--resource-group "{rg_2}" '
             '--device-admin-password encryption-algorithm="AES256" encryption-cert-thumbprint="7DCBDFC44ED968D232C9A99'
             '8FC105B5C70E84BE0" value="jJ5MvXa/AEWvwxviS92uCjatCXeyLYTy8jx/k105MjQRXT7i6Do8qpEcQ8d+OBbwmQTnwKW0CYyzzVR'
             'Cc0uZcPCf6PsWtP4l6wvcKGAP66PwK68eEkTUOmp+wUHc4hk02kWmTWeAjBZkuDBP3xK1RnZo95g2RE4i1UgKNP5BEKCLd71O104DW3AW'
             'W41mh9XLWNOaxw+VjQY7wmvlE6XkvpkMhcGuha2u7lx8zi9ZkcMvJVYDYK36Fb/K3KhBAmDjjDmVq04jtBlcSTXQObt0nlj4BwGGtdrpe'
             'Ipr67zqr5i3cPm6e6AleIaIhp6sI/uyGSMiT3oev2eg49u2ii7kVA',
             checks=[])


# EXAMPLE: ShareRefreshPost
@try_manual
def step_sharerefreshpost(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge share refresh '
             '--name "smbshare" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ExtendedInfoPost
@try_manual
def step_extendedinfopost(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge device get-extended-information '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: UploadCertificatePost
@try_manual
def step_uploadcertificatepost(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge device upload-certificate '
             '--name "{myDevice}" '
             '--certificate "MIIC9DCCAdygAwIBAgIQWJae7GNjiI9Mcv/gJyrOPTANBgkqhkiG9w0BAQUFADASMRAwDgYDVQQDDAdXaW5kb3dzMB'
             '4XDTE4MTEyNzAwMTA0NVoXDTIxMTEyODAwMTA0NVowEjEQMA4GA1UEAwwHV2luZG93czCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQo'
             'CggEBAKxkRExqxf0qH1avnyORptIbRC2yQwqe3EIbJ2FPKr5jtAppGeX/dGKrFSnX+7/0HFr77aJHafdpEAtOiLyJ4zCAVs0obZCCIq4q'
             'JdmjYUTU0UXH/w/YzXfQA0d9Zh9AN+NJBX9xj05NzgsT24fkgsK2v6mWJQXT7YcWAsl5sEYPnx1e+MrupNyVSL/RUJmrS+etJSysHtFeW'
             'RhsUhVAs1DD5ExJvBLU3WH0IsojEvpXcjrutB5/MDQNrd/StGI6WovoSSPH7FyT9tgERx+q+Yg3YUGzfaIPCctlrRGehcdtzdNoKd0rsX'
             '62yCq0U6POoSfwe22NJu41oAUMd7e6R8cCAwEAAaNGMEQwEwYDVR0lBAwwCgYIKwYBBQUHAwIwHQYDVR0OBBYEFDd0VxnS3LnMIfwc7xW'
             '4b4IZWG5GMA4GA1UdDwEB/wQEAwIFIDANBgkqhkiG9w0BAQUFAAOCAQEAPQRby2u9celvtvL/DLEb5Vt3/tPStRQC5MyTD62L5RT/q8E6'
             'EMCXVZNkXF5WlWucLJi/18tY+9PNgP9xWLJh7kpSWlWdi9KPtwMqKDlEH8L2TnQdjimt9XuiCrTnoFy/1X2BGLY/rCaUJNSd15QCkz2xe'
             'W+Z+YSk2GwAc/A/4YfNpqSIMfNuPrT76o02VdD9WmJUA3fS/HY0sU9qgQRS/3F5/0EPS+HYQ0SvXCK9tggcCd4O050ytNBMJC9qMOJ7yE'
             '0iOrFfOJSCfDAuPhn/rHFh79Kn1moF+/CE+nc0/2RPiLC8r54/rt5dYyyxJDfXg0a3VrrX39W69WZGW5OXiw==" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: DownloadUpdatesPost
@try_manual
def step_downloadupdatespost(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge device download-update '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ScanForUpdatesPost
@try_manual
def step_scanforupdatespost(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge device scan-for-update '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: InstallUpdatesPost
@try_manual
def step_installupdatespost(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge device install-update '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: DataBoxEdgeDevicePatch
@try_manual
def step_databoxedgedevicepatch(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge device update '
             '--name "{myDevice}" '
             '--tags Key1="value1" Key2="value2" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myDevice}", case_sensitive=False),
                 test.check("tags.Key1", "value1", case_sensitive=False),
                 test.check("tags.Key2", "value2", case_sensitive=False),
             ])


# EXAMPLE: ContainerDelete
@try_manual
def step_containerdelete(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge container delete -y '
             '--name "{myContainer}" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}" '
             '--storage-account-name "{sa_2}"',
             checks=[])


# EXAMPLE: SACDelete
@try_manual
def step_sacdelete(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge storage-account-credentials delete -y '
             '--name "{myStorageAccountCredentials}" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: BandwidthScheduleDelete
@try_manual
def step_bandwidthscheduledelete(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge bandwidth-schedule delete -y '
             '--name "bandwidth-1" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: StorageAccountDelete
@try_manual
def step_storageaccountdelete(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge storage-account delete -y '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}" '
             '--name "{sa_2}"',
             checks=[])


# EXAMPLE: TriggerDelete
@try_manual
def step_triggerdelete(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge trigger delete -y '
             '--name "trigger1" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ShareDelete
@try_manual
def step_sharedelete(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge share delete -y '
             '--name "smbshare" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: OrderDelete
@try_manual
def step_orderdelete(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge order delete -y '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: UserDelete
@try_manual
def step_userdelete(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge user delete -y '
             '--name "user1" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: RoleDelete
@try_manual
def step_roledelete(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge role delete -y '
             '--name "IoTRole1" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: DataBoxEdgeDeviceDelete
@try_manual
def step_databoxedgedevicedelete(test, rg, rg_3, rg_2):
    test.cmd('az databoxedge device delete -y '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=[])


# Env cleanup
@try_manual
def cleanup(test, rg, rg_3, rg_2):
    pass


# Testcase
@try_manual
def call_scenario(test, rg, rg_3, rg_2):
    setup(test, rg, rg_3, rg_2)
    step_databoxedgedeviceput(test, rg, rg_3, rg_2)
    step_userput(test, rg, rg_3, rg_2)
    step_roleput(test, rg, rg_3, rg_2)
    step_shareput(test, rg, rg_3, rg_2)
    step_orderput(test, rg, rg_3, rg_2)
    step_triggerput(test, rg, rg_3, rg_2)
    step_storageaccountput(test, rg, rg_3, rg_2)
    step_bandwidthscheduleput(test, rg, rg_3, rg_2)
    step_sacput(test, rg, rg_3, rg_2)
    step_containerput(test, rg, rg_3, rg_2)
    step_containerget(test, rg, rg_3, rg_2)
    step_sacget(test, rg, rg_3, rg_2)
    step_containerlistallindevice(test, rg, rg_3, rg_2)
    step_bandwidthscheduleget(test, rg, rg_3, rg_2)
    step_operationsstatusget(test, rg, rg_3, rg_2)
    step_storageaccountget(test, rg, rg_3, rg_2)
    step_networksettingsget(test, rg, rg_3, rg_2)
    step_updatesummaryget(test, rg, rg_3, rg_2)
    step_triggerget(test, rg, rg_3, rg_2)
    step_sacgetallindevice(test, rg, rg_3, rg_2)
    step_alertget(test, rg, rg_3, rg_2)
    step_shareget(test, rg, rg_3, rg_2)
    step_orderget(test, rg, rg_3, rg_2)
    step_userget(test, rg, rg_3, rg_2)
    step_roleget(test, rg, rg_3, rg_2)
    step_jobsget(test, rg, rg_3, rg_2)
    step_bandwidthschedulegetallindevice(test, rg, rg_3, rg_2)
    step_storageaccountgetallindevice(test, rg, rg_3, rg_2)
    step_triggergetallindevice(test, rg, rg_3, rg_2)
    step_ordergetallindevice(test, rg, rg_3, rg_2)
    step_alertgetallindevice(test, rg, rg_3, rg_2)
    step_sharegetallindevice(test, rg, rg_3, rg_2)
    step_nodesgetallindevice(test, rg, rg_3, rg_2)
    step_rolegetallindevice(test, rg, rg_3, rg_2)
    step_usergetallindevice(test, rg, rg_3, rg_2)
    step_databoxedgedevicegetbyname(test, rg, rg_3, rg_2)
    step_databoxedgedevicegetbyresourcegroup(test, rg, rg_3, rg_2)
    step_databoxedgedevicegetbysubscription(test, rg, rg_3, rg_2)
    step_listskus(test, rg, rg_3, rg_2)
    step_listavailableskus(test, rg, rg_3, rg_2)
    step_operationsget(test, rg, rg_3, rg_2)
    step_containerrefresh(test, rg, rg_3, rg_2)
    step_createorupdatesecuritysettings(test, rg, rg_3, rg_2)
    step_sharerefreshpost(test, rg, rg_3, rg_2)
    step_extendedinfopost(test, rg, rg_3, rg_2)
    step_uploadcertificatepost(test, rg, rg_3, rg_2)
    step_downloadupdatespost(test, rg, rg_3, rg_2)
    step_scanforupdatespost(test, rg, rg_3, rg_2)
    step_installupdatespost(test, rg, rg_3, rg_2)
    step_databoxedgedevicepatch(test, rg, rg_3, rg_2)
    step_containerdelete(test, rg, rg_3, rg_2)
    step_sacdelete(test, rg, rg_3, rg_2)
    step_bandwidthscheduledelete(test, rg, rg_3, rg_2)
    step_storageaccountdelete(test, rg, rg_3, rg_2)
    step_triggerdelete(test, rg, rg_3, rg_2)
    step_sharedelete(test, rg, rg_3, rg_2)
    step_orderdelete(test, rg, rg_3, rg_2)
    step_userdelete(test, rg, rg_3, rg_2)
    step_roledelete(test, rg, rg_3, rg_2)
    step_databoxedgedevicedelete(test, rg, rg_3, rg_2)
    cleanup(test, rg, rg_3, rg_2)


@try_manual
class DataBoxEdgeManagementClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestdataboxedge_GroupForEdgeAutomation'[:7], key='rg', parameter_name='rg')
    @ResourceGroupPreparer(name_prefix='clitestdataboxedge_GroupForDataBoxEdgeAutomation'[:7], key='rg_3',
                           parameter_name='rg_3')
    @ResourceGroupPreparer(name_prefix='clitestdataboxedge_AzureVM'[:7], key='rg_2', parameter_name='rg_2')
    @StorageAccountPreparer(name_prefix='clitestdataboxedge_blobstorageaccount1'[:7], key='sa',
                            resource_group_parameter_name='rg')
    @StorageAccountPreparer(name_prefix='clitestdataboxedge_storageaccount1'[:7], key='sa_2',
                            resource_group_parameter_name='rg')
    def test_databoxedge(self, rg, rg_3, rg_2):

        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myDevice': 'testedgedevice',
            'myContainer': 'blobcontainer1',
            'myUser': 'user2',
            'myUser2': 'cisbvt',
            'myStorageAccountCredentials': 'sac1',
            'myStorageAccountCredentials2': 'cisbvt',
        })

        call_scenario(self, rg, rg_3, rg_2)
        calc_coverage(__file__)
        raise_if()
