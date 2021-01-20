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


# EXAMPLE: /HostPools/put/HostPool_Create
@try_manual
def step_hostpool_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization hostpool create '
             '--location "centralus" '
             '--description "des1" '
             '--friendly-name "friendly" '
             '--host-pool-type "Pooled" '
             '--load-balancer-type "BreadthFirst" '
             '--max-session-limit 999999 '
             '--personal-desktop-assignment-type "Automatic" '
             '--preferred-app-group-type "Desktop" '
             '--registration-info expiration-time="2021-01-30T01:20:13.806Z" registration-token-operation="Update" '
             '--sso-client-id "client" '
             '--sso-client-secret-key-vault-path "https://keyvault/secret" '
             '--sso-secret-type "SharedKey" '
             '--ssoadfs-authority "https://adfs" '
             '--start-vm-on-connect false '
             '--vm-template "{{json:json}}" '
             '--tags tag1="value1" tag2="value2" '
             '--name "{myHostPool}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /HostPools/get/HostPool_Get
@try_manual
def step_hostpool_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization hostpool show '
             '--name "{myHostPool}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /HostPools/get/HostPool_List
@try_manual
def step_hostpool_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization hostpool list '
             '-g ""',
             checks=checks)


# EXAMPLE: /HostPools/get/HostPool_ListByResourceGroup
@try_manual
def step_hostpool_list2(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization hostpool list '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /HostPools/patch/HostPool_Update
@try_manual
def step_hostpool_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization hostpool update '
             '--description "des1" '
             '--friendly-name "friendly" '
             '--load-balancer-type "BreadthFirst" '
             '--max-session-limit 999999 '
             '--personal-desktop-assignment-type "Automatic" '
             '--registration-info expiration-time="2021-01-30T01:20:13.808Z" registration-token-operation="Update" '
             '--sso-client-id "client" '
             '--sso-client-secret-key-vault-path "https://keyvault/secret" '
             '--sso-secret-type "SharedKey" '
             '--ssoadfs-authority "https://adfs" '
             '--start-vm-on-connect false '
             '--vm-template "{{json:json}}" '
             '--tags tag1="value1" tag2="value2" '
             '--name "{myHostPool}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ApplicationGroups/put/ApplicationGroup_Create
@try_manual
def step_applicationgroup_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization applicationgroup create '
             '--location "centralus" '
             '--description "des1" '
             '--application-group-type "RemoteApp" '
             '--friendly-name "friendly" '
             '--host-pool-arm-path "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.DesktopVir'
             'tualization/hostPools/{myHostPool}" '
             '--tags tag1="value1" tag2="value2" '
             '--name "{myApplicationGroup}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ApplicationGroups/get/ApplicationGroup_Get
@try_manual
def step_applicationgroup_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization applicationgroup show '
             '--name "{myApplicationGroup}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ApplicationGroups/get/ApplicationGroup_List
@try_manual
def step_applicationgroup_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization applicationgroup list '
             '--filter "applicationGroupType eq \'RailApplication\'" '
             '-g ""',
             checks=checks)


