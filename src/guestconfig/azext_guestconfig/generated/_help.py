# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['guestconfig guest-configuration-assignment'] = """
    type: group
    short-summary: guestconfig guest-configuration-assignment
"""

helps['guestconfig guest-configuration-assignment list'] = """
    type: command
    short-summary: List all guest configuration assignments for a virtual machine.
    examples:
      - name: List all guest configuration assignments for a virtual machine
        text: |-
               az guestconfig guest-configuration-assignment list --resource-group "myResourceGroupName" --vm-name "myV\
MName"
"""

helps['guestconfig guest-configuration-assignment show'] = """
    type: command
    short-summary: Get information about a guest configuration assignment
    examples:
      - name: Get a guest configuration assignment
        text: |-
               az guestconfig guest-configuration-assignment show --name "SecureProtocol" --resource-group "myResourceG\
roupName" --vm-name "myVMName"
"""

helps['guestconfig guest-configuration-assignment create'] = """
    type: command
    short-summary: Creates an association between a VM and guest configuration
    parameters:
      - name: --guest-configuration-configuration-parameter
        short-summary: The configuration parameters for the guest configuration.
        long-summary: |
            Usage: --guest-configuration-configuration-parameter name=XX value=XX

            name: Name of the configuration parameter.
            value: Value of the configuration parameter.

            Multiple actions can be specified by using more than one --guest-configuration-configuration-parameter argu\
ment.
      - name: --guest-configuration-configuration-setting
        short-summary: The configuration setting for the guest configuration.
        long-summary: |
            Usage: --guest-configuration-configuration-setting configuration-mode=XX allow-module-overwrite=XX action-a\
fter-reboot=XX refresh-frequency-mins=XX reboot-if-needed=XX configuration-mode-frequency-mins=XX

            configuration-mode: Specifies how the LCM(Local Configuration Manager) actually applies the configuration t\
o the target nodes. Possible values are ApplyOnly, ApplyAndMonitor, and ApplyAndAutoCorrect.
            allow-module-overwrite: If true - new configurations downloaded from the pull service are allowed to overwr\
ite the old ones on the target node. Otherwise, false
            action-after-reboot: Specifies what happens after a reboot during the application of a configuration. The p\
ossible values are ContinueConfiguration and StopConfiguration
            refresh-frequency-mins: The time interval, in minutes, at which the LCM checks a pull service to get update\
d configurations. This value is ignored if the LCM is not configured in pull mode. The default value is 30.
            reboot-if-needed: Set this to true to automatically reboot the node after a configuration that requires reb\
oot is applied. Otherwise, you will have to manually reboot the node for any configuration that requires it. The defaul\
t value is false. To use this setting when a reboot condition is enacted by something other than DSC (such as Windows I\
nstaller), combine this setting with the xPendingReboot module.
            configuration-mode-frequency-mins: How often, in minutes, the current configuration is checked and applied.\
 This property is ignored if the ConfigurationMode property is set to ApplyOnly. The default value is 15.
    examples:
      - name: Create or update guest configuration assignment
        text: |-
               az guestconfig guest-configuration-assignment create --guest-configuration-assignment-name "WhitelistedA\
pplication" --guest-configuration-name "WhitelistedApplication" --location "westcentralus" --context "Azure policy" --g\
uest-configuration-name "WhitelistedApplication" --guest-configuration-configuration-parameter name="[InstalledApplicat\
ion]bwhitelistedapp;Name" value="NotePad,sql" --guest-configuration-configuration-setting action-after-reboot="Continue\
Configuration" configuration-mode="MonitorOnly" configuration-mode-frequency-mins=15 reboot-if-needed="False" --guest-c\
onfiguration-version "1.*" --resource-group "myResourceGroupName" --vm-name "myVMName"
"""

helps['guestconfig guest-configuration-assignment update'] = """
    type: command
    short-summary: Creates an association between a VM and guest configuration
    parameters:
      - name: --guest-configuration-configuration-parameter
        short-summary: The configuration parameters for the guest configuration.
        long-summary: |
            Usage: --guest-configuration-configuration-parameter name=XX value=XX

            name: Name of the configuration parameter.
            value: Value of the configuration parameter.

            Multiple actions can be specified by using more than one --guest-configuration-configuration-parameter argu\
