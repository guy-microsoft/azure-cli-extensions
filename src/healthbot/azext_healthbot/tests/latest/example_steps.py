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


# EXAMPLE: /Bots/put/BotCreate
@try_manual
def step_create(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthbot create '
             '--bot-name "{myBot}" '
             '--location "East US" '
             '--name "F0" '
             '--resource-group "{rg_2}"',
             checks=checks)


# EXAMPLE: /Bots/get/List Bots by Resource Group
@try_manual
def step_list(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthbot list '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Bots/get/List Bots by Subscription
@try_manual
def step_list2(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthbot list '
             '-g ""',
             checks=checks)


# EXAMPLE: /Bots/get/ResourceInfoGet
@try_manual
def step_show(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthbot show '
             '--name "{myBot}" '
             '--resource-group "{rg_2}"',
             checks=checks)


# EXAMPLE: /Bots/patch/BotUpdate
@try_manual
def step_update(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthbot update '
             '--bot-name "{myBot}" '
             '--name "F0" '
             '--resource-group "{rg_2}"',
             checks=checks)


# EXAMPLE: /Bots/delete/BotDelete
@try_manual
def step_delete(test, rg, rg_2, checks=None):
    if checks is None:
        checks = []
    test.cmd('az healthbot delete -y '
             '--name "{myBot}" '
             '--resource-group "{rg_2}"',
             checks=checks)
