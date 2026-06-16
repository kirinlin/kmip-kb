---
title: Tag Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.0","1.1","1.2","1.3","1.4","2.0","2.1"]
source_section: "11.56"
status: reviewed
related: ["ttlv-encoding", "item-data-types", "message-structure"]
keywords: ["tag", "TTLV tag", "42XXXX", "tag enumeration", "field identifier", "tag namespace", "420138"]
tag_hex: "420138"
xml_text: "Tag"
---

# Tag Enumeration

## Overview

The Tag enumeration is the master registry of TTLV tag values — the 3-byte `42xxxx` identifiers that name every field, structure, and enumeration in a KMIP message. Every field in every KMIP request or response is prefixed with a 3-byte tag drawn from this enumeration, giving KMIP's encoding a self-describing character: a parser needs only the tag registry to identify any field it encounters, without a separate per-message schema.

Tags are grouped by range:
- `420000`–`42FFFF`: Standard KMIP tags defined in this enumeration.
- `540000`–`54FFFF`: Extension tags. The range `540000`–`547FFF` is available for private-use extensions; `548000`–`54FFFF` is reserved for KMIP specification use.

## Encoding (Tag / Type / Length / Value)

Tags appear as the first 3 bytes of every TTLV item: `[Tag 3B][Type 1B][Length 4B][Value nB][Padding]`. The type byte following the tag identifies the data type (Structure, Integer, Enumeration, etc.). Tags themselves are not encoded as TTLV values; they are the framing identifiers.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Activation Date | `00420001` | `ActivationDate` |  |
| Application Data | `00420002` | `ApplicationData` |  |
| Application Namespace | `00420003` | `ApplicationNamespace` |  |
| Application Specific Information | `00420004` | `ApplicationSpecificInformation` |  |
| Archive Date | `00420005` | `ArchiveDate` |  |
| Asynchronous Correlation Value | `00420006` | `AsynchronousCorrelationValue` |  |
| Asynchronous Indicator | `00420007` | `AsynchronousIndicator` |  |
| Attribute | `00420008` | `Attribute` |  |
| Attribute Name | `0042000A` | `AttributeName` |  |
| Attribute Value | `0042000B` | `AttributeValue` |  |
| Authentication | `0042000C` | `Authentication` |  |
| Batch Count | `0042000D` | `BatchCount` |  |
| Batch Error Continuation Option | `0042000E` | `BatchErrorContinuationOption` |  |
| Batch Item | `0042000F` | `BatchItem` |  |
| Batch Order Option | `00420010` | `BatchOrderOption` |  |
| Block Cipher Mode | `00420011` | `BlockCipherMode` |  |
| Cancellation Result | `00420012` | `CancellationResult` |  |
| Certificate | `00420013` | `Certificate` |  |
| Certificate Request | `00420018` | `CertificateRequest` |  |
| Certificate Request Type | `00420019` | `CertificateRequestType` |  |
| Certificate Type | `0042001D` | `CertificateType` |  |
| Certificate Value | `0042001E` | `CertificateValue` |  |
| Compromise Date | `00420020` | `CompromiseDate` |  |
| Compromise Occurrence Date | `00420021` | `CompromiseOccurrenceDate` |  |
| Contact Information | `00420022` | `ContactInformation` |  |
| Credential | `00420023` | `Credential` |  |
| Credential Type | `00420024` | `CredentialType` |  |
| Credential Value | `00420025` | `CredentialValue` |  |
| Criticality Indicator | `00420026` | `CriticalityIndicator` |  |
| CRT Coefficient | `00420027` | `CRTCoefficient` |  |
| Cryptographic Algorithm | `00420028` | `CryptographicAlgorithm` |  |
| Cryptographic Domain Parameters | `00420029` | `CryptographicDomainParameters` |  |
| Cryptographic Length | `0042002A` | `CryptographicLength` |  |
| Cryptographic Parameters | `0042002B` | `CryptographicParameters` |  |
| Cryptographic Usage Mask | `0042002C` | `CryptographicUsageMask` |  |
| D | `0042002E` | `D` |  |
| Deactivation Date | `0042002F` | `DeactivationDate` |  |
| Derivation Data | `00420030` | `DerivationData` |  |
| Derivation Method | `00420031` | `DerivationMethod` |  |
| Derivation Parameters | `00420032` | `DerivationParameters` |  |
| Destroy Date | `00420033` | `DestroyDate` |  |
| Digest | `00420034` | `Digest` |  |
| Digest Value | `00420035` | `DigestValue` |  |
| Encryption Key Information | `00420036` | `EncryptionKeyInformation` |  |
| G | `00420037` | `G` |  |
| Hashing Algorithm | `00420038` | `HashingAlgorithm` |  |
| Initial Date | `00420039` | `InitialDate` |  |
| Initialization Vector | `0042003A` | `InitializationVector` |  |
| Iteration Count | `0042003C` | `IterationCount` |  |
| IV/Counter/Nonce | `0042003D` | `IVCounterNonce` |  |
| J | `0042003E` | `J` |  |
| Key | `0042003F` | `Key` |  |
| Key Block | `00420040` | `KeyBlock` |  |
| Key Compression Type | `00420041` | `KeyCompressionType` |  |
| Key Format Type | `00420042` | `KeyFormatType` |  |
| Key Material | `00420043` | `KeyMaterial` |  |
| Key Part Identifier | `00420044` | `KeyPartIdentifier` |  |
| Key Value | `00420045` | `KeyValue` |  |
| Key Wrapping Data | `00420046` | `KeyWrappingData` |  |
| Key Wrapping Specification | `00420047` | `KeyWrappingSpecification` |  |
| Last Change Date | `00420048` | `LastChangeDate` |  |
| Lease Time | `00420049` | `LeaseTime` |  |
| Link | `0042004A` | `Link` |  |
| Link Type | `0042004B` | `LinkType` |  |
| Linked Object Identifier | `0042004C` | `LinkedObjectIdentifier` |  |
| MAC/Signature | `0042004D` | `MACSignature` |  |
| MAC/Signature Key Information | `0042004E` | `MACSignatureKeyInformation` |  |
| Maximum Items | `0042004F` | `MaximumItems` |  |
| Maximum Response Size | `00420050` | `MaximumResponseSize` |  |
| Modulus | `00420052` | `Modulus` |  |
| Name Type | `00420054` | `NameType` |  |
| Name Value | `00420055` | `NameValue` |  |
| Object Group | `00420056` | `ObjectGroup` |  |
| Object Type | `00420057` | `ObjectType` |  |
| Offset | `00420058` | `Offset` |  |
| Opaque Data Type | `00420059` | `OpaqueDataType` |  |
| Opaque Data Value | `0042005A` | `OpaqueDataValue` |  |
| Opaque Object | `0042005B` | `OpaqueObject` |  |
| Operation | `0042005C` | `Operation` |  |
| P | `0042005E` | `P` |  |
| Padding Method | `0042005F` | `PaddingMethod` |  |
| Prime Exponent P | `00420060` | `PrimeExponentP` |  |
| Prime Exponent Q | `00420061` | `PrimeExponentQ` |  |
| Prime Field Size | `00420062` | `PrimeFieldSize` |  |
| Private Exponent | `00420063` | `PrivateExponent` |  |
| Private Key | `00420064` | `PrivateKey` |  |
| Private Key Unique Identifier | `00420066` | `PrivateKeyUniqueIdentifier` |  |
| Process Start Date | `00420067` | `ProcessStartDate` |  |
| Protect Stop Date | `00420068` | `ProtectStopDate` |  |
| Protocol Version | `00420069` | `ProtocolVersion` |  |
| Protocol Version Major | `0042006A` | `ProtocolVersionMajor` |  |
| Protocol Version Minor | `0042006B` | `ProtocolVersionMinor` |  |
| Public Exponent | `0042006C` | `PublicExponent` |  |
| Public Key | `0042006D` | `PublicKey` |  |
| Public Key Unique Identifier | `0042006F` | `PublicKeyUniqueIdentifier` |  |
| Put Function | `00420070` | `PutFunction` |  |
| Q | `00420071` | `Q` |  |
| Q String | `00420072` | `QString` |  |
| Qlength | `00420073` | `Qlength` |  |
| Query Function | `00420074` | `QueryFunction` |  |
| Recommended Curve | `00420075` | `RecommendedCurve` |  |
| Replaced Unique Identifier | `00420076` | `ReplacedUniqueIdentifier` |  |
| Request Header | `00420077` | `RequestHeader` |  |
| Request Message | `00420078` | `RequestMessage` |  |
| Request Payload | `00420079` | `RequestPayload` |  |
| Response Header | `0042007A` | `ResponseHeader` |  |
| Response Message | `0042007B` | `ResponseMessage` |  |
| Response Payload | `0042007C` | `ResponsePayload` |  |
| Result Message | `0042007D` | `ResultMessage` |  |
| Result Reason | `0042007E` | `ResultReason` |  |
| Result Status | `0042007F` | `ResultStatus` |  |
| Revocation Message | `00420080` | `RevocationMessage` |  |
| Revocation Reason | `00420081` | `RevocationReason` |  |
| Revocation Reason Code | `00420082` | `RevocationReasonCode` |  |
| Key Role Type | `00420083` | `KeyRoleType` |  |
| Salt | `00420084` | `Salt` |  |
| Secret Data | `00420085` | `SecretData` |  |
| Secret Data Type | `00420086` | `SecretDataType` |  |
| Server Information | `00420088` | `ServerInformation` |  |
| Split Key | `00420089` | `SplitKey` |  |
| Split Key Method | `0042008A` | `SplitKeyMethod` |  |
| Split Key Parts | `0042008B` | `SplitKeyParts` |  |
| Split Key Threshold | `0042008C` | `SplitKeyThreshold` |  |
| State | `0042008D` | `State` |  |
| Storage Status Mask | `0042008E` | `StorageStatusMask` |  |
| Symmetric Key | `0042008F` | `SymmetricKey` |  |
| Time Stamp | `00420092` | `TimeStamp` |  |
| Unique Batch Item ID | `00420093` | `UniqueBatchItemID` |  |
| Unique Identifier | `00420094` | `UniqueIdentifier` |  |
| Usage Limits | `00420095` | `UsageLimits` |  |
| Usage Limits Count | `00420096` | `UsageLimitsCount` |  |
| Usage Limits Total | `00420097` | `UsageLimitsTotal` |  |
| Usage Limits Unit | `00420098` | `UsageLimitsUnit` |  |
| Username | `00420099` | `Username` |  |
| Validity Date | `0042009A` | `ValidityDate` |  |
| Validity Indicator | `0042009B` | `ValidityIndicator` |  |
| Vendor Identification | `0042009D` | `VendorIdentification` |  |
| Wrapping Method | `0042009E` | `WrappingMethod` |  |
| X | `0042009F` | `X` |  |
| Y | `004200A0` | `Y` |  |
| Password | `004200A1` | `Password` |  |
| Device Identifier | `004200A2` | `DeviceIdentifier` |  |
| Encoding Option | `004200A3` | `EncodingOption` |  |
| Fresh | `004200A8` | `Fresh` |  |
| Machine Identifier | `004200A9` | `MachineIdentifier` |  |
| Media Identifier | `004200AA` | `MediaIdentifier` |  |
| Network Identifier | `004200AB` | `NetworkIdentifier` |  |
| Object Group Member | `004200AC` | `ObjectGroupMember` |  |
| Certificate Length | `004200AD` | `CertificateLength` |  |
| Digital Signature Algorithm | `004200AE` | `DigitalSignatureAlgorithm` |  |
| Certificate Serial Number | `004200AF` | `CertificateSerialNumber` |  |
| Device Serial Number | `004200B0` | `DeviceSerialNumber` |  |
| Issuer Alternative Name | `004200B1` | `IssuerAlternativeName` |  |
| Issuer Distinguished Name | `004200B2` | `IssuerDistinguishedName` |  |
| Subject Alternative Name | `004200B3` | `SubjectAlternativeName` |  |
| Subject Distinguished Name | `004200B4` | `SubjectDistinguishedName` |  |
| X.509 Certificate Identifier | `004200B5` | `X_509CertificateIdentifier` |  |
| X.509 Certificate Issuer | `004200B6` | `X_509CertificateIssuer` |  |
| X.509 Certificate Subject | `004200B7` | `X_509CertificateSubject` |  |
| Key Value Location | `004200B8` | `KeyValueLocation` |  |
| Key Value Location Value | `004200B9` | `KeyValueLocationValue` |  |
| Key Value Location Type | `004200BA` | `KeyValueLocationType` |  |
| Key Value Present | `004200BB` | `KeyValuePresent` |  |
| Original Creation Date | `004200BC` | `OriginalCreationDate` |  |
| PGP Key | `004200BD` | `PGPKey` |  |
| PGP Key Version | `004200BE` | `PGPKeyVersion` |  |
| Alternative Name | `004200BF` | `AlternativeName` |  |
| Alternative Name Value | `004200C0` | `AlternativeNameValue` |  |
| Alternative Name Type | `004200C1` | `AlternativeNameType` |  |
| Data | `004200C2` | `Data` |  |
| Signature Data | `004200C3` | `SignatureData` |  |
| Data Length | `004200C4` | `DataLength` |  |
| Random IV | `004200C5` | `RandomIV` |  |
| MAC Data | `004200C6` | `MACData` |  |
| Attestation Type | `004200C7` | `AttestationType` |  |
| Nonce | `004200C8` | `Nonce` |  |
| Nonce ID | `004200C9` | `NonceID` |  |
| Nonce Value | `004200CA` | `NonceValue` |  |
| Attestation Measurement | `004200CB` | `AttestationMeasurement` |  |
| Attestation Assertion | `004200CC` | `AttestationAssertion` |  |
| IV Length | `004200CD` | `IVLength` |  |
| Tag Length | `004200CE` | `TagLength` |  |
| Fixed Field Length | `004200CF` | `FixedFieldLength` |  |
| Counter Length | `004200D0` | `CounterLength` |  |
| Initial Counter Value | `004200D1` | `InitialCounterValue` |  |
| Invocation Field Length | `004200D2` | `InvocationFieldLength` |  |
| Attestation Capable Indicator | `004200D3` | `AttestationCapableIndicator` |  |
| Offset Items | `004200D4` | `OffsetItems` |  |
| Located Items | `004200D5` | `LocatedItems` |  |
| Correlation Value | `004200D6` | `CorrelationValue` |  |
| Init Indicator | `004200D7` | `InitIndicator` |  |
| Final Indicator | `004200D8` | `FinalIndicator` |  |
| RNG Parameters | `004200D9` | `RNGParameters` |  |
| RNG Algorithm | `004200DA` | `RNGAlgorithm` |  |
| DRBG Algorithm | `004200DB` | `DRBGAlgorithm` |  |
| FIPS186 Variation | `004200DC` | `FIPS186Variation` |  |
| Prediction Resistance | `004200DD` | `PredictionResistance` |  |
| Random Number Generator | `004200DE` | `RandomNumberGenerator` |  |
| Validation Information | `004200DF` | `ValidationInformation` |  |
| Validation Authority Type | `004200E0` | `ValidationAuthorityType` |  |
| Validation Authority Country | `004200E1` | `ValidationAuthorityCountry` |  |
| Validation Authority URI | `004200E2` | `ValidationAuthorityURI` |  |
| Validation Version Major | `004200E3` | `ValidationVersionMajor` |  |
| Validation Version Minor | `004200E4` | `ValidationVersionMinor` |  |
| Validation Type | `004200E5` | `ValidationType` |  |
| Validation Level | `004200E6` | `ValidationLevel` |  |
| Validation Certificate Identifier | `004200E7` | `ValidationCertificateIdentifier` |  |
| Validation Certificate URI | `004200E8` | `ValidationCertificateURI` |  |
| Validation Vendor URI | `004200E9` | `ValidationVendorURI` |  |
| Validation Profile | `004200EA` | `ValidationProfile` |  |
| Profile Information | `004200EB` | `ProfileInformation` |  |
| Profile Name | `004200EC` | `ProfileName` |  |
| Server URI | `004200ED` | `ServerURI` |  |
| Server Port | `004200EE` | `ServerPort` |  |
| Streaming Capability | `004200EF` | `StreamingCapability` |  |
| Asynchronous Capability | `004200F0` | `AsynchronousCapability` |  |
| Attestation Capability | `004200F1` | `AttestationCapability` |  |
| Unwrap Mode | `004200F2` | `UnwrapMode` |  |
| Destroy Action | `004200F3` | `DestroyAction` |  |
| Shredding Algorithm | `004200F4` | `ShreddingAlgorithm` |  |
| RNG Mode | `004200F5` | `RNGMode` |  |
| Client Registration Method | `004200F6` | `ClientRegistrationMethod` |  |
| Capability Information | `004200F7` | `CapabilityInformation` |  |
| Key Wrap Type | `004200F8` | `KeyWrapType` |  |
| Batch Undo Capability | `004200F9` | `BatchUndoCapability` |  |
| Batch Continue Capability | `004200FA` | `BatchContinueCapability` |  |
| PKCS#12 Friendly Name | `004200FB` | `PKCS_12FriendlyName` |  |
| Description | `004200FC` | `Description` |  |
| Comment | `004200FD` | `Comment` |  |
| Authenticated Encryption Additional Data | `004200FE` | `AuthenticatedEncryptionAdditionalData` |  |
| Authenticated Encryption Tag | `004200FF` | `AuthenticatedEncryptionTag` |  |
| Salt Length | `00420100` | `SaltLength` |  |
| Mask Generator | `00420101` | `MaskGenerator` |  |
| Mask Generator Hashing Algorithm | `00420102` | `MaskGeneratorHashingAlgorithm` |  |
| P Source | `00420103` | `PSource` |  |
| Trailer Field | `00420104` | `TrailerField` |  |
| Client Correlation Value | `00420105` | `ClientCorrelationValue` |  |
| Server Correlation Value | `00420106` | `ServerCorrelationValue` |  |
| Digested Data | `00420107` | `DigestedData` |  |
| Certificate Subject CN | `00420108` | `CertificateSubjectCN` |  |
| Certificate Subject O | `00420109` | `CertificateSubjectO` |  |
| Certificate Subject OU | `0042010A` | `CertificateSubjectOU` |  |
| Certificate Subject Email | `0042010B` | `CertificateSubjectEmail` |  |
| Certificate Subject C | `0042010C` | `CertificateSubjectC` |  |
| Certificate Subject ST | `0042010D` | `CertificateSubjectST` |  |
| Certificate Subject L | `0042010E` | `CertificateSubjectL` |  |
| Certificate Subject UID | `0042010F` | `CertificateSubjectUID` |  |
| Certificate Subject Serial Number | `00420110` | `CertificateSubjectSerialNumber` |  |
| Certificate Subject Title | `00420111` | `CertificateSubjectTitle` |  |
| Certificate Subject DC | `00420112` | `CertificateSubjectDC` |  |
| Certificate Subject DN Qualifier | `00420113` | `CertificateSubjectDNQualifier` |  |
| Certificate Issuer CN | `00420114` | `CertificateIssuerCN` |  |
| Certificate Issuer O | `00420115` | `CertificateIssuerO` |  |
| Certificate Issuer OU | `00420116` | `CertificateIssuerOU` |  |
| Certificate Issuer Email | `00420117` | `CertificateIssuerEmail` |  |
| Certificate Issuer C | `00420118` | `CertificateIssuerC` |  |
| Certificate Issuer ST | `00420119` | `CertificateIssuerST` |  |
| Certificate Issuer L | `0042011A` | `CertificateIssuerL` |  |
| Certificate Issuer UID | `0042011B` | `CertificateIssuerUID` |  |
| Certificate Issuer Serial Number | `0042011C` | `CertificateIssuerSerialNumber` |  |
| Certificate Issuer Title | `0042011D` | `CertificateIssuerTitle` |  |
| Certificate Issuer DC | `0042011E` | `CertificateIssuerDC` |  |
| Certificate Issuer DN Qualifier | `0042011F` | `CertificateIssuerDNQualifier` |  |
| Sensitive | `00420120` | `Sensitive` |  |
| Always Sensitive | `00420121` | `AlwaysSensitive` |  |
| Extractable | `00420122` | `Extractable` |  |
| Never Extractable | `00420123` | `NeverExtractable` |  |
| Replace Existing | `00420124` | `ReplaceExisting` |  |
| Attributes | `00420125` | `Attributes` |  |
| Common Attributes | `00420126` | `CommonAttributes` |  |
| Private Key Attributes | `00420127` | `PrivateKeyAttributes` |  |
| Public Key Attributes | `00420128` | `PublicKeyAttributes` |  |
| Server Name | `0042012D` | `ServerName` |  |
| Server Serial Number | `0042012E` | `ServerSerialNumber` |  |
| Server Version | `0042012F` | `ServerVersion` |  |
| Server Load | `00420130` | `ServerLoad` |  |
| Product Name | `00420131` | `ProductName` |  |
| Build Level | `00420132` | `BuildLevel` |  |
| Build Date | `00420133` | `BuildDate` |  |
| Cluster Info | `00420134` | `ClusterInfo` |  |
| Alternate Failover Endpoints | `00420135` | `AlternateFailoverEndpoints` |  |
| Short Unique Identifier | `00420136` | `ShortUniqueIdentifier` |  |
| Tag | `00420138` | `Tag` |  |
| Certificate Request Unique Identifier | `00420139` | `CertificateRequestUniqueIdentifier` |  |
| NIST Key Type | `0042013A` | `NISTKeyType` |  |
| Attribute Reference | `0042013B` | `AttributeReference` |  |
| Current Attribute | `0042013C` | `CurrentAttribute` |  |
| New Attribute | `0042013D` | `NewAttribute` |  |
| Certificate Request Value | `00420140` | `CertificateRequestValue` |  |
| Log Message | `00420141` | `LogMessage` |  |
| Profile Version | `00420142` | `ProfileVersion` |  |
| Profile Version Major | `00420143` | `ProfileVersionMajor` |  |
| Profile Version Minor | `00420144` | `ProfileVersionMinor` |  |
| Protection Level | `00420145` | `ProtectionLevel` |  |
| Protection Period | `00420146` | `ProtectionPeriod` |  |
| Quantum Safe | `00420147` | `QuantumSafe` |  |
| Quantum Safe Capability | `00420148` | `QuantumSafeCapability` |  |
| Ticket | `00420149` | `Ticket` |  |
| Ticket Type | `0042014A` | `TicketType` |  |
| Ticket Value | `0042014B` | `TicketValue` |  |
| Request Count | `0042014C` | `RequestCount` |  |
| Rights | `0042014D` | `Rights` |  |
| Objects | `0042014E` | `Objects` |  |
| Operations | `0042014F` | `Operations` |  |
| Right | `00420150` | `Right` |  |
| Endpoint Role | `00420151` | `EndpointRole` |  |
| Defaults Information | `00420152` | `DefaultsInformation` |  |
| Object Defaults | `00420153` | `ObjectDefaults` |  |
| Ephemeral | `00420154` | `Ephemeral` |  |
| Server Hashed Password | `00420155` | `ServerHashedPassword` |  |
| One Time Password | `00420156` | `OneTimePassword` |  |
| Hashed Password | `00420157` | `HashedPassword` |  |
| Adjustment Type | `00420158` | `AdjustmentType` |  |
| PKCS#11 Interface | `00420159` | `PKCS_11Interface` |  |
| PKCS#11 Function | `0042015A` | `PKCS_11Function` |  |
| PKCS#11 Input Parameters | `0042015B` | `PKCS_11InputParameters` |  |
| PKCS#11 Output Parameters | `0042015C` | `PKCS_11OutputParameters` |  |
| PKCS#11 Return Code | `0042015D` | `PKCS_11ReturnCode` |  |
| Protection Storage Mask | `0042015E` | `ProtectionStorageMask` |  |
| Protection Storage Masks | `0042015F` | `ProtectionStorageMasks` |  |
| Interop Function | `00420160` | `InteropFunction` |  |
| Interop Identifier | `00420161` | `InteropIdentifier` |  |
| Adjustment Value | `00420162` | `AdjustmentValue` |  |
| Common Protection Storage Masks | `00420163` | `CommonProtectionStorageMasks` |  |
| Private Protection Storage Masks | `00420164` | `PrivateProtectionStorageMasks` |  |
| Public Protection Storage Masks | `00420165` | `PublicProtectionStorageMasks` |  |
| Object Groups | `00420166` | `ObjectGroups` |  |
| Object Types | `00420167` | `ObjectTypes` |  |
| Constraints | `00420168` | `Constraints` |  |
| Constraint | `00420169` | `Constraint` |  |

The Tag Enumeration is large — KMIP v2.1 defines over 400 standard tags — covering every field name used in the specification. Examples include:

- `420001` — Activation Date
- `420028` — Cryptographic Algorithm
- `42002A` — Cryptographic Length
- `42002C` — Cryptographic Usage Mask
- `420040` — Key Block
- `420042` — Key Format Type
- `420057` — Object Type
- `42005C` — Operation
- `420094` — Unique Identifier
- `4200BE` — Name
- `4200C3` — State

Vendor extension tags in the `54xxxx` range do not appear in this enumeration; they are defined by the extending party.

## Examples

A TTLV decoder encountering `42 00 28 05 00 00 00 04 00 00 00 03 00 00 00 00` parses tag `420028` (Cryptographic Algorithm), type `05` (Enumeration), length `4`, value `3` (AES), with 4 bytes of padding.

## Related

[TTLV Encoding](../encoding/ttlv-encoding.md) · [Item Data Types](../references/item-data-types.md) · [Message Structure](../messages/message-structure.md)
