# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from .. import try_manual


# EXAMPLE: /ServerGroups/put/Create a new server group
@try_manual
def step_server_group_create(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server-group create '
             '--location "westus" '
             '--administrator-login "citus" '
             '--administrator-login-password "password" '
             '--availability-zone "1" '
             '--backup-retention-days 35 '
             '--citus-version "9.5" '
             '--subnet-arm-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg_2}/providers/Microsoft.Netw'
             'ork/virtualNetworks/{vn}/subnets/default" '
             '--enable-mx true '
             '--enable-zfs false '
             '--postgresql-version "12" '
             '--server-role-groups name="" enable-ha=true role="Coordinator" server-count=1 '
             'server-edition="GeneralPurpose" storage-quota-in-mb=524288 v-cores=4 '
             '--server-role-groups name="" enable-ha=false role="Worker" server-count=3 server-edition="MemoryOptimized'
             '" storage-quota-in-mb=524288 v-cores=4 '
             '--standby-availability-zone "2" '
             '--tags ElasticServer="1" '
             '--resource-group "{rg}" '
             '--name "{myServerGroup2}"',
             checks=checks)


# EXAMPLE: /ServerGroups/put/Create a new server group as a point in time restore
@try_manual
def step_server_group_create2(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server-group create '
             '--location "westus" '
             '--create-mode "PointInTimeRestore" '
             '--enable-mx true '
             '--enable-zfs false '
             '--point-in-time-utc "2017-12-14T00:00:37.467Z" '
             '--source-location "eastus" '
             '--source-resource-group-name "SourceGroup" '
             '--source-server-group-name "pgtests-source-server-group" '
             '--source-subscription-id "dddddddd-dddd-dddd-dddd-dddddddddddd" '
             '--resource-group "{rg}" '
             '--name "{myServerGroup2}"',
             checks=checks)


# EXAMPLE: /ServerGroups/put/Create a new server group as a read replica
@try_manual
def step_server_group_create3(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server-group create '
             '--location "westus" '
             '--create-mode "ReadReplica" '
             '--source-location "eastus" '
             '--source-resource-group-name "SourceGroup" '
             '--source-server-group-name "pgtests-source-server-group" '
             '--source-subscription-id "dddddddd-dddd-dddd-dddd-dddddddddddd" '
             '--resource-group "{rg}" '
             '--name "{myServerGroup2}"',
             checks=checks)


# EXAMPLE: /ServerGroups/get/Get the server group
@try_manual
def step_server_group_show(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server-group show '
             '--resource-group "{rg}" '
             '--name "{myServerGroup}"',
             checks=checks)


# EXAMPLE: /ServerGroups/get/List all the server groups
@try_manual
def step_server_group_list(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server-group list '
             '-g ""',
             checks=checks)


