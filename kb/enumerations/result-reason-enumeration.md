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
| Operation Canceled By Requester | `00000009` | `OperationCanceledByRequester` | The client explicitly canceled the asynchronous operation via a Cancel request. |
| Cryptographic Failure | `0000000A` | `CryptographicFailure` | A cryptographic operation (sign, verify, encrypt) failed — for example, an invalid signature. |
| Permission Denied | `0000000C` | `PermissionDenied` | The authenticated principal does not have the right to perform the operation on the target object. |
| Object Archived | `0000000D` | `ObjectArchived` | The referenced object has been moved to offline archival storage and is not immediately available for the requested operation. |
| Application Namespace Not Supported | `0000000F` | `ApplicationNamespaceNotSupported` | The Application Namespace specified in the request is not supported by the server. |
| Key Format Type Not Supported | `00000010` | `KeyFormatTypeNotSupported` | The server does not support the Key Format Type requested for the key material. |
| Key Compression Type Not Supported | `00000011` | `KeyCompressionTypeNotSupported` | The server does not support the Key Compression Type requested for the key material. |
| Encoding Option Error | `00000012` | `EncodingOptionError` | An error occurred with the Encoding Option specified in the request, such as requesting an encoding the server cannot produce. |
| Key Value Not Present | `00000013` | `KeyValueNotPresent` | The key material is absent — for example, only the metadata stub remains after the key value was destroyed. |
| Attestation Required | `00000014` | `AttestationRequired` | The server requires attestation data that was not supplied in the request. |
| Attestation Failed | `00000015` | `AttestationFailed` | The attestation data supplied in the request did not pass the server's verification checks. |
| Sensitive | `00000016` | `Sensitive` | The object is marked sensitive and its key material cannot be exported or revealed in plaintext. |
| Not Extractable | `00000017` | `NotExtractable` | The object's Extractable attribute is set to false, preventing the key value from being returned via Get or Get Attributes. |
| Object Already Exists | `00000018` | `ObjectAlreadyExists` | A Create or Register request conflicts with an existing object. |
| Invalid Ticket | `00000019` | `InvalidTicket` | The ticket value in the request is unrecognized, already used, or has expired. |
| Usage Limit Exceeded | `0000001A` | `UsageLimitExceeded` | The object has reached its maximum permitted use count as defined by the Usage Limits attribute. |
| Numeric Range | `0000001B` | `NumericRange` | A numeric value in the request falls outside the permitted range for that field. |
| Invalid Data Type | `0000001C` | `InvalidDataType` | A field in the request carries a value whose TTLV type does not match what the server expects. |
| Read Only Attribute | `0000001D` | `ReadOnlyAttribute` | An attempt was made to set or modify an attribute that the server treats as read-only. |
| Multi Valued Attribute | `0000001E` | `MultiValuedAttribute` | The operation requires a single-valued attribute but the object carries multiple values for that attribute. |
| Unsupported Attribute | `0000001F` | `UnsupportedAttribute` | The server does not support the attribute named in the request. |
| Attribute Instance Not Found | `00000020` | `AttributeInstanceNotFound` | No attribute instance matching the specified index was found on the object. |
| Attribute Not Found | `00000021` | `AttributeNotFound` | The specified attribute does not exist on the managed object. |
| Attribute Read Only | `00000022` | `AttributeReadOnly` | The client attempted to modify an attribute that is designated read-only for that object type or lifecycle state. |
| Attribute Single Valued | `00000023` | `AttributeSingleValued` | An attempt was made to add a second value to an attribute defined as single-valued. |
| Bad Cryptographic Parameters | `00000024` | `BadCryptographicParameters` | The Cryptographic Parameters structure in the request is invalid, incomplete, or incompatible with the key or operation. |
| Bad Password | `00000025` | `BadPassword` | The password provided for a password-based key derivation operation or credential check is incorrect. |
| Codec Error | `00000026` | `CodecError` | An encoding or decoding error occurred that does not map to a more specific reason code. |
| Illegal Object Type | `00000028` | `IllegalObjectType` | The requested operation is not applicable to the type of managed object referenced — for example, applying a key-only operation to a certificate. |
| Incompatible Cryptographic Usage Mask | `00000029` | `IncompatibleCryptographicUsageMask` | The object's Cryptographic Usage Mask does not permit the requested operation — for example, using a key that lacks the Decrypt bit to decrypt data. |
| Internal Server Error | `0000002A` | `InternalServerError` | An unexpected condition within the server prevented the operation from completing; no more specific reason code applies. |
| Invalid Asynchronous Correlation Value | `0000002B` | `InvalidAsynchronousCorrelationValue` | The Asynchronous Correlation Value in a Poll or Cancel request does not match any pending asynchronous operation. |
| Invalid Attribute | `0000002C` | `InvalidAttribute` | The attribute structure is malformed or references an unrecognized attribute name. |
| Invalid Attribute Value | `0000002D` | `InvalidAttributeValue` | The value supplied for an attribute is outside the permitted set or violates an attribute-specific constraint. |
| Invalid Correlation Value | `0000002E` | `InvalidCorrelationValue` | The batch item Correlation Value does not match any outstanding correlated operation. |
| Invalid CSR | `0000002F` | `InvalidCSR` | The Certificate Signing Request in the request is malformed or cannot be parsed. |
| Invalid Object Type | `00000030` | `InvalidObjectType` | The Object Type in the request does not match the actual type of the referenced managed object. |
| Key Wrap Type Not Supported | `00000032` | `KeyWrapTypeNotSupported` | The server does not support the wrap type specified in the Key Wrapping Specification. |
| Missing Initialization Vector | `00000034` | `MissingInitializationVector` | A cipher mode that requires an IV or nonce was requested, but none was provided. |
| Non Unique Name Attribute | `00000035` | `NonUniqueNameAttribute` | The Name attribute value in the request conflicts with an existing object, violating a server uniqueness policy. |
| Object Destroyed | `00000036` | `ObjectDestroyed` | The referenced object has been destroyed and its key material is no longer available. |
| Object Not Found | `00000037` | `ObjectNotFound` | The managed object referenced by the request does not exist on the server. |
| Not Authorised | `00000039` | `NotAuthorised` | The authenticated principal is not authorised to perform the operation under server policy. |
| Server Limit Exceeded | `0000003A` | `ServerLimitExceeded` | A server-side resource or capacity limit was reached, such as the maximum number of managed objects. |
| Unknown Enumeration | `0000003B` | `UnknownEnumeration` | The request contains an enumeration value that the server does not recognize. |
| Unknown Tag | `0000003D` | `UnknownTag` | The request contains a TTLV tag that the server does not recognize. |
| Unsupported Cryptographic Parameters | `0000003E` | `UnsupportedCryptographicParameters` | The cryptographic algorithm, key length, or parameter combination is not supported by the server. |
| Unsupported Protocol Version | `0000003F` | `UnsupportedProtocolVersion` | The protocol version in the request header is not supported by the server. |
| Wrapping Object Archived | `00000040` | `WrappingObjectArchived` | The key designated to wrap the object has been archived and is not immediately available. |
| Wrapping Object Destroyed | `00000041` | `WrappingObjectDestroyed` | The key used to wrap the object has been destroyed; the wrapped value cannot be recovered. |
| Wrapping Object Not Found | `00000042` | `WrappingObjectNotFound` | The key specified for wrapping or unwrapping does not exist on the server. |
| Wrong Key Lifecycle State | `00000043` | `WrongKeyLifecycleState` | The operation is not permitted given the object's current state (e.g., using a Deactivated key for encryption). |
| Protection Storage Unavailable | `00000044` | `ProtectionStorageUnavailable` | The server cannot store the object in the protection environment required by the Protection Storage Mask attribute. |
| PKCS#11 Codec Error | `00000045` | `PKCS_11CodecError` | An encoding or decoding error occurred in the PKCS#11 interface layer. |
| PKCS#11 Invalid Function | `00000046` | `PKCS_11InvalidFunction` | The PKCS#11 function call is invalid or not permitted in the current context or session state. |
| PKCS#11 Invalid Interface | `00000047` | `PKCS_11InvalidInterface` | The PKCS#11 interface version or slot is not compatible with the server's PKCS#11 implementation. |
| Private Protection Storage Unavailable | `00000048` | `PrivateProtectionStorageUnavailable` | The protection storage designated for private key material is not accessible. |
| Public Protection Storage Unavailable | `00000049` | `PublicProtectionStorageUnavailable` | The protection storage designated for public key material is not accessible. |
| Unknown Object Group | `0000004A` | `UnknownObjectGroup` | The Object Group attribute value in the request does not correspond to any known group on the server. |
| Constraint Violation | `0000004B` | `ConstraintViolation` | An attribute-based constraint rule was violated. |
| Duplicate Process Request | `0000004C` | `DuplicateProcessRequest` | An identical request has already been submitted and is pending or was recently completed. |
| General Failure | `00000100` | `GeneralFailure` | A catch-all for server-side failures that do not map to any more specific reason code. |

## Examples

A Get request for a non-existent key returns Result Status = **Operation Failed**, Result Reason = **Item Not Found**. A Destroy request on a key that is still Active returns Result Reason = **Wrong Key Lifecycle State**.

## Related

[Result Status Enumeration](result-status-enumeration.md) · [Error Handling](../concepts/error-handling.md) · [Message Structure](../messages/message-structure.md)