ment.
      - name: --guest-configuration-configuration-setting
        short-summary: The configuration setting for the guest configuration.
        long-summary: |
            Usage: --guest-configuration-configuration-setting configuration-mode=XX allow-module-overwrite=XX action-a\
fter-reboot=XX refresh-frequency-mins=XX reboot-if-needed=XX configuration-mode-frequency-mins=XX

            configuration-mode: Specifies how the LCM(Local Configuration Manager) actually applies the configuration t\
o the target nodes. Possible values are ApplyOnly, ApplyAndMonitor, and ApplyAndAutoCorrect.
            allow-module-overwrite: If true - new configurations downloaded from the pull service are allowed to overwr\
ite the old ones on the target node. Otherwise, false
            action-after-reboot: Specifies what happens after a reboot during the application of a configuration. The p\
ossible values are ContinueConfiguration and StopConfiguration
            refresh-frequency-mins: The time interval, in minutes, at which the LCM checks a pull service to get update\
d configurations. This value is ignored if the LCM is not configured in pull mode. The default value is 30.
            reboot-if-needed: Set this to true to automatically reboot the node after a configuration that requires reb\
oot is applied. Otherwise, you will have to manually reboot the node for any configuration that requires it. The defaul\
t value is false. To use this setting when a reboot condition is enacted by something other than DSC (such as Windows I\
nstaller), combine this setting with the xPendingReboot module.
            configuration-mode-frequency-mins: How often, in minutes, the current configuration is checked and applied.\
 This property is ignored if the ConfigurationMode property is set to ApplyOnly. The default value is 15.
    examples:
      - name: Create or update guest configuration assignment
        text: |-
               az guestconfig guest-configuration-assignment update --guest-configuration-assignment-name "WhitelistedA\
pplication" --guest-configuration-name "WhitelistedApplication" --location "westcentralus" --context "Azure policy" --g\
uest-configuration-name "WhitelistedApplication" --guest-configuration-configuration-parameter name="[InstalledApplicat\
ion]bwhitelistedapp;Name" value="NotePad,sql" --guest-configuration-configuration-setting action-after-reboot="Continue\
Configuration" configuration-mode="MonitorOnly" configuration-mode-frequency-mins=15 reboot-if-needed="False" --guest-c\
onfiguration-version "1.*" --resource-group "myResourceGroupName" --vm-name "myVMName"
"""

helps['guestconfig guest-configuration-assignment wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the guestconfig guest-configuration-assignment\
 is met.
    examples:
      - name: Pause executing next line of CLI script until the guestconfig guest-configuration-assignment is successfu\
lly created.
        text: |-
               az guestconfig guest-configuration-assignment wait --name "SecureProtocol" --resource-group "myResourceG\
roupName" --vm-name "myVMName" --created
"""

helps['guestconfig guest-configuration-assignment-report'] = """
    type: group
    short-summary: guestconfig guest-configuration-assignment-report
"""

helps['guestconfig guest-configuration-assignment-report list'] = """
    type: command
    short-summary: List all reports for the guest configuration assignment, latest report first.
    examples:
      - name: List all guest configuration assignments for a virtual machine
        text: |-
               az guestconfig guest-configuration-assignment-report list --guest-configuration-assignment-name "AuditSe\
cureProtocol" --resource-group "myResourceGroupName" --vm-name "myVMName"
"""

helps['guestconfig guest-configuration-assignment-report show'] = """
    type: command
    short-summary: Get a report for the guest configuration assignment, by reportId.
    examples:
      - name: Get a guest configuration assignment report by Id for a virtual machine
        text: |-
               az guestconfig guest-configuration-assignment-report show --guest-configuration-assignment-name "AuditSe\
cureProtocol" --report-id "7367cbb8-ae99-47d0-a33b-a283564d2cb1" --resource-group "myResourceGroupName" --vm-name "myvm\
"
"""

helps['guestconfig guest-configuration-hcrp-assignment'] = """
    type: group
    short-summary: guestconfig guest-configuration-hcrp-assignment
"""

