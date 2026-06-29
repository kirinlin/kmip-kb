---
title: Result Reason Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.46"
status: reviewed
related: ["result-status-enumeration", "message-structure", "error-handling"]
keywords: ["result reason", "error code", "failure reason", "item not found", "operation not supported", "permission denied", "42007E", "ResultReason"]
tag_hex: "42007E"
xml_text: "ResultReason"
tag_type: "Enumeration"
---

# Result Reason Enumeration

## Overview

The Result Reason enumeration provides the specific error code within a failed batch item response. Where [Result Status](result-status-enumeration.md) conveys the broad outcome (success vs. failure vs. pending), Result Reason pinpoints why a failure occurred. Both appear in every batch item response alongside an optional Result Message text string, giving clients structured error information they can respond to programmatically.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Item Not Found | `00000001` | `ItemNotFound` | The Unique Identifier in the request does not correspond to any managed object on the server. The most frequent error for well-formed but referentially-invalid requests. |
| Response Too Large | `00000002` | `ResponseTooLarge` | The server cannot return all requested data within a single response message. The client must use paging or narrow its request. |
| Authentication Not Successful | `00000003` | `AuthenticationNotSuccessful` | The credential supplied is invalid, expired, or otherwise rejected by the authentication mechanism. |
| Invalid Message | `00000004` | `InvalidMessage` | The request structure is malformed at the TTLV or message-structure level. |
| Operation Not Supported | `00000005` | `OperationNotSupported` | The server does not implement the requested operation. |
| Missing Data | `00000006` | `MissingData` | A required field is absent from the request. |
| Invalid Field | `00000007` | `InvalidField` | A field value is syntactically or semantically incorrect. |
| Feature Not Supported | `00000008` | `FeatureNotSupported` | The server supports the operation in general but not the specific combination of parameters or options requested. |
| Operation Canceled By Requester | `00000009` | `OperationCanceledByRequester` |  |
| Cryptographic Failure | `0000000A` | `CryptographicFailure` | A cryptographic operation (sign, verify, encrypt) failed — for example, an invalid signature. |
| Permission Denied | `0000000C` | `PermissionDenied` | The authenticated principal does not have the right to perform the operation on the target object. |
| Object Archived | `0000000D` | `ObjectArchived` |  |
| Application Namespace Not Supported | `0000000F` | `ApplicationNamespaceNotSupported` |  |
| Key Format Type Not Supported | `00000010` | `KeyFormatTypeNotSupported` |  |
| Key Compression Type Not Supported | `00000011` | `KeyCompressionTypeNotSupported` |  |
| Encoding Option Error | `00000012` | `EncodingOptionError` |  |
| Key Value Not Present | `00000013` | `KeyValueNotPresent` |  |
| Attestation Required | `00000014` | `AttestationRequired` |  |
| Attestation Failed | `00000015` | `AttestationFailed` |  |
| Sensitive | `00000016` | `Sensitive` |  |
| Not Extractable | `00000017` | `NotExtractable` |  |
| Object Already Exists | `00000018` | `ObjectAlreadyExists` | A Create or Register request conflicts with an existing object. |
| Invalid Ticket | `00000019` | `InvalidTicket` |  |
| Usage Limit Exceeded | `0000001A` | `UsageLimitExceeded` |  |
| Numeric Range | `0000001B` | `NumericRange` |  |
| Invalid Data Type | `0000001C` | `InvalidDataType` |  |
| Read Only Attribute | `0000001D` | `ReadOnlyAttribute` |  |
| Multi Valued Attribute | `0000001E` | `MultiValuedAttribute` |  |
| Unsupported Attribute | `0000001F` | `UnsupportedAttribute` |  |
| Attribute Instance Not Found | `00000020` | `AttributeInstanceNotFound` |  |
| Attribute Not Found | `00000021` | `AttributeNotFound` |  |
| Attribute Read Only | `00000022` | `AttributeReadOnly` |  |
| Attribute Single Valued | `00000023` | `AttributeSingleValued` |  |
| Bad Cryptographic Parameters | `00000024` | `BadCryptographicParameters` |  |
| Bad Password | `00000025` | `BadPassword` |  |
| Codec Error | `00000026` | `CodecError` |  |
| Illegal Object Type | `00000028` | `IllegalObjectType` |  |
| Incompatible Cryptographic Usage Mask | `00000029` | `IncompatibleCryptographicUsageMask` |  |
| Internal Server Error | `0000002A` | `InternalServerError` |  |
| Invalid Asynchronous Correlation Value | `0000002B` | `InvalidAsynchronousCorrelationValue` |  |
| Invalid Attribute | `0000002C` | `InvalidAttribute` |  |
| Invalid Attribute Value | `0000002D` | `InvalidAttributeValue` |  |
| Invalid Correlation Value | `0000002E` | `InvalidCorrelationValue` |  |
| Invalid CSR | `0000002F` | `InvalidCSR` |  |
| Invalid Object Type | `00000030` | `InvalidObjectType` |  |
| Key Wrap Type Not Supported | `00000032` | `KeyWrapTypeNotSupported` |  |
| Missing Initialization Vector | `00000034` | `MissingInitializationVector` |  |
| Non Unique Name Attribute | `00000035` | `NonUniqueNameAttribute` |  |
| Object Destroyed | `00000036` | `ObjectDestroyed` |  |
| Object Not Found | `00000037` | `ObjectNotFound` |  |
| Not Authorised | `00000039` | `NotAuthorised` |  |
| Server Limit Exceeded | `0000003A` | `ServerLimitExceeded` |  |
| Unknown Enumeration | `0000003B` | `UnknownEnumeration` |  |
| Unknown Tag | `0000003D` | `UnknownTag` |  |
| Unsupported Cryptographic Parameters | `0000003E` | `UnsupportedCryptographicParameters` |  |
| Unsupported Protocol Version | `0000003F` | `UnsupportedProtocolVersion` |  |
| Wrapping Object Archived | `00000040` | `WrappingObjectArchived` |  |
| Wrapping Object Destroyed | `00000041` | `WrappingObjectDestroyed` |  |
| Wrapping Object Not Found | `00000042` | `WrappingObjectNotFound` |  |
| Wrong Key Lifecycle State | `00000043` | `WrongKeyLifecycleState` | The operation is not permitted given the object's current state (e.g., using a Deactivated key for encryption). |
| Protection Storage Unavailable | `00000044` | `ProtectionStorageUnavailable` | The server cannot store the object in the protection environment required by the Protection Storage Mask attribute. |
| PKCS#11 Codec Error | `00000045` | `PKCS_11CodecError` |  |
| PKCS#11 Invalid Function | `00000046` | `PKCS_11InvalidFunction` |  |
| PKCS#11 Invalid Interface | `00000047` | `PKCS_11InvalidInterface` |  |
| Private Protection Storage Unavailable | `00000048` | `PrivateProtectionStorageUnavailable` |  |
| Public Protection Storage Unavailable | `00000049` | `PublicProtectionStorageUnavailable` |  |
| Unknown Object Group | `0000004A` | `UnknownObjectGroup` |  |
| Constraint Violation | `0000004B` | `ConstraintViolation` | An attribute-based constraint rule was violated. |
| Duplicate Process Request | `0000004C` | `DuplicateProcessRequest` |  |
| General Failure | `00000100` | `GeneralFailure` |  |

## Examples

A Get request for a non-existent key returns Result Status = **Operation Failed**, Result Reason = **Item Not Found**. A Destroy request on a key that is still Active returns Result Reason = **Wrong Key Lifecycle State**.

## Related

[Result Status Enumeration](result-status-enumeration.md) · [Error Handling](../concepts/error-handling.md) · [Message Structure](../messages/message-structure.md)