# EXAMPLE: /ApplicationGroups/get/ApplicationGroup_ListByResourceGroup
@try_manual
def step_applicationgroup_list2(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization applicationgroup list '
             '--filter "applicationGroupType eq \'RailApplication\'" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ApplicationGroups/patch/ApplicationGroups_Update
@try_manual
def step_applicationgroup_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization applicationgroup update '
             '--description "des1" '
             '--friendly-name "friendly" '
             '--tags tag1="value1" tag2="value2" '
             '--name "{myApplicationGroup}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ApplicationGroups/delete/ApplicationGroup_Delete
@try_manual
def step_applicationgroup_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization applicationgroup delete -y '
             '--name "{myApplicationGroup}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /MsixImages/post/MsixImage_Expand
@try_manual
def step_msix_image_expand(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization msix-image expand '
             '--host-pool-name "{myHostPool2}" '
             '--uri "imagepath" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /MSIXPackages/put/MSIXPackage_Create
@try_manual
def step_msix_package_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization msix-package create '
             '--host-pool-name "{myHostPool2}" '
             '--display-name "displayname" '
             '--image-path "imagepath" '
             '--is-active false '
             '--is-regular-registration false '
             '--last-updated "2021-01-30T01:20:13.810Z" '
             '--package-applications description="application-desc" app-id="ApplicationId" '
             'app-user-model-id="AppUserModelId" friendly-name="friendlyname" icon-image-name="Apptile" '
             'raw-icon="VGhpcyBpcyBhIHN0cmluZyB0byBoYXNo" raw-png="VGhpcyBpcyBhIHN0cmluZyB0byBoYXNo" '
             '--package-dependencies dependency-name="MsixTest_Dependency_Name" min-version="version" '
             'publisher="PublishedName" '
             '--package-family-name "MsixPackage_FamilyName" '
             '--package-name "MsixPackage_name" '
             '--package-relative-path "packagerelativepath" '
             '--version "version" '
             '--msix-package-full-name "msixpackagefullname" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /MSIXPackages/get/MSIXPackage_Get
@try_manual
def step_msix_package_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization msix-package show '
             '--host-pool-name "{myHostPool2}" '
             '--msix-package-full-name "packagefullname" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /MSIXPackages/get/MSIXPackage_List
@try_manual
def step_msix_package_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization msix-package list '
             '--host-pool-name "{myHostPool2}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /MSIXPackages/patch/MSIXPackage_Update
@try_manual
def step_msix_package_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization msix-package update '
             '--host-pool-name "{myHostPool2}" '
             '--display-name "displayname" '
             '--is-active true '
             '--is-regular-registration false '
             '--msix-package-full-name "msixpackagefullname" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /MSIXPackages/delete/MSIXPackage_Delete
@try_manual
def step_msix_package_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization msix-package delete -y '
             '--host-pool-name "{myHostPool2}" '
             '--msix-package-full-name "packagefullname" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ScalingPlans/put/ScalingPlans_Create
@try_manual
def step_scaling_plan_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization scaling-plan create '
             '--resource-group "{rg}" '
             '--location "centralus" '
             '--description "des1" '
             '--exclusion-tag "value" '
             '--friendly-name "friendly" '
             '--host-pool-references host-pool-arm-path="/subscriptions/{subscription_id}/resourceGroups/{rg}/providers'
             '/Microsoft.DesktopVirtualization/hostPools/{myHostPool}" scaling-plan-enabled=true '
             '--host-pool-type "Personal" '
             '--schedules name="schedule1" days-of-week="Monday" days-of-week="Tuesday" days-of-week="Wednesday" '
             'days-of-week="Thursday" days-of-week="Friday" off-peak-load-balancing-algorithm="DepthFirst" '
             'off-peak-start-time="2021-01-30T01:20:13.799Z" peak-load-balancing-algorithm="BreadthFirst" '
             'peak-start-time="2021-01-30T01:20:13.799Z" ramp-down-capacity-threshold-pct=50 '
             'ramp-down-force-logoff-users=true ramp-down-load-balancing-algorithm="DepthFirst" '
             'ramp-down-minimum-hosts-pct=20 ramp-down-notification-message="message" ramp-down-notification-minutes=30'
             ' ramp-down-start-time="2021-01-30T01:20:13.799Z" ramp-up-algorithm="DepthFirst" '
             'ramp-up-capacity-threshold-pct=80 ramp-up-minimum-host-pct=20 ramp-up-start-time="2021-01-30T01:20:13.799'
             'Z" '
             '--time-zone "" '
             '--tags tag1="value1" tag2="value2" '
             '--name "{myScalingPlan}"',
             checks=checks)


# EXAMPLE: /ScalingPlans/get/ScalingPlans_Get
@try_manual
def step_scaling_plan_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization scaling-plan show '
             '--resource-group "{rg}" '
             '--name "{myScalingPlan}"',
             checks=checks)