helps['guestconfig guest-configuration-hcrp-assignment list'] = """
    type: command
    short-summary: List all guest configuration assignments for an ARC machine.
    examples:
      - name: List all guest configuration assignments for a virtual machine
        text: |-
               az guestconfig guest-configuration-hcrp-assignment list --machine-name "myMachineName" --resource-group \
"myResourceGroupName"
"""

helps['guestconfig guest-configuration-hcrp-assignment show'] = """
    type: command
    short-summary: Get information about a guest configuration assignment
    examples:
      - name: Get a guest configuration assignment
        text: |-
               az guestconfig guest-configuration-hcrp-assignment show --guest-configuration-assignment-name "SecurePro\
tocol" --machine-name "myMachineName" --resource-group "myResourceGroupName"
"""

helps['guestconfig guest-configuration-hcrp-assignment create'] = """
    type: command
    short-summary: Creates an association between a ARC machine and guest configuration
    parameters:
      - name: --guest-configuration-configuration-parameter
        short-summary: The configuration parameters for the guest configuration.
        long-summary: |
            Usage: --guest-configuration-configuration-parameter name=XX value=XX

            name: Name of the configuration parameter.
            value: Value of the configuration parameter.

            Multiple actions can be specified by using more than one --guest-configuration-configuration-parameter argu\
ment.
      - name: --guest-configuration-configuration-setting
        short-summary: The configuration setting for the guest configuration.
        long-summary: |
            Usage: --guest-configuration-configuration-setting configuration-mode=XX allow-module-overwrite=XX action-a\
fter-reboot=XX refresh-frequency-mins=XX reboot-if-needed=XX configuration-mode-frequency-mins=XX

            configuration-mode: Specifies how the LCM(Local Configuration Manager) actually applies the configuration t\
o the target nodes. Possible values are ApplyOnly, ApplyAndMonitor, and ApplyAndAutoCorrect.
            allow-module-overwrite: If true - new configurations downloaded from the pull service are allowed to overwr\
ite the old ones on the target node. Otherwise, false
            action-after-reboot: Specifies what happens after a reboot during the application of a configuration. The p\
ossible values are ContinueConfiguration and StopConfiguration
            refresh-frequency-mins: The time interval, in minutes, at which the LCM checks a pull service to get update\
d configurations. This value is ignored if the LCM is not configured in pull mode. The default value is 30.
            reboot-if-needed: Set this to true to automatically reboot the node after a configuration that requires reb\
oot is applied. Otherwise, you will have to manually reboot the node for any configuration that requires it. The defaul\
t value is false. To use this setting when a reboot condition is enacted by something other than DSC (such as Windows I\
nstaller), combine this setting with the xPendingReboot module.
            configuration-mode-frequency-mins: How often, in minutes, the current configuration is checked and applied.\
 This property is ignored if the ConfigurationMode property is set to ApplyOnly. The default value is 15.
    examples:
      - name: Create or update guest configuration assignment
        text: |-
               az guestconfig guest-configuration-hcrp-assignment create --guest-configuration-assignment-name "Whiteli\
stedApplication" --machine-name "myMachineName" --guest-configuration-name "WhitelistedApplication" --location "westcen\
tralus" --context "Azure policy" --guest-configuration-name "WhitelistedApplication" --guest-configuration-configuratio\
n-parameter name="[InstalledApplication]bwhitelistedapp;Name" value="NotePad,sql" --guest-configuration-configuration-s\
etting action-after-reboot="ContinueConfiguration" configuration-mode="MonitorOnly" configuration-mode-frequency-mins=1\
5 reboot-if-needed="False" --guest-configuration-version "1.*" --resource-group "myResourceGroupName"
"""

