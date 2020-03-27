# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .preparers import VirtualNetworkPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class LogicManagementClientScenarioTest(ScenarioTest):

    def current_subscription(self):
        subs = self.cmd('az account show').get_output_in_json()
        return subs['id']

    @ResourceGroupPreparer(name_prefix='cli_test_logic_test-resource-group'[:9], key='rg')
    @ResourceGroupPreparer(name_prefix='cli_test_logic_testResourceGroup'[:9], key='rg_2')
    @ResourceGroupPreparer(name_prefix='cli_test_logic_testrg123'[:9], key='rg_3')
    @VirtualNetworkPreparer(name_prefix='cli_test_logic_testVNET'[:9], key='vn', resource_group_key='rg_2')
    def test_logic(self, resource_group):

        self.kwargs.update({
            'subscription_id': self.current_subscription()
        })

        self.kwargs.update({
            'test-integration-account': self.create_random_name(prefix='cli_test_integration_accounts'[:9], length=24),
            'IntegrationAccounts_2': self.create_random_name(prefix='cli_test_integration_accounts'[:9], length=24),
            'IntegrationAccounts_3': self.create_random_name(prefix='cli_test_integration_accounts'[:9], length=24),
            'IntegrationAccounts_4': self.create_random_name(prefix='cli_test_integration_accounts'[:9], length=24),
            'testIntegrationServiceEnvironment': self.create_random_name(prefix='cli_test_integration_service_environments'[:9], length=24),
            'test-workflow': self.create_random_name(prefix='cli_test_workflows'[:9], length=24),
            'Workflows_2': self.create_random_name(prefix='cli_test_workflows'[:9], length=24),
            'Workflows_3': self.create_random_name(prefix='cli_test_workflows'[:9], length=24),
            'Workflows_4': self.create_random_name(prefix='cli_test_workflows'[:9], length=24),
        })

        self.cmd('az logic integration-account create '
                 '--location "westus" '
                 '--sku name=Standard '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic workflow create '
                 '--resource-group "{rg}" '
                 '--location "brazilsouth" '
                 '--properties-definition $schema=https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json# actions=[object Object]=undefined contentVersion=1.0.0.0 outputs=[object Object]=undefined parameters=[object Object]=undefined triggers=[object Object]=undefined '
                 '--properties-integration-account id=/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Logic/integrationAccounts/{test-integration-account} '
                 '--properties-parameters "{{\\"$connections\\":{{\\"value\\":{{\\"test-custom-connector\\":{{\\"connectionId\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Web/connections/test-custom-connector\\",\\"connectionName\\":\\"test-custom-connector\\",\\"id\\":\\"/subscriptions/{subscription_id}/providers/Microsoft.Web/locations/brazilsouth/managedApis/test-custom-connector\\"}}}}}}}}" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic integration-account-map create '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--location "westus" '
                 '--properties-content "<?xml version=\\"1.0\\" encoding=\\"UTF-16\\"?>\\r\\n<xsl:stylesheet xmlns:xsl=\\"http://www.w3.org/1999/XSL/Transform\\" xmlns:msxsl=\\"urn:schemas-microsoft-com:xslt\\" xmlns:var=\\"http://schemas.microsoft.com/BizTalk/2003/var\\" exclude-result-prefixes=\\"msxsl var s0 userCSharp\\" version=\\"1.0\\" xmlns:ns0=\\"http://BizTalk_Server_Project4.StringFunctoidsDestinationSchema\\" xmlns:s0=\\"http://BizTalk_Server_Project4.StringFunctoidsSourceSchema\\" xmlns:userCSharp=\\"http://schemas.microsoft.com/BizTalk/2003/userCSharp\\">\\r\\n  <xsl:import href=\\"http://btsfunctoids.blob.core.windows.net/functoids/functoids.xslt\\" />\\r\\n  <xsl:output omit-xml-declaration=\\"yes\\" method=\\"xml\\" version=\\"1.0\\" />\\r\\n  <xsl:template match=\\"/\\">\\r\\n    <xsl:apply-templates select=\\"/s0:Root\\" />\\r\\n  </xsl:template>\\r\\n  <xsl:template match=\\"/s0:Root\\">\\r\\n    <xsl:variable name=\\"var:v1\\" select=\\"userCSharp:StringFind(string(StringFindSource/text()) , &quot;SearchString&quot;)\\" />\\r\\n    <xsl:variable name=\\"var:v2\\" select=\\"userCSharp:StringLeft(string(StringLeftSource/text()) , &quot;2&quot;)\\" />\\r\\n    <xsl:variable name=\\"var:v3\\" select=\\"userCSharp:StringRight(string(StringRightSource/text()) , &quot;2&quot;)\\" />\\r\\n    <xsl:variable name=\\"var:v4\\" select=\\"userCSharp:StringUpperCase(string(UppercaseSource/text()))\\" />\\r\\n    <xsl:variable name=\\"var:v5\\" select=\\"userCSharp:StringLowerCase(string(LowercaseSource/text()))\\" />\\r\\n    <xsl:variable name=\\"var:v6\\" select=\\"userCSharp:StringSize(string(SizeSource/text()))\\" />\\r\\n    <xsl:variable name=\\"var:v7\\" select=\\"userCSharp:StringSubstring(string(StringExtractSource/text()) , &quot;0&quot; , &quot;2&quot;)\\" />\\r\\n    <xsl:variable name=\\"var:v8\\" select=\\"userCSharp:StringConcat(string(StringConcatSource/text()))\\" />\\r\\n    <xsl:variable name=\\"var:v9\\" select=\\"userCSharp:StringTrimLeft(string(StringLeftTrimSource/text()))\\" />\\r\\n    <xsl:variable name=\\"var:v10\\" select=\\"userCSharp:StringTrimRight(string(StringRightTrimSource/text()))\\" />\\r\\n    <ns0:Root>\\r\\n      <StringFindDestination>\\r\\n        <xsl:value-of select=\\"$var:v1\\" />\\r\\n      </StringFindDestination>\\r\\n      <StringLeftDestination>\\r\\n        <xsl:value-of select=\\"$var:v2\\" />\\r\\n      </StringLeftDestination>\\r\\n      <StringRightDestination>\\r\\n        <xsl:value-of select=\\"$var:v3\\" />\\r\\n      </StringRightDestination>\\r\\n      <UppercaseDestination>\\r\\n        <xsl:value-of select=\\"$var:v4\\" />\\r\\n      </UppercaseDestination>\\r\\n      <LowercaseDestination>\\r\\n        <xsl:value-of select=\\"$var:v5\\" />\\r\\n      </LowercaseDestination>\\r\\n      <SizeDestination>\\r\\n        <xsl:value-of select=\\"$var:v6\\" />\\r\\n      </SizeDestination>\\r\\n      <StringExtractDestination>\\r\\n        <xsl:value-of select=\\"$var:v7\\" />\\r\\n      </StringExtractDestination>\\r\\n      <StringConcatDestination>\\r\\n        <xsl:value-of select=\\"$var:v8\\" />\\r\\n      </StringConcatDestination>\\r\\n      <StringLeftTrimDestination>\\r\\n        <xsl:value-of select=\\"$var:v9\\" />\\r\\n      </StringLeftTrimDestination>\\r\\n      <StringRightTrimDestination>\\r\\n        <xsl:value-of select=\\"$var:v10\\" />\\r\\n      </StringRightTrimDestination>\\r\\n    </ns0:Root>\\r\\n  </xsl:template>\\r\\n</xsl:stylesheet>" '
                 '--properties-content-type "application/xml" '
                 '--properties-map-type "Xslt" '
                 '--map-name "testMap" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-service-environment create '
                 '--location "brazilsouth" '
                 '--properties "{{\\"networkConfiguration\\":{{\\"accessEndpoint\\":{{\\"type\\":\\"Internal\\"}},\\"subnets\\":[{{\\"id\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg_2}/providers/Microsoft.Network/virtualNetworks/{vn}/subnets/default\\"}},{{\\"id\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg_2}/providers/Microsoft.Network/virtualNetworks/{vn}/subnets/default\\"}},{{\\"id\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg_2}/providers/Microsoft.Network/virtualNetworks/{vn}/subnets/default\\"}},{{\\"id\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg_2}/providers/Microsoft.Network/virtualNetworks/{vn}/subnets/default\\"}}]}}}}" '
                 '--sku name=Premium capacity=2 '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-account-schema create '
                 '--location "westus" '
                 '--properties-content "<?xml version=\\"1.0\\" encoding=\\"utf-16\\"?>\\r\\n<xs:schema xmlns:b=\\"http://schemas.microsoft.com/BizTalk/2003\\" xmlns=\\"http://Inbound_EDI.OrderFile\\" targetNamespace=\\"http://Inbound_EDI.OrderFile\\" xmlns:xs=\\"http://www.w3.org/2001/XMLSchema\\">\\r\\n  <xs:annotation>\\r\\n    <xs:appinfo>\\r\\n      <b:schemaInfo default_pad_char=\\" \\" count_positions_by_byte=\\"false\\" parser_optimization=\\"speed\\" lookahead_depth=\\"3\\" suppress_empty_nodes=\\"false\\" generate_empty_nodes=\\"true\\" allow_early_termination=\\"false\\" early_terminate_optional_fields=\\"false\\" allow_message_breakup_of_infix_root=\\"false\\" compile_parse_tables=\\"false\\" standard=\\"Flat File\\" root_reference=\\"OrderFile\\" />\\r\\n      <schemaEditorExtension:schemaInfo namespaceAlias=\\"b\\" extensionClass=\\"Microsoft.BizTalk.FlatFileExtension.FlatFileExtension\\" standardName=\\"Flat File\\" xmlns:schemaEditorExtension=\\"http://schemas.microsoft.com/BizTalk/2003/SchemaEditorExtensions\\" />\\r\\n    </xs:appinfo>\\r\\n  </xs:annotation>\\r\\n  <xs:element name=\\"OrderFile\\">\\r\\n    <xs:annotation>\\r\\n      <xs:appinfo>\\r\\n        <b:recordInfo structure=\\"delimited\\" preserve_delimiter_for_empty_data=\\"true\\" suppress_trailing_delimiters=\\"false\\" sequence_number=\\"1\\" />\\r\\n      </xs:appinfo>\\r\\n    </xs:annotation>\\r\\n    <xs:complexType>\\r\\n      <xs:sequence>\\r\\n        <xs:annotation>\\r\\n          <xs:appinfo>\\r\\n            <b:groupInfo sequence_number=\\"0\\" />\\r\\n          </xs:appinfo>\\r\\n        </xs:annotation>\\r\\n        <xs:element name=\\"Order\\">\\r\\n          <xs:annotation>\\r\\n            <xs:appinfo>\\r\\n              <b:recordInfo sequence_number=\\"1\\" structure=\\"delimited\\" preserve_delimiter_for_empty_data=\\"true\\" suppress_trailing_delimiters=\\"false\\" child_delimiter_type=\\"hex\\" child_delimiter=\\"0x0D 0x0A\\" child_order=\\"infix\\" />\\r\\n            </xs:appinfo>\\r\\n          </xs:annotation>\\r\\n          <xs:complexType>\\r\\n            <xs:sequence>\\r\\n              <xs:annotation>\\r\\n                <xs:appinfo>\\r\\n                  <b:groupInfo sequence_number=\\"0\\" />\\r\\n                </xs:appinfo>\\r\\n              </xs:annotation>\\r\\n              <xs:element name=\\"Header\\">\\r\\n                <xs:annotation>\\r\\n                  <xs:appinfo>\\r\\n                    <b:recordInfo sequence_number=\\"1\\" structure=\\"delimited\\" preserve_delimiter_for_empty_data=\\"true\\" suppress_trailing_delimiters=\\"false\\" child_delimiter_type=\\"char\\" child_delimiter=\\"|\\" child_order=\\"infix\\" tag_name=\\"HDR|\\" />\\r\\n                  </xs:appinfo>\\r\\n                </xs:annotation>\\r\\n                <xs:complexType>\\r\\n                  <xs:sequence>\\r\\n                    <xs:annotation>\\r\\n                      <xs:appinfo>\\r\\n                        <b:groupInfo sequence_number=\\"0\\" />\\r\\n                      </xs:appinfo>\\r\\n                    </xs:annotation>\\r\\n                    <xs:element name=\\"PODate\\" type=\\"xs:string\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n                          <b:fieldInfo sequence_number=\\"1\\" justification=\\"left\\" />\\r\\n                        </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n                    </xs:element>\\r\\n                    <xs:element name=\\"PONumber\\" type=\\"xs:string\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n                          <b:fieldInfo justification=\\"left\\" sequence_number=\\"2\\" />\\r\\n                        </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n                    </xs:element>\\r\\n                    <xs:element name=\\"CustomerID\\" type=\\"xs:string\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n                          <b:fieldInfo sequence_number=\\"3\\" justification=\\"left\\" />\\r\\n                        </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n                    </xs:element>\\r\\n                    <xs:element name=\\"CustomerContactName\\" type=\\"xs:string\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n                          <b:fieldInfo sequence_number=\\"4\\" justification=\\"left\\" />\\r\\n                        </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n                    </xs:element>\\r\\n                    <xs:element name=\\"CustomerContactPhone\\" type=\\"xs:string\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n                          <b:fieldInfo sequence_number=\\"5\\" justification=\\"left\\" />\\r\\n                        </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n                    </xs:element>\\r\\n                  </xs:sequence>\\r\\n                </xs:complexType>\\r\\n              </xs:element>\\r\\n              <xs:element minOccurs=\\"1\\" maxOccurs=\\"unbounded\\" name=\\"LineItems\\">\\r\\n                <xs:annotation>\\r\\n                  <xs:appinfo>\\r\\n                    <b:recordInfo sequence_number=\\"2\\" structure=\\"delimited\\" preserve_delimiter_for_empty_data=\\"true\\" suppress_trailing_delimiters=\\"false\\" child_delimiter_type=\\"char\\" child_delimiter=\\"|\\" child_order=\\"infix\\" tag_name=\\"DTL|\\" />\\r\\n                  </xs:appinfo>\\r\\n                </xs:annotation>\\r\\n                <xs:complexType>\\r\\n                  <xs:sequence>\\r\\n                    <xs:annotation>\\r\\n                      <xs:appinfo>\\r\\n                        <b:groupInfo sequence_number=\\"0\\" />\\r\\n                      </xs:appinfo>\\r\\n                    </xs:annotation>\\r\\n                    <xs:element name=\\"PONumber\\" type=\\"xs:string\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n                          <b:fieldInfo sequence_number=\\"1\\" justification=\\"left\\" />\\r\\n                        </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n                    </xs:element>\\r\\n                    <xs:element name=\\"ItemOrdered\\" type=\\"xs:string\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n                          <b:fieldInfo sequence_number=\\"2\\" justification=\\"left\\" />\\r\\n                        </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n                    </xs:element>\\r\\n                    <xs:element name=\\"Quantity\\" type=\\"xs:string\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n                          <b:fieldInfo sequence_number=\\"3\\" justification=\\"left\\" />\\r\\n                        </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n                    </xs:element>\\r\\n                    <xs:element name=\\"UOM\\" type=\\"xs:string\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n                          <b:fieldInfo sequence_number=\\"4\\" justification=\\"left\\" />\\r\\n                        </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n                    </xs:element>\\r\\n                    <xs:element name=\\"Price\\" type=\\"xs:string\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n                          <b:fieldInfo sequence_number=\\"5\\" justification=\\"left\\" />\\r\\n                        </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n                    </xs:element>\\r\\n                    <xs:element name=\\"ExtendedPrice\\" type=\\"xs:string\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n                          <b:fieldInfo sequence_number=\\"6\\" justification=\\"left\\" />\\r\\n                        </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n                    </xs:element>\\r\\n                    <xs:element name=\\"Description\\" type=\\"xs:string\\">\\r\\n                      <xs:annotation>\\r\\n                        <xs:appinfo>\\r\\n                          <b:fieldInfo sequence_number=\\"7\\" justification=\\"left\\" />\\r\\n                        </xs:appinfo>\\r\\n                      </xs:annotation>\\r\\n                    </xs:element>\\r\\n                  </xs:sequence>\\r\\n                </xs:complexType>\\r\\n              </xs:element>\\r\\n            </xs:sequence>\\r\\n          </xs:complexType>\\r\\n        </xs:element>\\r\\n      </xs:sequence>\\r\\n    </xs:complexType>\\r\\n  </xs:element>\\r\\n</xs:schema>" '
                 '--properties-content-type "application/xml" '
                 '--properties-schema-type "Xml" '
                 '--tags integrationAccountSchemaName=IntegrationAccountSchema8120 '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}" '
                 '--schema-name "testSchema"',
                 checks=[])

        self.cmd('az logic integration-account-session create '
                 '--integration-account-name "{IntegrationAccounts_3}" '
                 '--resource-group "{rg_3}" '
                 '--properties-content controlNumber=1234 controlNumberChangedTime=2017-02-21T22:30:11.9923759Z '
                 '--session-name "testsession123-ICN"',
                 checks=[])

        self.cmd('az logic integration-account-partner create '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--location "westus" '
                 '--properties-content "{{\\"b2b\\":{{\\"businessIdentities\\":[{{\\"qualifier\\":\\"AA\\",\\"value\\":\\"ZZ\\"}}]}}}}" '
                 '--properties-partner-type "B2B" '
                 '--partner-name "testPartner" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-agreement create '
                 '--location "westus" '
                 '--properties-agreement-type "AS2" '
                 '--properties-content "{{\\"aS2\\":{{\\"receiveAgreement\\":{{\\"protocolSettings\\":{{\\"acknowledgementConnectionSettings\\":{{\\"ignoreCertificateNameMismatch\\":true,\\"keepHttpConnectionAlive\\":true,\\"supportHttpStatusCodeContinue\\":true,\\"unfoldHttpHeaders\\":true}},\\"envelopeSettings\\":{{\\"autogenerateFileName\\":true,\\"fileNameTemplate\\":\\"Test\\",\\"messageContentType\\":\\"text/plain\\",\\"suspendMessageOnFileNameGenerationError\\":true,\\"transmitFileNameInMimeHeader\\":true}},\\"errorSettings\\":{{\\"resendIfMDNNotReceived\\":true,\\"suspendDuplicateMessage\\":true}},\\"mdnSettings\\":{{\\"dispositionNotificationTo\\":\\"http://tempuri.org\\",\\"mdnText\\":\\"Sample\\",\\"micHashingAlgorithm\\":\\"SHA1\\",\\"needMDN\\":true,\\"receiptDeliveryUrl\\":\\"http://tempuri.org\\",\\"sendInboundMdnToMessageBox\\":true,\\"sendMDNAsynchronously\\":true,\\"signMDN\\":true,\\"signOutboundMdnIfOptional\\":true}},\\"messageConnectionSettings\\":{{\\"ignoreCertificateNameMismatch\\":true,\\"keepHttpConnectionAlive\\":true,\\"supportHttpStatusCodeContinue\\":true,\\"unfoldHttpHeaders\\":true}},\\"securitySettings\\":{{\\"enableNRRForInboundDecodedMessages\\":true,\\"enableNRRForInboundEncodedMessages\\":true,\\"enableNRRForInboundMDN\\":true,\\"enableNRRForOutboundDecodedMessages\\":true,\\"enableNRRForOutboundEncodedMessages\\":true,\\"enableNRRForOutboundMDN\\":true,\\"overrideGroupSigningCertificate\\":false}},\\"validationSettings\\":{{\\"checkCertificateRevocationListOnReceive\\":true,\\"checkCertificateRevocationListOnSend\\":true,\\"checkDuplicateMessage\\":true,\\"compressMessage\\":true,\\"encryptMessage\\":false,\\"encryptionAlgorithm\\":\\"AES128\\",\\"interchangeDuplicatesValidityDays\\":100,\\"overrideMessageProperties\\":true,\\"signMessage\\":false}}}},\\"receiverBusinessIdentity\\":{{\\"qualifier\\":\\"ZZ\\",\\"value\\":\\"ZZ\\"}},\\"senderBusinessIdentity\\":{{\\"qualifier\\":\\"AA\\",\\"value\\":\\"AA\\"}}}},\\"sendAgreement\\":{{\\"protocolSettings\\":{{\\"acknowledgementConnectionSettings\\":{{\\"ignoreCertificateNameMismatch\\":true,\\"keepHttpConnectionAlive\\":true,\\"supportHttpStatusCodeContinue\\":true,\\"unfoldHttpHeaders\\":true}},\\"envelopeSettings\\":{{\\"autogenerateFileName\\":true,\\"fileNameTemplate\\":\\"Test\\",\\"messageContentType\\":\\"text/plain\\",\\"suspendMessageOnFileNameGenerationError\\":true,\\"transmitFileNameInMimeHeader\\":true}},\\"errorSettings\\":{{\\"resendIfMDNNotReceived\\":true,\\"suspendDuplicateMessage\\":true}},\\"mdnSettings\\":{{\\"dispositionNotificationTo\\":\\"http://tempuri.org\\",\\"mdnText\\":\\"Sample\\",\\"micHashingAlgorithm\\":\\"SHA1\\",\\"needMDN\\":true,\\"receiptDeliveryUrl\\":\\"http://tempuri.org\\",\\"sendInboundMdnToMessageBox\\":true,\\"sendMDNAsynchronously\\":true,\\"signMDN\\":true,\\"signOutboundMdnIfOptional\\":true}},\\"messageConnectionSettings\\":{{\\"ignoreCertificateNameMismatch\\":true,\\"keepHttpConnectionAlive\\":true,\\"supportHttpStatusCodeContinue\\":true,\\"unfoldHttpHeaders\\":true}},\\"securitySettings\\":{{\\"enableNRRForInboundDecodedMessages\\":true,\\"enableNRRForInboundEncodedMessages\\":true,\\"enableNRRForInboundMDN\\":true,\\"enableNRRForOutboundDecodedMessages\\":true,\\"enableNRRForOutboundEncodedMessages\\":true,\\"enableNRRForOutboundMDN\\":true,\\"overrideGroupSigningCertificate\\":false}},\\"validationSettings\\":{{\\"checkCertificateRevocationListOnReceive\\":true,\\"checkCertificateRevocationListOnSend\\":true,\\"checkDuplicateMessage\\":true,\\"compressMessage\\":true,\\"encryptMessage\\":false,\\"encryptionAlgorithm\\":\\"AES128\\",\\"interchangeDuplicatesValidityDays\\":100,\\"overrideMessageProperties\\":true,\\"signMessage\\":false}}}},\\"receiverBusinessIdentity\\":{{\\"qualifier\\":\\"AA\\",\\"value\\":\\"AA\\"}},\\"senderBusinessIdentity\\":{{\\"qualifier\\":\\"ZZ\\",\\"value\\":\\"ZZ\\"}}}}}}}}" '
                 '--properties-guest-identity qualifier=AA value=AA '
                 '--properties-guest-partner "GuestPartner" '
                 '--properties-host-identity qualifier=ZZ value=ZZ '
                 '--properties-host-partner "HostPartner" '
                 '--tags IntegrationAccountAgreement=<IntegrationAccountAgreementName> '
                 '--agreement-name "testAgreement" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-certificate create '
                 '--location "brazilsouth" '
                 '--properties-key "{{\\"keyName\\":\\"<keyName>\\",\\"keyVault\\":{{\\"id\\":\\"/subscriptions/{subscription_id}/resourcegroups/{rg_2}/providers/microsoft.keyvault/vaults/<keyVaultName>\\"}},\\"keyVersion\\":\\"87d9764197604449b9b8eb7bd8710868\\"}}" '
                 '--properties-public-certificate "<publicCertificateValue>" '
                 '--certificate-name "testCertificate" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-assembly create '
                 '--location "westus" '
                 '--properties assembly-name=System.IdentityModel.Tokens.Jwt content=Base64 encoded=undefined Assembly=undefined Content=undefined metadata=[object Object]=undefined '
                 '--assembly-artifact-name "testAssembly" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-batch-configuration create '
                 '--location "westus" '
                 '--properties "{{\\"batchGroupName\\":\\"DEFAULT\\",\\"releaseCriteria\\":{{\\"batchSize\\":234567,\\"messageCount\\":10,\\"recurrence\\":{{\\"frequency\\":\\"Minute\\",\\"interval\\":1,\\"startTime\\":\\"2017-03-24T11:43:00\\",\\"timeZone\\":\\"India Standard Time\\"}}}}}}" '
                 '--batch-configuration-name "testBatchConfiguration" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic workflow-run-action-repetition-request-history show '
                 '--action-name "HTTP_Webhook" '
                 '--repetition-name "000001" '
                 '--request-history-name "08586611142732800686" '
                 '--resource-group "{rg}" '
                 '--run-name "08586776228332053161046300351" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow-run-action-request-history show '
                 '--action-name "HTTP_Webhook" '
                 '--request-history-name "08586611142732800686" '
                 '--resource-group "{rg}" '
                 '--run-name "08586776228332053161046300351" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow-run-action-scope-repetition show '
                 '--action-name "for_each" '
                 '--repetition-name "000000" '
                 '--resource-group "{rg_2}" '
                 '--run-name "08586776228332053161046300351" '
                 '--workflow-name "{Workflows_2}"',
                 checks=[])

        self.cmd('az logic workflow-run-action-repetition show '
                 '--action-name "testAction" '
                 '--repetition-name "000001" '
                 '--resource-group "{rg_2}" '
                 '--run-name "08586776228332053161046300351" '
                 '--workflow-name "{Workflows_2}"',
                 checks=[])

        self.cmd('az logic integration-account-batch-configuration show '
                 '--batch-configuration-name "testBatchConfiguration" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api list '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api show '
                 '--api-name "servicebus" '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api put '
                 '--api-name "servicebus" '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api-operation list '
                 '--api-name "servicebus" '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-account-assembly show '
                 '--assembly-artifact-name "testAssembly" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-service-environment-network-health show '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-account-certificate show '
                 '--certificate-name "testCertificate" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic workflow-trigger-history show '
                 '--history-name "08586676746934337772206998657CU22" '
                 '--resource-group "{rg_2}" '
                 '--trigger-name "testTriggerName" '
                 '--workflow-name "{Workflows_3}"',
                 checks=[])

        self.cmd('az logic integration-account-agreement show '
                 '--agreement-name "testAgreement" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-partner show '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--partner-name "testPartner" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-session show '
                 '--integration-account-name "{IntegrationAccounts_3}" '
                 '--resource-group "{rg_3}" '
                 '--session-name "testsession123-ICN"',
                 checks=[])

        self.cmd('az logic integration-account-schema show '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}" '
                 '--schema-name "testSchema"',
                 checks=[])

        self.cmd('az logic workflow-run-operation show '
                 '--operation-id "ebdcbbde-c4db-43ec-987c-fd0f7726f43b" '
                 '--resource-group "{rg_2}" '
                 '--run-name "08586774142730039209110422528" '
                 '--workflow-name "{Workflows_2}"',
                 checks=[])

        self.cmd('az logic integration-service-environment show '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic workflow-run-action show '
                 '--action-name "HTTP" '
                 '--resource-group "{rg}" '
                 '--run-name "08586676746934337772206998657CU22" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic integration-account-map show '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--map-name "testMap" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic workflow-trigger show '
                 '--resource-group "{rg}" '
                 '--trigger-name "manual" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow-version show '
                 '--resource-group "{rg}" '
                 '--version-id "08586676824806722526" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic integration-account show '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic workflow-run show '
                 '--resource-group "{rg}" '
                 '--run-name "08586676746934337772206998657CU22" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow show '
                 '--resource-group "{rg}" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow-run-action-repetition-request-history list '
                 '--action-name "HTTP_Webhook" '
                 '--repetition-name "000001" '
                 '--resource-group "{rg}" '
                 '--run-name "08586776228332053161046300351" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api list '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api show '
                 '--api-name "servicebus" '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api put '
                 '--api-name "servicebus" '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api-operation list '
                 '--api-name "servicebus" '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic workflow-run-action-request-history list '
                 '--action-name "HTTP_Webhook" '
                 '--resource-group "{rg}" '
                 '--run-name "08586776228332053161046300351" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow-run-action-scope-repetition list '
                 '--action-name "for_each" '
                 '--resource-group "{rg_2}" '
                 '--run-name "08586776228332053161046300351" '
                 '--workflow-name "{Workflows_2}"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api list '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api show '
                 '--api-name "servicebus" '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api put '
                 '--api-name "servicebus" '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api-operation list '
                 '--api-name "servicebus" '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic workflow-run-action-repetition list '
                 '--action-name "testAction" '
                 '--resource-group "{rg_2}" '
                 '--run-name "08586776228332053161046300351" '
                 '--workflow-name "{Workflows_2}"',
                 checks=[])

        self.cmd('az logic integration-service-environment-sku list '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-account-batch-configuration list '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic workflow-trigger-history list '
                 '--resource-group "{rg_2}" '
                 '--trigger-name "testTriggerName" '
                 '--workflow-name "{Workflows_3}"',
                 checks=[])

        self.cmd('az logic integration-account-certificate list '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-assembly list '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-agreement list '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-partner list '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-session list '
                 '--integration-account-name "{IntegrationAccounts_3}" '
                 '--resource-group "{rg_3}"',
                 checks=[])

        self.cmd('az logic integration-account-schema list '
                 '--integration-account-name "{IntegrationAccounts_4}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-map list '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic workflow-run-action list '
                 '--resource-group "{rg}" '
                 '--run-name "08586676746934337772206998657CU22" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow-version list '
                 '--resource-group "{rg}" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow-trigger list '
                 '--resource-group "{rg}" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow-run list '
                 '--resource-group "{rg}" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic integration-service-environment list '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-account list '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic workflow list '
                 '--resource-group "{rg}"',
                 checks=[])

        self.cmd('az logic integration-service-environment list',
                 checks=[])

        self.cmd('az logic integration-account list',
                 checks=[])

        self.cmd('az logic workflow list',
                 checks=[])

        self.cmd('az logic workflow-run-action-repetition list-expression-trace '
                 '--action-name "testAction" '
                 '--repetition-name "000001" '
                 '--resource-group "{rg_2}" '
                 '--run-name "08586776228332053161046300351" '
                 '--workflow-name "{Workflows_2}"',
                 checks=[])

        self.cmd('az logic integration-account-assembly list-content-callback-url '
                 '--assembly-artifact-name "testAssembly" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-schema list-content-callback-url '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--resource-group "{rg_2}" '
                 '--schema-name "testSchema"',
                 checks=[])

        self.cmd('az logic integration-account-map list-content-callback-url '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--map-name "testMap" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-partner list-content-callback-url '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--partner-name "testPartner" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-agreement list-content-callback-url '
                 '--agreement-name "testAgreement" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-schema list-content-callback-url '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--resource-group "{rg_2}" '
                 '--schema-name "testSchema"',
                 checks=[])

        self.cmd('az logic integration-account-map list-content-callback-url '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--map-name "testMap" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-partner list-content-callback-url '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--partner-name "testPartner" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-agreement list-content-callback-url '
                 '--agreement-name "testAgreement" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-schema list-content-callback-url '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--resource-group "{rg_2}" '
                 '--schema-name "testSchema"',
                 checks=[])

        self.cmd('az logic integration-account-map list-content-callback-url '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--map-name "testMap" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-partner list-content-callback-url '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--partner-name "testPartner" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-agreement list-content-callback-url '
                 '--agreement-name "testAgreement" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic workflow-version-trigger list-callback-url '
                 '--key-type "Primary" '
                 '--not-after "2017-03-05T08:00:00Z" '
                 '--resource-group "{rg_2}" '
                 '--trigger-name "testTriggerName" '
                 '--version-id "testWorkflowVersionId" '
                 '--workflow-name "{Workflows_3}"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api list '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api show '
                 '--api-name "servicebus" '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api put '
                 '--api-name "servicebus" '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api-operation list '
                 '--api-name "servicebus" '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-account-schema list-content-callback-url '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--resource-group "{rg_2}" '
                 '--schema-name "testSchema"',
                 checks=[])

        self.cmd('az logic integration-account-map list-content-callback-url '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--map-name "testMap" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-partner list-content-callback-url '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--partner-name "testPartner" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-agreement list-content-callback-url '
                 '--agreement-name "testAgreement" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic workflow-run-action list-expression-trace '
                 '--action-name "testAction" '
                 '--resource-group "{rg_2}" '
                 '--run-name "08586776228332053161046300351" '
                 '--workflow-name "{Workflows_2}"',
                 checks=[])

        self.cmd('az logic workflow-trigger-history resubmit '
                 '--history-name "testHistoryName" '
                 '--resource-group "{rg_2}" '
                 '--trigger-name "testTriggerName" '
                 '--workflow-name "{Workflows_3}"',
                 checks=[])

        self.cmd('az logic integration-service-environment restart '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-account regenerate-access-key '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic workflow-trigger list-callback-url '
                 '--resource-group "{rg}" '
                 '--trigger-name "manual" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic integration-account log-tracking-event '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--events "[{{\\"error\\":{{\\"code\\":\\"NotFound\\",\\"message\\":\\"Some error occurred\\"}},\\"eventLevel\\":\\"Informational\\",\\"eventTime\\":\\"2016-08-05T01:54:49.505567Z\\",\\"record\\":{{\\"agreementProperties\\":{{\\"agreementName\\":\\"testAgreement\\",\\"as2From\\":\\"testas2from\\",\\"as2To\\":\\"testas2to\\",\\"receiverPartnerName\\":\\"testPartner2\\",\\"senderPartnerName\\":\\"testPartner1\\"}},\\"messageProperties\\":{{\\"IsMessageEncrypted\\":false,\\"IsMessageSigned\\":false,\\"correlationMessageId\\":\\"Unique message identifier\\",\\"direction\\":\\"Receive\\",\\"dispositionType\\":\\"received-success\\",\\"fileName\\":\\"test\\",\\"isMdnExpected\\":true,\\"isMessageCompressed\\":false,\\"isMessageFailed\\":false,\\"isNrrEnabled\\":true,\\"mdnType\\":\\"Async\\",\\"messageId\\":\\"12345\\"}}}},\\"recordType\\":\\"AS2Message\\"}}]" '
                 '--source-type "Microsoft.Logic/workflows" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-service-environment update '
                 '--sku name=Developer capacity=0 '
                 '--tags tag1=value1 '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-account list-key-vault-key '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-vault id=subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/testResourceGroup/providers/Microsoft.KeyVault/vaults/testKeyVault '
                 '--skip-token "testSkipToken" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic workflow-trigger reset '
                 '--resource-group "{rg_2}" '
                 '--trigger-name "testTrigger" '
                 '--workflow-name "{Workflows_4}"',
                 checks=[])

        self.cmd('az logic integration-account list-callback-url '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--key-type "Primary" '
                 '--not-after "2017-03-05T08:00:00Z" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic workflow-trigger reset '
                 '--resource-group "{rg_2}" '
                 '--source "{{\\"id\\":\\"subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/sourceResGroup/providers/Microsoft.Logic/workflows/sourceWorkflow/triggers/sourceTrigger\\"}}" '
                 '--trigger-name "testTrigger" '
                 '--workflow-name "{Workflows_4}"',
                 checks=[])

        self.cmd('az logic workflow validate-by-resource-group '
                 '--resource-group "{rg}" '
                 '--location "brazilsouth" '
                 '--properties-definition $schema=https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json# actions=[object Object]=undefined contentVersion=1.0.0.0 outputs=[object Object]=undefined parameters=[object Object]=undefined triggers=[object Object]=undefined '
                 '--properties-integration-account id=/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Logic/integrationAccounts/{test-integration-account} '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow validate-by-location '
                 '--location "brazilsouth" '
                 '--resource-group "{rg}" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow-trigger reset '
                 '--resource-group "{rg_2}" '
                 '--trigger-name "testTrigger" '
                 '--workflow-name "{Workflows_4}"',
                 checks=[])

        self.cmd('az logic workflow generate-upgraded-definition '
                 '--target-schema-version "2016-06-01" '
                 '--resource-group "{rg}" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow-trigger run '
                 '--resource-group "{rg}" '
                 '--trigger-name "manual" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow-run cancel '
                 '--resource-group "{rg}" '
                 '--run-name "08586676746934337772206998657CU22" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow regenerate-access-key '
                 '--resource-group "{rg_2}" '
                 '--workflow-name "{Workflows_3}"',
                 checks=[])

        self.cmd('az logic integration-account update '
                 '--location "westus" '
                 '--sku name=Standard '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic workflow list-callback-url '
                 '--key-type "Primary" '
                 '--not-after "2018-04-19T16:00:00Z" '
                 '--resource-group "{rg_2}" '
                 '--workflow-name "{Workflows_4}"',
                 checks=[])

        self.cmd('az logic workflow list-swagger '
                 '--resource-group "{rg_2}" '
                 '--workflow-name "{Workflows_3}"',
                 checks=[])

        self.cmd('az logic workflow validate-by-resource-group '
                 '--resource-group "{rg}" '
                 '--location "brazilsouth" '
                 '--properties-definition $schema=https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json# actions=[object Object]=undefined contentVersion=1.0.0.0 outputs=[object Object]=undefined parameters=[object Object]=undefined triggers=[object Object]=undefined '
                 '--properties-integration-account id=/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Logic/integrationAccounts/{test-integration-account} '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow validate-by-location '
                 '--location "brazilsouth" '
                 '--resource-group "{rg}" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow disable '
                 '--resource-group "{rg}" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow enable '
                 '--resource-group "{rg}" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic workflow move '
                 '--resource-group "{rg_2}" '
                 '--workflow-name "{Workflows_4}"',
                 checks=[])

        self.cmd('az logic workflow update '
                 '--resource-group "{rg}" '
                 '--location "brazilsouth" '
                 '--properties-definition $schema=https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json# actions=[object Object]=undefined contentVersion=1.0.0.0 outputs=[object Object]=undefined parameters=[object Object]=undefined triggers=[object Object]=undefined '
                 '--properties-integration-account id=/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Logic/integrationAccounts/{test-integration-account} '
                 '--properties-parameters "{{\\"$connections\\":{{\\"value\\":{{\\"test-custom-connector\\":{{\\"connectionId\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Web/connections/test-custom-connector\\",\\"connectionName\\":\\"test-custom-connector\\",\\"id\\":\\"/subscriptions/{subscription_id}/providers/Microsoft.Web/locations/brazilsouth/managedApis/test-custom-connector\\"}}}}}}}}" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic integration-account-batch-configuration delete '
                 '--batch-configuration-name "testBatchConfiguration" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-service-environment-managed-api delete '
                 '--api-name "servicebus" '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-account-assembly delete '
                 '--assembly-artifact-name "testAssembly" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-certificate delete '
                 '--certificate-name "testCertificate" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-agreement delete '
                 '--agreement-name "testAgreement" '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-partner delete '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--partner-name "testPartner" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account-session delete '
                 '--integration-account-name "{IntegrationAccounts_3}" '
                 '--resource-group "{rg_3}" '
                 '--session-name "testsession123-ICN"',
                 checks=[])

        self.cmd('az logic integration-account-schema delete '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}" '
                 '--schema-name "testSchema"',
                 checks=[])

        self.cmd('az logic workflow delete '
                 '--resource-group "{rg}" '
                 '--workflow-name "{test-workflow}"',
                 checks=[])

        self.cmd('az logic integration-account-map delete '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--map-name "testMap" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-account delete '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-service-environment delete '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])

        self.cmd('az logic integration-account delete '
                 '--integration-account-name "{IntegrationAccounts_2}" '
                 '--resource-group "{rg_2}"',
                 checks=[])

        self.cmd('az logic integration-service-environment delete '
                 '--integration-service-environment-name "{testIntegrationServiceEnvironment}" '
                 '--resource-group "testResourceGroup"',
                 checks=[])
