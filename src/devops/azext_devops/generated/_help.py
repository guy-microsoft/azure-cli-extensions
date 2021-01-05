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


helps['devops pipeline-template-definition'] = """
    type: group
    short-summary: Manage pipeline template definition with devops
"""

helps['devops pipeline-template-definition list'] = """
    type: command
    short-summary: "Lists all pipeline templates which can be used to configure an Azure Pipeline."
    examples:
      - name: Get the list of pipeline template definitions
        text: |-
               az devops pipeline-template-definition list
"""

helps['devops pipeline'] = """
    type: group
    short-summary: Manage pipeline with devops
"""

helps['devops pipeline list'] = """
    type: command
    short-summary: "Lists all Azure Pipelines under the specified resource group. And Lists all Azure Pipelines under \
the specified subscription."
    examples:
      - name: List all Azure Pipelines under the specified resource group
        text: |-
               az devops pipeline list --resource-group "myAspNetWebAppPipeline-rg"
      - name: List all Azure pipelines under the specified subscription
        text: |-
               az devops pipeline list
"""

helps['devops pipeline show'] = """
    type: command
    short-summary: "Gets an existing Azure Pipeline."
    examples:
      - name: Get an existing Azure pipeline
        text: |-
               az devops pipeline show --name "myAspNetWebAppPipeline" --resource-group "myAspNetWebAppPipeline-rg"
"""

helps['devops pipeline create'] = """
    type: command
    short-summary: "Create an Azure Pipeline."
    examples:
      - name: Create an Azure pipeline to deploy a sample ASP.Net application to Azure web-app
        text: |-
               az devops pipeline create --location "South India" --properties bootstrapConfiguration={"template":{"id"\
:"ms.vss-continuous-delivery-pipeline-templates.aspnet-windowswebapp","parameters":{"appInsightLocation":"South \
India","appServicePlan":"S1 Standard","azureAuth":"{\\"scheme\\":\\"ServicePrincipal\\",\\"parameters\\":{\\"tenantid\\\
":\\"{subscriptionTenantId}\\",\\"objectid\\":\\"{appObjectId}\\",\\"serviceprincipalid\\":\\"{appId}\\",\\"serviceprin\
cipalkey\\":\\"{appSecret}\\"}}","location":"South India","resourceGroup":"myAspNetWebAppPipeline-rg","subscriptionId":\
"{subscriptionId}","webAppName":"myAspNetWebApp"}}} organization={"name":"myAspNetWebAppPipeline-org"} \
project={"name":"myAspNetWebAppPipeline-project"} --pipeline-name "myAspNetWebAppPipeline" --resource-group \
"myAspNetWebAppPipeline-rg"
"""

helps['devops pipeline update'] = """
    type: command
    short-summary: "Updates the properties of an Azure Pipeline. Currently, only tags can be updated."
    examples:
      - name: Get an existing Azure pipeline
        text: |-
               az devops pipeline update --name "myAspNetWebAppPipeline" --resource-group "myAspNetWebAppPipeline-rg" \
--tags tagKey="tagvalue"
"""

helps['devops pipeline delete'] = """
    type: command
    short-summary: "Deletes an Azure Pipeline."
    examples:
      - name: Get an existing Azure pipeline
        text: |-
               az devops pipeline delete --name "myAspNetWebAppPipeline" --resource-group "myAspNetWebAppPipeline-rg"
"""

helps['devops pipeline wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the devops pipeline is met.
    examples:
      - name: Pause executing next line of CLI script until the devops pipeline is successfully created.
        text: |-
               az devops pipeline wait --name "myAspNetWebAppPipeline" --resource-group "myAspNetWebAppPipeline-rg" \
--created
"""