helps['guestconfig guest-configuration-hcrp-assignment update'] = """
    type: command
    short-summary: Creates an association between a ARC machine and guest configuration
    parameters:
      - name: --guest-configuration-configuration-parameter
        short-summary: The configuration parameters for the guest configuration.
        long-summary: |
            Usage: --guest-configuration-configuration-parameter name=XX value=XX

            name: Name of the configuration parameter.
            value: Value of the configuration parameter.

            Multiple actions can be specified by using more than one --guest-configuration-configuration-parameter argu\
ment.
      - name: --guest-configuration-configuration-setting
        short-summary: The configuration setting for the guest configuration.
        long-summary: |
            Usage: --guest-configuration-configuration-setting configuration-mode=XX allow-module-overwrite=XX action-a\
fter-reboot=XX refresh-frequency-mins=XX reboot-if-needed=XX configuration-mode-frequency-mins=XX

            configuration-mode: Specifies how the LCM(Local Configuration Manager) actually applies the configuration t\
o the target nodes. Possible values are ApplyOnly, ApplyAndMonitor, and ApplyAndAutoCorrect.
            allow-module-overwrite: If true - new configurations downloaded from the pull service are allowed to overwr\
ite the old ones on the target node. Otherwise, false
            action-after-reboot: Specifies what happens after a reboot during the application of a configuration. The p\
ossible values are ContinueConfiguration and StopConfiguration
            refresh-frequency-mins: The time interval, in minutes, at which the LCM checks a pull service to get update\
d configurations. This value is ignored if the LCM is not configured in pull mode. The default value is 30.
            reboot-if-needed: Set this to true to automatically reboot the node after a configuration that requires reb\
oot is applied. Otherwise, you will have to manually reboot the node for any configuration that requires it. The defaul\
t value is false. To use this setting when a reboot condition is enacted by something other than DSC (such as Windows I\
nstaller), combine this setting with the xPendingReboot module.
            configuration-mode-frequency-mins: How often, in minutes, the current configuration is checked and applied.\
 This property is ignored if the ConfigurationMode property is set to ApplyOnly. The default value is 15.
    examples:
      - name: Create or update guest configuration assignment
        text: |-
               az guestconfig guest-configuration-hcrp-assignment update --guest-configuration-assignment-name "Whiteli\
stedApplication" --machine-name "myMachineName" --guest-configuration-name "WhitelistedApplication" --location "westcen\
tralus" --context "Azure policy" --guest-configuration-name "WhitelistedApplication" --guest-configuration-configuratio\
n-parameter name="[InstalledApplication]bwhitelistedapp;Name" value="NotePad,sql" --guest-configuration-configuration-s\
etting action-after-reboot="ContinueConfiguration" configuration-mode="MonitorOnly" configuration-mode-frequency-mins=1\
5 reboot-if-needed="False" --guest-configuration-version "1.*" --resource-group "myResourceGroupName"
"""

helps['guestconfig guest-configuration-hcrp-assignment wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the guestconfig guest-configuration-hcrp-assig\
nment is met.
    examples:
      - name: Pause executing next line of CLI script until the guestconfig guest-configuration-hcrp-assignment is succ\
essfully created.
        text: |-
               az guestconfig guest-configuration-hcrp-assignment wait --guest-configuration-assignment-name "SecurePro\
tocol" --machine-name "myMachineName" --resource-group "myResourceGroupName" --created
"""

helps['guestconfig guest-configuration-hcrp-assignment-report'] = """
    type: group
    short-summary: guestconfig guest-configuration-hcrp-assignment-report
"""

helps['guestconfig guest-configuration-hcrp-assignment-report list'] = """
    type: command
    short-summary: List all reports for the guest configuration assignment, latest report first.
    examples:
      - name: List all guest configuration assignments for a virtual machine
        text: |-
               az guestconfig guest-configuration-hcrp-assignment-report list --guest-configuration-assignment-name "Au\
ditSecureProtocol" --machine-name "myMachineName" --resource-group "myResourceGroupName"
"""

helps['guestconfig guest-configuration-hcrp-assignment-report show'] = """
    type: command
    short-summary: Get a report for the guest configuration assignment, by reportId.
    examples:
      - name: Get a guest configuration assignment report by Id for a virtual machine
        text: |-
               az guestconfig guest-configuration-hcrp-assignment-report show --guest-configuration-assignment-name "Au\
ditSecureProtocol" --machine-name "myMachineName" --report-id "7367cbb8-ae99-47d0-a33b-a283564d2cb1" --resource-group "\
myResourceGroupName"
"""