# EXAMPLE: /ServerGroups/get/List the server groups by resource group
@try_manual
def step_server_group_list2(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server-group list '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ServerGroups/patch/Add new worker nodes
@try_manual
def step_server_group_update(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server-group update '
             '--location "westus" '
             '--server-role-groups name="" role="Worker" server-count=10 '
             '--resource-group "{rg}" '
             '--name "{myServerGroup2}"',
             checks=checks)


# EXAMPLE: /ServerGroups/patch/Scale compute
@try_manual
def step_server_group_update2(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server-group update '
             '--location "westus" '
             '--server-role-groups name="" role="Coordinator" v-cores=16 '
             '--resource-group "{rg}" '
             '--name "{myServerGroup2}"',
             checks=checks)


# EXAMPLE: /ServerGroups/patch/Scale storage
@try_manual
def step_server_group_update3(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server-group update '
             '--location "westus" '
             '--server-role-groups name="" role="Worker" storage-quota-in-mb=8388608 '
             '--resource-group "{rg}" '
             '--name "{myServerGroup2}"',
             checks=checks)


# EXAMPLE: /ServerGroups/patch/Update customer maintenance window
@try_manual
def step_server_group_update4(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server-group update '
             '--maintenance-window custom-window="Enabled" day-of-week=0 start-hour=8 start-minute=0 '
             '--resource-group "{rg}" '
             '--name "{myServerGroup2}"',
             checks=checks)


# EXAMPLE: /ServerGroups/patch/Update the server group
@try_manual
def step_server_group_update5(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server-group update '
             '--administrator-login-password "secret" '
             '--backup-retention-days 30 '
             '--postgresql-version "12" '
             '--server-role-groups name="" enable-ha=false role="Coordinator" server-count=1 '
             'server-edition="GeneralPurpose" storage-quota-in-mb=1048576 v-cores=8 '
             '--server-role-groups name="" enable-ha=true role="Worker" server-count=4 server-edition="MemoryOptimized"'
             ' storage-quota-in-mb=524288 v-cores=4 '
             '--tags ElasticServer="2" '
             '--resource-group "{rg}" '
             '--name "{myServerGroup2}"',
             checks=checks)


# EXAMPLE: /ServerGroups/post/Restart all servers in the server group
@try_manual
def step_server_group_restart(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server-group restart '
             '--resource-group "{rg}" '
             '--name "{myServerGroup}"',
             checks=checks)


# EXAMPLE: /ServerGroups/post/Start all servers in the server group
@try_manual
def step_server_group_start(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server-group start '
             '--resource-group "{rg}" '
             '--name "{myServerGroup}"',
             checks=checks)


# EXAMPLE: /ServerGroups/post/Stop all servers in the server group
@try_manual
def step_server_group_stop(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server-group stop '
             '--resource-group "{rg}" '
             '--name "{myServerGroup}"',
             checks=checks)


# EXAMPLE: /FirewallRules/put/Create a firewall rule of the server group
@try_manual
def step_firewall_rule_create(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc firewall-rule create '
             '--name "{myFirewallRule}" '
             '--end-ip-address "255.255.255.255" '
             '--start-ip-address "0.0.0.0" '
             '--resource-group "{rg}" '
             '--server-group-name "{myServerGroup4}"',
             checks=checks)


# EXAMPLE: /FirewallRules/get/Get the firewall rule of the server group
@try_manual
def step_firewall_rule_show(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc firewall-rule show '
             '--name "{myFirewallRule}" '
             '--resource-group "{rg}" '
             '--server-group-name "{myServerGroup4}"',
             checks=checks)


# EXAMPLE: /FirewallRules/get/List firewall rules of the server group
@try_manual
def step_firewall_rule_list(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc firewall-rule list '
             '--resource-group "{rg}" '
             '--server-group-name "{myServerGroup4}"',
             checks=checks)


# EXAMPLE: /FirewallRules/delete/Delete the firewall rule of the server group
@try_manual
def step_firewall_rule_delete(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc firewall-rule delete -y '
             '--name "{myFirewallRule}" '
             '--resource-group "{rg}" '
             '--server-group-name "{myServerGroup4}"',
             checks=checks)


# EXAMPLE: /Roles/put/RoleCreate
@try_manual
def step_role_create(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc role create '
             '--password "secret" '
             '--resource-group "{rg}" '
             '--name "{myRole}" '
             '--server-group-name "{myServerGroup4}"',
             checks=checks)


# EXAMPLE: /Roles/get/RoleList
@try_manual
def step_role_list(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc role list '
             '--resource-group "{rg}" '
             '--server-group-name "{myServerGroup4}"',
             checks=checks)


# EXAMPLE: /Roles/delete/RoleDelete
@try_manual
def step_role_delete(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc role delete -y '
             '--resource-group "{rg}" '
             '--name "{myRole}" '
             '--server-group-name "{myServerGroup4}"',
             checks=checks)


# EXAMPLE: /Servers/get/Get the server of server group
@try_manual
def step_server_show(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server show '
             '--resource-group "{rg}" '
             '--server-group-name "{myServerGroup}" '
             '--name "{myServer}"',
             checks=checks)


# EXAMPLE: /Servers/get/List servers of the server group
@try_manual
def step_server_list(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server list '
             '--resource-group "{rg}" '
             '--server-group-name "{myServerGroup}"',
             checks=checks)


# EXAMPLE: /Configurations/get/Get single configuration of the server group
@try_manual
def step_configuration_show(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc configuration show '
             '--name "{myConfiguration}" '
             '--resource-group "{rg_3}" '
             '--server-group-name "{myServerGroup2}"',
             checks=checks)


# EXAMPLE: /Configurations/get/List configurations of the server group
@try_manual
def step_configuration_list(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc configuration list '
             '--resource-group "{rg_3}" '
             '--server-group-name "{myServerGroup2}"',
             checks=checks)


# EXAMPLE: /Configurations/get/List configurations of the server that in the server group
@try_manual
def step_configuration_list2(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc configuration list '
             '--resource-group "{rg_3}" '
             '--server-group-name "{myServerGroup2}" '
             '--server-name "{myServer2}"',
             checks=checks)


# EXAMPLE: /Configurations/patch/Update single configuration of the server group
@try_manual
def step_configuration_update(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc configuration update '
             '--name "{myConfiguration}" '
             '--server-role-group-configurations role="Coordinator" value="on" '
             '--server-role-group-configurations role="Worker" value="off" '
             '--resource-group "{rg_3}" '
             '--server-group-name "{myServerGroup2}"',
             checks=checks)


# EXAMPLE: /ServerGroups/delete/Delete the server group
@try_manual
def step_server_group_delete(test, rg_2, rg, rg_3, checks=None):
    if checks is None:
        checks = []
    test.cmd('az postgresqlhsc server-group delete -y '
             '--resource-group "{rg}" '
             '--name "{myServerGroup3}"',
             checks=checks)

