# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AvroCompressionCodec(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    DEFLATE = "deflate"
    SNAPPY = "snappy"
    XZ = "xz"
    BZIP2 = "bzip2"

class AzureFunctionActivityMethod(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The list of HTTP methods supported by a AzureFunctionActivity.
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"
    TRACE = "TRACE"

class AzureSearchIndexWriteBehaviorType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specify the write behavior when upserting documents into Azure Search Index.
    """

    MERGE = "Merge"
    UPLOAD = "Upload"

class BlobEventTypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    MICROSOFT_STORAGE_BLOB_CREATED = "Microsoft.Storage.BlobCreated"
    MICROSOFT_STORAGE_BLOB_DELETED = "Microsoft.Storage.BlobDeleted"

class CassandraSourceReadConsistencyLevels(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The consistency level specifies how many Cassandra servers must respond to a read request
    before returning data to the client application. Cassandra checks the specified number of
    Cassandra servers for data to satisfy the read request. Must be one of
    cassandraSourceReadConsistencyLevels. The default value is 'ONE'. It is case-insensitive.
    """

    ALL = "ALL"
    EACH_QUORUM = "EACH_QUORUM"
    QUORUM = "QUORUM"
    LOCAL_QUORUM = "LOCAL_QUORUM"
    ONE = "ONE"
    TWO = "TWO"
    THREE = "THREE"
    LOCAL_ONE = "LOCAL_ONE"
    SERIAL = "SERIAL"
    LOCAL_SERIAL = "LOCAL_SERIAL"

class CompressionCodec(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    GZIP = "gzip"
    SNAPPY = "snappy"
    LZO = "lzo"
    BZIP2 = "bzip2"
    DEFLATE = "deflate"
    ZIP_DEFLATE = "zipDeflate"
    LZ4 = "lz4"
    TAR = "tar"
    TAR_G_ZIP = "tarGZip"

class CopyBehaviorType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """All available types of copy behavior.
    """

    PRESERVE_HIERARCHY = "PreserveHierarchy"
    FLATTEN_HIERARCHY = "FlattenHierarchy"
    MERGE_FILES = "MergeFiles"

class DataFlowComputeType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Compute type of the cluster which will execute data flow job.
    """

    GENERAL = "General"
    MEMORY_OPTIMIZED = "MemoryOptimized"
    COMPUTE_OPTIMIZED = "ComputeOptimized"

class DataFlowDebugCommandType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The command type.
    """

    EXECUTE_PREVIEW_QUERY = "executePreviewQuery"
    EXECUTE_STATISTICS_QUERY = "executeStatisticsQuery"
    EXECUTE_EXPRESSION_QUERY = "executeExpressionQuery"

class DatasetCompressionLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """All available compression levels.
    """

    OPTIMAL = "Optimal"
    FASTEST = "Fastest"

class DayOfWeek(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The days of the week.
    """

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"

class DaysOfWeek(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"

class Db2AuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """AuthenticationType to be used for connection. It is mutually exclusive with connectionString
    property.
    """

    BASIC = "Basic"

class DependencyCondition(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    SKIPPED = "Skipped"
    COMPLETED = "Completed"

class DynamicsAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to connect to Dynamics server. 'Office365' for online scenario, 'Ifd'
    for on-premises with Ifd scenario, 'AADServicePrincipal' for Server-To-Server authentication in
    online scenario. Type: string (or Expression with resultType string).
    """

    OFFICE365 = "Office365"
    IFD = "Ifd"
    AAD_SERVICE_PRINCIPAL = "AADServicePrincipal"

class DynamicsDeploymentType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The deployment type of the Dynamics instance. 'Online' for Dynamics Online and
    'OnPremisesWithIfd' for Dynamics on-premises with Ifd. Type: string (or Expression with
    resultType string).
    """

    ONLINE = "Online"
    ON_PREMISES_WITH_IFD = "OnPremisesWithIfd"

class DynamicsServicePrincipalCredentialType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The service principal credential type to use in Server-To-Server authentication.
    'ServicePrincipalKey' for key/secret, 'ServicePrincipalCert' for certificate. Type: string (or
    Expression with resultType string).
    """

    SERVICE_PRINCIPAL_KEY = "ServicePrincipalKey"
    SERVICE_PRINCIPAL_CERT = "ServicePrincipalCert"

class DynamicsSinkWriteBehavior(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Defines values for DynamicsSinkWriteBehavior.
    """

    UPSERT = "Upsert"

class EventSubscriptionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Event Subscription Status.
    """

    ENABLED = "Enabled"
    PROVISIONING = "Provisioning"
    DEPROVISIONING = "Deprovisioning"
    DISABLED = "Disabled"
    UNKNOWN = "Unknown"

class FactoryIdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The identity type.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"

class FtpAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to be used to connect to the FTP server.
    """

    BASIC = "Basic"
    ANONYMOUS = "Anonymous"

class GlobalParameterType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Global Parameter type.
    """

    OBJECT = "Object"
    STRING = "String"
    INT = "Int"
    FLOAT = "Float"
    BOOL = "Bool"
    ARRAY = "Array"

class GoogleAdWordsAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The OAuth 2.0 authentication mechanism used for authentication. ServiceAuthentication can only
    be used on self-hosted IR.
    """

    SERVICE_AUTHENTICATION = "ServiceAuthentication"
    USER_AUTHENTICATION = "UserAuthentication"

class GoogleBigQueryAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The OAuth 2.0 authentication mechanism used for authentication. ServiceAuthentication can only
    be used on self-hosted IR.
    """

    SERVICE_AUTHENTICATION = "ServiceAuthentication"
    USER_AUTHENTICATION = "UserAuthentication"

class HBaseAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication mechanism to use to connect to the HBase server.
    """

    ANONYMOUS = "Anonymous"
    BASIC = "Basic"

class HdiNodeTypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The node types on which the script action should be executed.
    """

    HEADNODE = "Headnode"
    WORKERNODE = "Workernode"
    ZOOKEEPER = "Zookeeper"

class HdInsightActivityDebugInfoOption(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The HDInsightActivityDebugInfoOption settings to use.
    """

    NONE = "None"
    ALWAYS = "Always"
    FAILURE = "Failure"

class HiveAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication method used to access the Hive server.
    """

    ANONYMOUS = "Anonymous"
    USERNAME = "Username"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"
    WINDOWS_AZURE_HD_INSIGHT_SERVICE = "WindowsAzureHDInsightService"

class HiveServerType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of Hive server.
    """

    HIVE_SERVER1 = "HiveServer1"
    HIVE_SERVER2 = "HiveServer2"
    HIVE_THRIFT_SERVER = "HiveThriftServer"

class HiveThriftTransportProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The transport protocol to use in the Thrift layer.
    """

    BINARY = "Binary"
    SASL = "SASL"
    HTTP = "HTTP "

class HttpAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to be used to connect to the HTTP server.
    """

    BASIC = "Basic"
    ANONYMOUS = "Anonymous"
    DIGEST = "Digest"
    WINDOWS = "Windows"
    CLIENT_CERTIFICATE = "ClientCertificate"

class ImpalaAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to use.
    """

    ANONYMOUS = "Anonymous"
    SASL_USERNAME = "SASLUsername"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"

class IntegrationRuntimeAuthKeyName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The name of the authentication key to regenerate.
    """

    AUTH_KEY1 = "authKey1"
    AUTH_KEY2 = "authKey2"

class IntegrationRuntimeAutoUpdate(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The state of integration runtime auto update.
    """

    ON = "On"
    OFF = "Off"

class IntegrationRuntimeEdition(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The edition for the SSIS Integration Runtime
    """

    STANDARD = "Standard"
    ENTERPRISE = "Enterprise"

class IntegrationRuntimeEntityReferenceType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of this referenced entity.
    """

    INTEGRATION_RUNTIME_REFERENCE = "IntegrationRuntimeReference"
    LINKED_SERVICE_REFERENCE = "LinkedServiceReference"

class IntegrationRuntimeInternalChannelEncryptionMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """It is used to set the encryption mode for node-node communication channel (when more than 2
    self-hosted integration runtime nodes exist).
    """

    NOT_SET = "NotSet"
    SSL_ENCRYPTED = "SslEncrypted"
    NOT_ENCRYPTED = "NotEncrypted"

class IntegrationRuntimeLicenseType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """License type for bringing your own license scenario.
    """

    BASE_PRICE = "BasePrice"
    LICENSE_INCLUDED = "LicenseIncluded"

class IntegrationRuntimeSsisCatalogPricingTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The pricing tier for the catalog database. The valid values could be found in
    https://azure.microsoft.com/en-us/pricing/details/sql-database/
    """

    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    PREMIUM_RS = "PremiumRS"

class IntegrationRuntimeState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The state of integration runtime.
    """

    INITIAL = "Initial"
    STOPPED = "Stopped"
    STARTED = "Started"
    STARTING = "Starting"
    STOPPING = "Stopping"
    NEED_REGISTRATION = "NeedRegistration"
    ONLINE = "Online"
    LIMITED = "Limited"
    OFFLINE = "Offline"
    ACCESS_DENIED = "AccessDenied"

class IntegrationRuntimeType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of integration runtime.
    """

    MANAGED = "Managed"
    SELF_HOSTED = "SelfHosted"

class IntegrationRuntimeUpdateResult(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The result of the last integration runtime node update.
    """

    NONE = "None"
    SUCCEED = "Succeed"
    FAIL = "Fail"

class JsonFormatFilePattern(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """JSON format file pattern. A property of JsonFormat.
    """

    SET_OF_OBJECTS = "setOfObjects"
    ARRAY_OF_OBJECTS = "arrayOfObjects"

class JsonWriteFilePattern(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """File pattern of JSON. This setting controls the way a collection of JSON objects will be
    treated. The default value is 'setOfObjects'. It is case-sensitive.
    """

    SET_OF_OBJECTS = "setOfObjects"
    ARRAY_OF_OBJECTS = "arrayOfObjects"

class ManagedIntegrationRuntimeNodeStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The managed integration runtime node status.
    """

    STARTING = "Starting"
    AVAILABLE = "Available"
    RECYCLING = "Recycling"
    UNAVAILABLE = "Unavailable"

class MongoDBAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to be used to connect to the MongoDB database.
    """

    BASIC = "Basic"
    ANONYMOUS = "Anonymous"

class NetezzaPartitionOption(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The partition mechanism that will be used for Netezza read in parallel.
    """

    NONE = "None"
    DATA_SLICE = "DataSlice"
    DYNAMIC_RANGE = "DynamicRange"

class ODataAADServicePrincipalCredentialType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specify the credential type (key or cert) is used for service principal.
    """

    SERVICE_PRINCIPAL_KEY = "ServicePrincipalKey"
    SERVICE_PRINCIPAL_CERT = "ServicePrincipalCert"

class ODataAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of authentication used to connect to the OData service.
    """

    BASIC = "Basic"
    ANONYMOUS = "Anonymous"
    WINDOWS = "Windows"
    AAD_SERVICE_PRINCIPAL = "AadServicePrincipal"
    MANAGED_SERVICE_IDENTITY = "ManagedServiceIdentity"

class OraclePartitionOption(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The partition mechanism that will be used for Oracle read in parallel.
    """

    NONE = "None"
    PHYSICAL_PARTITIONS_OF_TABLE = "PhysicalPartitionsOfTable"
    DYNAMIC_RANGE = "DynamicRange"

class OrcCompressionCodec(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    ZLIB = "zlib"
    SNAPPY = "snappy"
    LZO = "lzo"

class ParameterType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Parameter type.
    """

    OBJECT = "Object"
    STRING = "String"
    INT = "Int"
    FLOAT = "Float"
    BOOL = "Bool"
    ARRAY = "Array"
    SECURE_STRING = "SecureString"

class PhoenixAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication mechanism used to connect to the Phoenix server.
    """

    ANONYMOUS = "Anonymous"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"
    WINDOWS_AZURE_HD_INSIGHT_SERVICE = "WindowsAzureHDInsightService"

class PolybaseSettingsRejectType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates whether the RejectValue property is specified as a literal value or a percentage.
    """

    VALUE = "value"
    PERCENTAGE = "percentage"

class PrestoAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication mechanism used to connect to the Presto server.
    """

    ANONYMOUS = "Anonymous"
    LDAP = "LDAP"

class PublicNetworkAccess(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Whether or not public network access is allowed for the data factory.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class RecurrenceFrequency(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enumerates possible frequency option for the schedule trigger.
    """

    NOT_SPECIFIED = "NotSpecified"
    MINUTE = "Minute"
    HOUR = "Hour"
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"

class RestServiceAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of authentication used to connect to the REST service.
    """

    ANONYMOUS = "Anonymous"
    BASIC = "Basic"
    AAD_SERVICE_PRINCIPAL = "AadServicePrincipal"
    MANAGED_SERVICE_IDENTITY = "ManagedServiceIdentity"

class RunQueryFilterOperand(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Parameter name to be used for filter. The allowed operands to query pipeline runs are
    PipelineName, RunStart, RunEnd and Status; to query activity runs are ActivityName,
    ActivityRunStart, ActivityRunEnd, ActivityType and Status, and to query trigger runs are
    TriggerName, TriggerRunTimestamp and Status.
    """

    PIPELINE_NAME = "PipelineName"
    STATUS = "Status"
    RUN_START = "RunStart"
    RUN_END = "RunEnd"
    ACTIVITY_NAME = "ActivityName"
    ACTIVITY_RUN_START = "ActivityRunStart"
    ACTIVITY_RUN_END = "ActivityRunEnd"
    ACTIVITY_TYPE = "ActivityType"
    TRIGGER_NAME = "TriggerName"
    TRIGGER_RUN_TIMESTAMP = "TriggerRunTimestamp"
    RUN_GROUP_ID = "RunGroupId"
    LATEST_ONLY = "LatestOnly"

class RunQueryFilterOperator(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Operator to be used for filter.
    """

    EQUALS = "Equals"
    NOT_EQUALS = "NotEquals"
    IN_ENUM = "In"
    NOT_IN = "NotIn"

class RunQueryOrder(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Sorting order of the parameter.
    """

    ASC = "ASC"
    DESC = "DESC"

class RunQueryOrderByField(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Parameter name to be used for order by. The allowed parameters to order by for pipeline runs
    are PipelineName, RunStart, RunEnd and Status; for activity runs are ActivityName,
    ActivityRunStart, ActivityRunEnd and Status; for trigger runs are TriggerName,
    TriggerRunTimestamp and Status.
    """

    RUN_START = "RunStart"
    RUN_END = "RunEnd"
    PIPELINE_NAME = "PipelineName"
    STATUS = "Status"
    ACTIVITY_NAME = "ActivityName"
    ACTIVITY_RUN_START = "ActivityRunStart"
    ACTIVITY_RUN_END = "ActivityRunEnd"
    TRIGGER_NAME = "TriggerName"
    TRIGGER_RUN_TIMESTAMP = "TriggerRunTimestamp"

class SalesforceSinkWriteBehavior(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The write behavior for the operation. Default is Insert.
    """

    INSERT = "Insert"
    UPSERT = "Upsert"

class SalesforceSourceReadBehavior(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The read behavior for the operation. Default is Query.
    """

    QUERY = "Query"
    QUERY_ALL = "QueryAll"

class SapCloudForCustomerSinkWriteBehavior(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The write behavior for the operation. Default is 'Insert'.
    """

    INSERT = "Insert"
    UPDATE = "Update"

class SapHanaAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to be used to connect to the SAP HANA server.
    """

    BASIC = "Basic"
    WINDOWS = "Windows"

class SapHanaPartitionOption(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The partition mechanism that will be used for SAP HANA read in parallel.
    """

    NONE = "None"
    PHYSICAL_PARTITIONS_OF_TABLE = "PhysicalPartitionsOfTable"
    SAP_HANA_DYNAMIC_RANGE = "SapHanaDynamicRange"

class SapTablePartitionOption(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The partition mechanism that will be used for SAP table read in parallel.
    """

    NONE = "None"
    PARTITION_ON_INT = "PartitionOnInt"
    PARTITION_ON_CALENDAR_YEAR = "PartitionOnCalendarYear"
    PARTITION_ON_CALENDAR_MONTH = "PartitionOnCalendarMonth"
    PARTITION_ON_CALENDAR_DATE = "PartitionOnCalendarDate"
    PARTITION_ON_TIME = "PartitionOnTime"

class SelfHostedIntegrationRuntimeNodeStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the integration runtime node.
    """

    NEED_REGISTRATION = "NeedRegistration"
    ONLINE = "Online"
    LIMITED = "Limited"
    OFFLINE = "Offline"
    UPGRADING = "Upgrading"
    INITIALIZING = "Initializing"
    INITIALIZE_FAILED = "InitializeFailed"

class ServiceNowAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to use.
    """

    BASIC = "Basic"
    O_AUTH2 = "OAuth2"

class SftpAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type to be used to connect to the FTP server.
    """

    BASIC = "Basic"
    SSH_PUBLIC_KEY = "SshPublicKey"

class SparkAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication method used to access the Spark server.
    """

    ANONYMOUS = "Anonymous"
    USERNAME = "Username"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"
    WINDOWS_AZURE_HD_INSIGHT_SERVICE = "WindowsAzureHDInsightService"

class SparkServerType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of Spark server.
    """

    SHARK_SERVER = "SharkServer"
    SHARK_SERVER2 = "SharkServer2"
    SPARK_THRIFT_SERVER = "SparkThriftServer"

class SparkThriftTransportProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The transport protocol to use in the Thrift layer.
    """

    BINARY = "Binary"
    SASL = "SASL"
    HTTP = "HTTP "

class SQLPartitionOption(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The partition mechanism that will be used for Sql read in parallel.
    """

    NONE = "None"
    PHYSICAL_PARTITIONS_OF_TABLE = "PhysicalPartitionsOfTable"
    DYNAMIC_RANGE = "DynamicRange"

class SsisLogLocationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of SSIS log location.
    """

    FILE = "File"

class SsisObjectMetadataType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of SSIS object metadata.
    """

    FOLDER = "Folder"
    PROJECT = "Project"
    PACKAGE = "Package"
    ENVIRONMENT = "Environment"

class SsisPackageLocationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of SSIS package location.
    """

    SSISDB = "SSISDB"
    FILE = "File"
    INLINE_PACKAGE = "InlinePackage"
    PACKAGE_STORE = "PackageStore"

class StoredProcedureParameterType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Stored procedure parameter type.
    """

    STRING = "String"
    INT = "Int"
    INT64 = "Int64"
    DECIMAL = "Decimal"
    GUID = "Guid"
    BOOLEAN = "Boolean"
    DATE = "Date"

class SybaseAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """AuthenticationType to be used for connection.
    """

    BASIC = "Basic"
    WINDOWS = "Windows"

class TeradataAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """AuthenticationType to be used for connection.
    """

    BASIC = "Basic"
    WINDOWS = "Windows"

class TeradataPartitionOption(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The partition mechanism that will be used for teradata read in parallel.
    """

    NONE = "None"
    HASH = "Hash"
    DYNAMIC_RANGE = "DynamicRange"

class TriggerRunStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Trigger run status.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    INPROGRESS = "Inprogress"

class TriggerRuntimeState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enumerates possible state of Triggers.
    """

    STARTED = "Started"
    STOPPED = "Stopped"
    DISABLED = "Disabled"

class TumblingWindowFrequency(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enumerates possible frequency option for the tumbling window trigger.
    """

    MINUTE = "Minute"
    HOUR = "Hour"

class VariableType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Variable type.
    """

    STRING = "String"
    BOOL = "Bool"
    ARRAY = "Array"

class WebActivityMethod(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The list of HTTP methods supported by a WebActivity.
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

class WebAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of authentication used to connect to the web table source.
    """

    BASIC = "Basic"
    ANONYMOUS = "Anonymous"
    CLIENT_CERTIFICATE = "ClientCertificate"

class WebHookActivityMethod(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The list of HTTP methods supported by a WebHook activity.
    """

    POST = "POST"
