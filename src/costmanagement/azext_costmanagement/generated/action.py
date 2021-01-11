# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=protected-access

import argparse
from collections import defaultdict
from knack.util import CLIError


class AddKpis(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddKpis, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'type':
                d['type'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            elif kl == 'enabled':
                d['enabled'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter kpis. All possible keys are: type, id, '
                               'enabled'.format(k))
        return d


class AddPivots(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddPivots, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'type':
                d['type'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter pivots. All possible keys are: type, name'
                .format(k))
        return d


class AddViewsTimePeriod(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.time_period = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'from':
                d['from_property'] = v[0]
            elif kl == 'to':
                d['to'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter time_period. All possible keys are: from, '
                               'to'.format(k))
        return d


class AddViewsConfiguration(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.configuration = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'columns':
                d['columns'] = v
            else:
                raise CLIError('Unsupported Key {} is provided for parameter configuration. All possible keys are: '
                               'columns'.format(k))
        return d


class AddViewsGrouping(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddViewsGrouping, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'type':
                d['type'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter grouping. All possible keys are: type, '
                               'name'.format(k))
        return d


class AddSorting(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddSorting, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'direction':
                d['direction'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter sorting. All possible keys are: '
                               'direction, name'.format(k))
        return d


class AddDefinition(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.definition = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'type':
                d['type'] = v[0]
            elif kl == 'category':
                d['category'] = v[0]
            elif kl == 'criteria':
                d['criteria'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter definition. All possible keys are: type, '
                               'category, criteria'.format(k))
        return d


class AddForecastTimePeriod(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.time_period = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'from':
                d['from_property'] = v[0]
            elif kl == 'to':
                d['to'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter time_period. All possible keys are: from, '
                               'to'.format(k))
        return d


class AddForecastConfiguration(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.configuration = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'columns':
                d['columns'] = v
            else:
                raise CLIError('Unsupported Key {} is provided for parameter configuration. All possible keys are: '
                               'columns'.format(k))
        return d


class AddQueryGrouping(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddQueryGrouping, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'type':
                d['type'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter grouping. All possible keys are: type, '
                               'name'.format(k))
        return d


class AddRecurrencePeriod(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.recurrence_period = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'from':
                d['from_property'] = v[0]
            elif kl == 'to':
                d['to'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter recurrence_period. All possible keys are: '
                               'from, to'.format(k))
        return d


class AddTimePeriod(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.time_period = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'from':
                d['from_property'] = v[0]
            elif kl == 'to':
                d['to'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter time_period. All possible keys are: from, '
                               'to'.format(k))
        return d


class AddConfiguration(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.configuration = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'columns':
                d['columns'] = v
            else:
                raise CLIError('Unsupported Key {} is provided for parameter configuration. All possible keys are: '
                               'columns'.format(k))
        return d


class AddDestination(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.destination = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'resource-id':
                d['resource_id'] = v[0]
            elif kl == 'container':
                d['container'] = v[0]
            elif kl == 'root-folder-path':
                d['root_folder_path'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter destination. All possible keys are: '
                               'resource-id, container, root-folder-path'.format(k))
        return d