# EXAMPLE: /ScalingPlans/get/ScalingPlans_ListByResourceGroup
@try_manual
def step_scaling_plan_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization scaling-plan list '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ScalingPlans/get/ScalingPlans_ListBySubscription
@try_manual
def step_scaling_plan_list2(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization scaling-plan list '
             '-g ""',
             checks=checks)


# EXAMPLE: /ScalingPlans/get/UserSession_SendMessage_Post
@try_manual
def step_scaling_plan_list3(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization scaling-plan list '
             '--host-pool-name "{myHostPool}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ScalingPlans/patch/ScalingPlans_Update
@try_manual
def step_scaling_plan_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization scaling-plan update '
             '--resource-group "{rg}" '
             '--name "{myScalingPlan}" '
             '--description "des1" '
             '--exclusion-tag "value" '
             '--friendly-name "friendly" '
             '--host-pool-references host-pool-arm-path="/subscriptions/{subscription_id}/resourceGroups/{rg}/providers'
             '/Microsoft.DesktopVirtualization/hostPools/{myHostPool}" scaling-plan-enabled=true '
             '--host-pool-type "Personal" '
             '--schedules name="schedule1" days-of-week="Monday" days-of-week="Tuesday" days-of-week="Wednesday" '
             'days-of-week="Thursday" days-of-week="Friday" off-peak-load-balancing-algorithm="DepthFirst" '
             'off-peak-start-time="2021-01-30T01:20:13.799Z" peak-load-balancing-algorithm="BreadthFirst" '
             'peak-start-time="2021-01-30T01:20:13.799Z" ramp-down-capacity-threshold-pct=50 '
             'ramp-down-force-logoff-users=true ramp-down-load-balancing-algorithm="DepthFirst" '
             'ramp-down-minimum-hosts-pct=20 ramp-down-notification-message="message" ramp-down-notification-minutes=30'
             ' ramp-down-start-time="2021-01-30T01:20:13.799Z" ramp-up-algorithm="DepthFirst" '
             'ramp-up-capacity-threshold-pct=80 ramp-up-minimum-host-pct=20 ramp-up-start-time="2021-01-30T01:20:13.799'
             'Z" '
             '--time-zone "" '
             '--tags tag1="value1" tag2="value2"',
             checks=checks)


# EXAMPLE: /ScalingPlans/delete/ScalingPlans_Delete
@try_manual
def step_scaling_plan_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization scaling-plan delete -y '
             '--resource-group "{rg}" '
             '--name "{myScalingPlan}"',
             checks=checks)


# EXAMPLE: /HostPools/delete/HostPool_Delete
@try_manual
def step_hostpool_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization hostpool delete -y '
             '--force true '
             '--name "{myHostPool}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Workspaces/put/Workspace_Create
@try_manual
def step_workspace_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization workspace create '
             '--resource-group "{rg}" '
             '--location "centralus" '
             '--description "des1" '
             '--friendly-name "friendly" '
             '--tags tag1="value1" tag2="value2" '
             '--name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Workspaces/get/Workspace_Get
@try_manual
def step_workspace_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization workspace show '
             '--resource-group "{rg}" '
             '--name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Workspaces/get/Workspace_ListByResourceGroup
@try_manual
def step_workspace_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization workspace list '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Workspaces/get/Workspace_ListBySubscription
@try_manual
def step_workspace_list2(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization workspace list '
             '-g ""',
             checks=checks)


# EXAMPLE: /Workspaces/patch/Workspace_Update
@try_manual
def step_workspace_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization workspace update '
             '--resource-group "{rg}" '
             '--description "des1" '
             '--friendly-name "friendly" '
             '--tags tag1="value1" tag2="value2" '
             '--name "{myWorkspace}"',
             checks=checks)


# EXAMPLE: /Workspaces/delete/Workspace_Delete
@try_manual
def step_workspace_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az desktopvirtualization workspace delete -y '
             '--resource-group "{rg}" '
             '--name "{myWorkspace}"',
             checks=checks)

