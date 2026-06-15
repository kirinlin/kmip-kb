---
title: Tag Enumeration
category: ttlv
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
- `0x420000`–`0x42FFFF`: Standard KMIP tags defined in this enumeration.
- `0x540000`–`0x54FFFF`: Extension tags. The range `0x540000`–`0x547FFF` is available for private-use extensions; `0x548000`–`0x54FFFF` is reserved for KMIP specification use.

## Encoding (Tag / Type / Length / Value)

Tags appear as the first 3 bytes of every TTLV item: `[Tag 3B][Type 1B][Length 4B][Value nB][Padding]`. The type byte following the tag identifies the data type (Structure, Integer, Enumeration, etc.). Tags themselves are not encoded as TTLV values; they are the framing identifiers.

## Fields & Structure

| Value | Hex | XML Text | Description |
|---|---|---|---|
| Activation Date | `0x00420001` | `ActivationDate` |  |
| Application Data | `0x00420002` | `ApplicationData` |  |
| Application Namespace | `0x00420003` | `ApplicationNamespace` |  |
| Application Specific Information | `0x00420004` | `ApplicationSpecificInformation` |  |
| Archive Date | `0x00420005` | `ArchiveDate` |  |
| Asynchronous Correlation Value | `0x00420006` | `AsynchronousCorrelationValue` |  |
| Asynchronous Indicator | `0x00420007` | `AsynchronousIndicator` |  |
| Attribute | `0x00420008` | `Attribute` |  |
| Attribute Name | `0x0042000A` | `AttributeName` |  |
| Attribute Value | `0x0042000B` | `AttributeValue` |  |
| Authentication | `0x0042000C` | `Authentication` |  |
| Batch Count | `0x0042000D` | `BatchCount` |  |
| Batch Error Continuation Option | `0x0042000E` | `BatchErrorContinuationOption` |  |
| Batch Item | `0x0042000F` | `BatchItem` |  |
| Batch Order Option | `0x00420010` | `BatchOrderOption` |  |
| Block Cipher Mode | `0x00420011` | `BlockCipherMode` |  |
| Cancellation Result | `0x00420012` | `CancellationResult` |  |
| Certificate | `0x00420013` | `Certificate` |  |
| Certificate Request | `0x00420018` | `CertificateRequest` |  |
| Certificate Request Type | `0x00420019` | `CertificateRequestType` |  |
| Certificate Type | `0x0042001D` | `CertificateType` |  |
| Certificate Value | `0x0042001E` | `CertificateValue` |  |
| Compromise Date | `0x00420020` | `CompromiseDate` |  |
| Compromise Occurrence Date | `0x00420021` | `CompromiseOccurrenceDate` |  |
| Contact Information | `0x00420022` | `ContactInformation` |  |
| Credential | `0x00420023` | `Credential` |  |
| Credential Type | `0x00420024` | `CredentialType` |  |
| Credential Value | `0x00420025` | `CredentialValue` |  |
| Criticality Indicator | `0x00420026` | `CriticalityIndicator` |  |
| CRT Coefficient | `0x00420027` | `CRTCoefficient` |  |
| Cryptographic Algorithm | `0x00420028` | `CryptographicAlgorithm` |  |
| Cryptographic Domain Parameters | `0x00420029` | `CryptographicDomainParameters` |  |
| Cryptographic Length | `0x0042002A` | `CryptographicLength` |  |
| Cryptographic Parameters | `0x0042002B` | `CryptographicParameters` |  |
| Cryptographic Usage Mask | `0x0042002C` | `CryptographicUsageMask` |  |
| D | `0x0042002E` | `D` |  |
| Deactivation Date | `0x0042002F` | `DeactivationDate` |  |
| Derivation Data | `0x00420030` | `DerivationData` |  |
| Derivation Method | `0x00420031` | `DerivationMethod` |  |
| Derivation Parameters | `0x00420032` | `DerivationParameters` |  |
| Destroy Date | `0x00420033` | `DestroyDate` |  |
| Digest | `0x00420034` | `Digest` |  |
| Digest Value | `0x00420035` | `DigestValue` |  |
| Encryption Key Information | `0x00420036` | `EncryptionKeyInformation` |  |
| G | `0x00420037` | `G` |  |
| Hashing Algorithm | `0x00420038` | `HashingAlgorithm` |  |
| Initial Date | `0x00420039` | `InitialDate` |  |
| Initialization Vector | `0x0042003A` | `InitializationVector` |  |
| Iteration Count | `0x0042003C` | `IterationCount` |  |
| IV/Counter/Nonce | `0x0042003D` | `IVCounterNonce` |  |
| J | `0x0042003E` | `J` |  |
| Key | `0x0042003F` | `Key` |  |
| Key Block | `0x00420040` | `KeyBlock` |  |
| Key Compression Type | `0x00420041` | `KeyCompressionType` |  |
| Key Format Type | `0x00420042` | `KeyFormatType` |  |
| Key Material | `0x00420043` | `KeyMaterial` |  |
| Key Part Identifier | `0x00420044` | `KeyPartIdentifier` |  |
| Key Value | `0x00420045` | `KeyValue` |  |
| Key Wrapping Data | `0x00420046` | `KeyWrappingData` |  |
| Key Wrapping Specification | `0x00420047` | `KeyWrappingSpecification` |  |
| Last Change Date | `0x00420048` | `LastChangeDate` |  |
| Lease Time | `0x00420049` | `LeaseTime` |  |
| Link | `0x0042004A` | `Link` |  |
| Link Type | `0x0042004B` | `LinkType` |  |
| Linked Object Identifier | `0x0042004C` | `LinkedObjectIdentifier` |  |
| MAC/Signature | `0x0042004D` | `MACSignature` |  |
| MAC/Signature Key Information | `0x0042004E` | `MACSignatureKeyInformation` |  |
| Maximum Items | `0x0042004F` | `MaximumItems` |  |
| Maximum Response Size | `0x00420050` | `MaximumResponseSize` |  |
| Modulus | `0x00420052` | `Modulus` |  |
| Name Type | `0x00420054` | `NameType` |  |
| Name Value | `0x00420055` | `NameValue` |  |
| Object Group | `0x00420056` | `ObjectGroup` |  |
| Object Type | `0x00420057` | `ObjectType` |  |
| Offset | `0x00420058` | `Offset` |  |
| Opaque Data Type | `0x00420059` | `OpaqueDataType` |  |
| Opaque Data Value | `0x0042005A` | `OpaqueDataValue` |  |
| Opaque Object | `0x0042005B` | `OpaqueObject` |  |
| Operation | `0x0042005C` | `Operation` |  |
| P | `0x0042005E` | `P` |  |
| Padding Method | `0x0042005F` | `PaddingMethod` |  |
| Prime Exponent P | `0x00420060` | `PrimeExponentP` |  |
| Prime Exponent Q | `0x00420061` | `PrimeExponentQ` |  |
| Prime Field Size | `0x00420062` | `PrimeFieldSize` |  |
| Private Exponent | `0x00420063` | `PrivateExponent` |  |
| Private Key | `0x00420064` | `PrivateKey` |  |
| Private Key Unique Identifier | `0x00420066` | `PrivateKeyUniqueIdentifier` |  |
| Process Start Date | `0x00420067` | `ProcessStartDate` |  |
| Protect Stop Date | `0x00420068` | `ProtectStopDate` |  |
| Protocol Version | `0x00420069` | `ProtocolVersion` |  |
| Protocol Version Major | `0x0042006A` | `ProtocolVersionMajor` |  |
| Protocol Version Minor | `0x0042006B` | `ProtocolVersionMinor` |  |
| Public Exponent | `0x0042006C` | `PublicExponent` |  |
| Public Key | `0x0042006D` | `PublicKey` |  |
| Public Key Unique Identifier | `0x0042006F` | `PublicKeyUniqueIdentifier` |  |
| Put Function | `0x00420070` | `PutFunction` |  |
| Q | `0x00420071` | `Q` |  |
| Q String | `0x00420072` | `QString` |  |
| Qlength | `0x00420073` | `Qlength` |  |
| Query Function | `0x00420074` | `QueryFunction` |  |
| Recommended Curve | `0x00420075` | `RecommendedCurve` |  |
| Replaced Unique Identifier | `0x00420076` | `ReplacedUniqueIdentifier` |  |
| Request Header | `0x00420077` | `RequestHeader` |  |
| Request Message | `0x00420078` | `RequestMessage` |  |
| Request Payload | `0x00420079` | `RequestPayload` |  |
| Response Header | `0x0042007A` | `ResponseHeader` |  |
| Response Message | `0x0042007B` | `ResponseMessage` |  |
| Response Payload | `0x0042007C` | `ResponsePayload` |  |
| Result Message | `0x0042007D` | `ResultMessage` |  |
| Result Reason | `0x0042007E` | `ResultReason` |  |
| Result Status | `0x0042007F` | `ResultStatus` |  |
| Revocation Message | `0x00420080` | `RevocationMessage` |  |
| Revocation Reason | `0x00420081` | `RevocationReason` |  |
| Revocation Reason Code | `0x00420082` | `RevocationReasonCode` |  |
| Key Role Type | `0x00420083` | `KeyRoleType` |  |
| Salt | `0x00420084` | `Salt` |  |
| Secret Data | `0x00420085` | `SecretData` |  |
| Secret Data Type | `0x00420086` | `SecretDataType` |  |
| Server Information | `0x00420088` | `ServerInformation` |  |
| Split Key | `0x00420089` | `SplitKey` |  |
| Split Key Method | `0x0042008A` | `SplitKeyMethod` |  |
| Split Key Parts | `0x0042008B` | `SplitKeyParts` |  |
| Split Key Threshold | `0x0042008C` | `SplitKeyThreshold` |  |
| State | `0x0042008D` | `State` |  |
| Storage Status Mask | `0x0042008E` | `StorageStatusMask` |  |
| Symmetric Key | `0x0042008F` | `SymmetricKey` |  |
| Time Stamp | `0x00420092` | `TimeStamp` |  |
| Unique Batch Item ID | `0x00420093` | `UniqueBatchItemID` |  |
| Unique Identifier | `0x00420094` | `UniqueIdentifier` |  |
| Usage Limits | `0x00420095` | `UsageLimits` |  |
| Usage Limits Count | `0x00420096` | `UsageLimitsCount` |  |
| Usage Limits Total | `0x00420097` | `UsageLimitsTotal` |  |
| Usage Limits Unit | `0x00420098` | `UsageLimitsUnit` |  |
| Username | `0x00420099` | `Username` |  |
| Validity Date | `0x0042009A` | `ValidityDate` |  |
| Validity Indicator | `0x0042009B` | `ValidityIndicator` |  |
| Vendor Identification | `0x0042009D` | `VendorIdentification` |  |
| Wrapping Method | `0x0042009E` | `WrappingMethod` |  |
| X | `0x0042009F` | `X` |  |
| Y | `0x004200A0` | `Y` |  |
| Password | `0x004200A1` | `Password` |  |
| Device Identifier | `0x004200A2` | `DeviceIdentifier` |  |
| Encoding Option | `0x004200A3` | `EncodingOption` |  |
| Fresh | `0x004200A8` | `Fresh` |  |
| Machine Identifier | `0x004200A9` | `MachineIdentifier` |  |
| Media Identifier | `0x004200AA` | `MediaIdentifier` |  |
| Network Identifier | `0x004200AB` | `NetworkIdentifier` |  |
| Object Group Member | `0x004200AC` | `ObjectGroupMember` |  |
| Certificate Length | `0x004200AD` | `CertificateLength` |  |
| Digital Signature Algorithm | `0x004200AE` | `DigitalSignatureAlgorithm` |  |
| Certificate Serial Number | `0x004200AF` | `CertificateSerialNumber` |  |
| Device Serial Number | `0x004200B0` | `DeviceSerialNumber` |  |
| Issuer Alternative Name | `0x004200B1` | `IssuerAlternativeName` |  |
| Issuer Distinguished Name | `0x004200B2` | `IssuerDistinguishedName` |  |
| Subject Alternative Name | `0x004200B3` | `SubjectAlternativeName` |  |
| Subject Distinguished Name | `0x004200B4` | `SubjectDistinguishedName` |  |
| X.509 Certificate Identifier | `0x004200B5` | `X_509CertificateIdentifier` |  |
| X.509 Certificate Issuer | `0x004200B6` | `X_509CertificateIssuer` |  |
| X.509 Certificate Subject | `0x004200B7` | `X_509CertificateSubject` |  |
| Key Value Location | `0x004200B8` | `KeyValueLocation` |  |
| Key Value Location Value | `0x004200B9` | `KeyValueLocationValue` |  |
| Key Value Location Type | `0x004200BA` | `KeyValueLocationType` |  |
| Key Value Present | `0x004200BB` | `KeyValuePresent` |  |
| Original Creation Date | `0x004200BC` | `OriginalCreationDate` |  |
| PGP Key | `0x004200BD` | `PGPKey` |  |
| PGP Key Version | `0x004200BE` | `PGPKeyVersion` |  |
| Alternative Name | `0x004200BF` | `AlternativeName` |  |
| Alternative Name Value | `0x004200C0` | `AlternativeNameValue` |  |
| Alternative Name Type | `0x004200C1` | `AlternativeNameType` |  |
| Data | `0x004200C2` | `Data` |  |
| Signature Data | `0x004200C3` | `SignatureData` |  |
| Data Length | `0x004200C4` | `DataLength` |  |
| Random IV | `0x004200C5` | `RandomIV` |  |
| MAC Data | `0x004200C6` | `MACData` |  |
| Attestation Type | `0x004200C7` | `AttestationType` |  |
| Nonce | `0x004200C8` | `Nonce` |  |
| Nonce ID | `0x004200C9` | `NonceID` |  |
| Nonce Value | `0x004200CA` | `NonceValue` |  |
| Attestation Measurement | `0x004200CB` | `AttestationMeasurement` |  |
| Attestation Assertion | `0x004200CC` | `AttestationAssertion` |  |
| IV Length | `0x004200CD` | `IVLength` |  |
| Tag Length | `0x004200CE` | `TagLength` |  |
| Fixed Field Length | `0x004200CF` | `FixedFieldLength` |  |
| Counter Length | `0x004200D0` | `CounterLength` |  |
| Initial Counter Value | `0x004200D1` | `InitialCounterValue` |  |
| Invocation Field Length | `0x004200D2` | `InvocationFieldLength` |  |
| Attestation Capable Indicator | `0x004200D3` | `AttestationCapableIndicator` |  |
| Offset Items | `0x004200D4` | `OffsetItems` |  |
| Located Items | `0x004200D5` | `LocatedItems` |  |
| Correlation Value | `0x004200D6` | `CorrelationValue` |  |
| Init Indicator | `0x004200D7` | `InitIndicator` |  |
| Final Indicator | `0x004200D8` | `FinalIndicator` |  |
| RNG Parameters | `0x004200D9` | `RNGParameters` |  |
| RNG Algorithm | `0x004200DA` | `RNGAlgorithm` |  |
| DRBG Algorithm | `0x004200DB` | `DRBGAlgorithm` |  |
| FIPS186 Variation | `0x004200DC` | `FIPS186Variation` |  |
| Prediction Resistance | `0x004200DD` | `PredictionResistance` |  |
| Random Number Generator | `0x004200DE` | `RandomNumberGenerator` |  |
| Validation Information | `0x004200DF` | `ValidationInformation` |  |
| Validation Authority Type | `0x004200E0` | `ValidationAuthorityType` |  |
| Validation Authority Country | `0x004200E1` | `ValidationAuthorityCountry` |  |
| Validation Authority URI | `0x004200E2` | `ValidationAuthorityURI` |  |
| Validation Version Major | `0x004200E3` | `ValidationVersionMajor` |  |
| Validation Version Minor | `0x004200E4` | `ValidationVersionMinor` |  |
| Validation Type | `0x004200E5` | `ValidationType` |  |
| Validation Level | `0x004200E6` | `ValidationLevel` |  |
| Validation Certificate Identifier | `0x004200E7` | `ValidationCertificateIdentifier` |  |
| Validation Certificate URI | `0x004200E8` | `ValidationCertificateURI` |  |
| Validation Vendor URI | `0x004200E9` | `ValidationVendorURI` |  |
| Validation Profile | `0x004200EA` | `ValidationProfile` |  |
| Profile Information | `0x004200EB` | `ProfileInformation` |  |
| Profile Name | `0x004200EC` | `ProfileName` |  |
| Server URI | `0x004200ED` | `ServerURI` |  |
| Server Port | `0x004200EE` | `ServerPort` |  |
| Streaming Capability | `0x004200EF` | `StreamingCapability` |  |
| Asynchronous Capability | `0x004200F0` | `AsynchronousCapability` |  |
| Attestation Capability | `0x004200F1` | `AttestationCapability` |  |
| Unwrap Mode | `0x004200F2` | `UnwrapMode` |  |
| Destroy Action | `0x004200F3` | `DestroyAction` |  |
| Shredding Algorithm | `0x004200F4` | `ShreddingAlgorithm` |  |
| RNG Mode | `0x004200F5` | `RNGMode` |  |
| Client Registration Method | `0x004200F6` | `ClientRegistrationMethod` |  |
| Capability Information | `0x004200F7` | `CapabilityInformation` |  |
| Key Wrap Type | `0x004200F8` | `KeyWrapType` |  |
| Batch Undo Capability | `0x004200F9` | `BatchUndoCapability` |  |
| Batch Continue Capability | `0x004200FA` | `BatchContinueCapability` |  |
| PKCS#12 Friendly Name | `0x004200FB` | `PKCS_12FriendlyName` |  |
| Description | `0x004200FC` | `Description` |  |
| Comment | `0x004200FD` | `Comment` |  |
| Authenticated Encryption Additional Data | `0x004200FE` | `AuthenticatedEncryptionAdditionalData` |  |
| Authenticated Encryption Tag | `0x004200FF` | `AuthenticatedEncryptionTag` |  |
| Salt Length | `0x00420100` | `SaltLength` |  |
| Mask Generator | `0x00420101` | `MaskGenerator` |  |
| Mask Generator Hashing Algorithm | `0x00420102` | `MaskGeneratorHashingAlgorithm` |  |
| P Source | `0x00420103` | `PSource` |  |
| Trailer Field | `0x00420104` | `TrailerField` |  |
| Client Correlation Value | `0x00420105` | `ClientCorrelationValue` |  |
| Server Correlation Value | `0x00420106` | `ServerCorrelationValue` |  |
| Digested Data | `0x00420107` | `DigestedData` |  |
| Certificate Subject CN | `0x00420108` | `CertificateSubjectCN` |  |
| Certificate Subject O | `0x00420109` | `CertificateSubjectO` |  |
| Certificate Subject OU | `0x0042010A` | `CertificateSubjectOU` |  |
| Certificate Subject Email | `0x0042010B` | `CertificateSubjectEmail` |  |
| Certificate Subject C | `0x0042010C` | `CertificateSubjectC` |  |
| Certificate Subject ST | `0x0042010D` | `CertificateSubjectST` |  |
| Certificate Subject L | `0x0042010E` | `CertificateSubjectL` |  |
| Certificate Subject UID | `0x0042010F` | `CertificateSubjectUID` |  |
| Certificate Subject Serial Number | `0x00420110` | `CertificateSubjectSerialNumber` |  |
| Certificate Subject Title | `0x00420111` | `CertificateSubjectTitle` |  |
| Certificate Subject DC | `0x00420112` | `CertificateSubjectDC` |  |
| Certificate Subject DN Qualifier | `0x00420113` | `CertificateSubjectDNQualifier` |  |
| Certificate Issuer CN | `0x00420114` | `CertificateIssuerCN` |  |
| Certificate Issuer O | `0x00420115` | `CertificateIssuerO` |  |
| Certificate Issuer OU | `0x00420116` | `CertificateIssuerOU` |  |
| Certificate Issuer Email | `0x00420117` | `CertificateIssuerEmail` |  |
| Certificate Issuer C | `0x00420118` | `CertificateIssuerC` |  |
| Certificate Issuer ST | `0x00420119` | `CertificateIssuerST` |  |
| Certificate Issuer L | `0x0042011A` | `CertificateIssuerL` |  |
| Certificate Issuer UID | `0x0042011B` | `CertificateIssuerUID` |  |
| Certificate Issuer Serial Number | `0x0042011C` | `CertificateIssuerSerialNumber` |  |
| Certificate Issuer Title | `0x0042011D` | `CertificateIssuerTitle` |  |
| Certificate Issuer DC | `0x0042011E` | `CertificateIssuerDC` |  |
| Certificate Issuer DN Qualifier | `0x0042011F` | `CertificateIssuerDNQualifier` |  |
| Sensitive | `0x00420120` | `Sensitive` |  |
| Always Sensitive | `0x00420121` | `AlwaysSensitive` |  |
| Extractable | `0x00420122` | `Extractable` |  |
| Never Extractable | `0x00420123` | `NeverExtractable` |  |
| Replace Existing | `0x00420124` | `ReplaceExisting` |  |
| Attributes | `0x00420125` | `Attributes` |  |
| Common Attributes | `0x00420126` | `CommonAttributes` |  |
| Private Key Attributes | `0x00420127` | `PrivateKeyAttributes` |  |
| Public Key Attributes | `0x00420128` | `PublicKeyAttributes` |  |
| Server Name | `0x0042012D` | `ServerName` |  |
| Server Serial Number | `0x0042012E` | `ServerSerialNumber` |  |
| Server Version | `0x0042012F` | `ServerVersion` |  |
| Server Load | `0x00420130` | `ServerLoad` |  |
| Product Name | `0x00420131` | `ProductName` |  |
| Build Level | `0x00420132` | `BuildLevel` |  |
| Build Date | `0x00420133` | `BuildDate` |  |
| Cluster Info | `0x00420134` | `ClusterInfo` |  |
| Alternate Failover Endpoints | `0x00420135` | `AlternateFailoverEndpoints` |  |
| Short Unique Identifier | `0x00420136` | `ShortUniqueIdentifier` |  |
| Tag | `0x00420138` | `Tag` |  |
| Certificate Request Unique Identifier | `0x00420139` | `CertificateRequestUniqueIdentifier` |  |
| NIST Key Type | `0x0042013A` | `NISTKeyType` |  |
| Attribute Reference | `0x0042013B` | `AttributeReference` |  |
| Current Attribute | `0x0042013C` | `CurrentAttribute` |  |
| New Attribute | `0x0042013D` | `NewAttribute` |  |
| Certificate Request Value | `0x00420140` | `CertificateRequestValue` |  |
| Log Message | `0x00420141` | `LogMessage` |  |
| Profile Version | `0x00420142` | `ProfileVersion` |  |
| Profile Version Major | `0x00420143` | `ProfileVersionMajor` |  |
| Profile Version Minor | `0x00420144` | `ProfileVersionMinor` |  |
| Protection Level | `0x00420145` | `ProtectionLevel` |  |
| Protection Period | `0x00420146` | `ProtectionPeriod` |  |
| Quantum Safe | `0x00420147` | `QuantumSafe` |  |
| Quantum Safe Capability | `0x00420148` | `QuantumSafeCapability` |  |
| Ticket | `0x00420149` | `Ticket` |  |
| Ticket Type | `0x0042014A` | `TicketType` |  |
| Ticket Value | `0x0042014B` | `TicketValue` |  |
| Request Count | `0x0042014C` | `RequestCount` |  |
| Rights | `0x0042014D` | `Rights` |  |
| Objects | `0x0042014E` | `Objects` |  |
| Operations | `0x0042014F` | `Operations` |  |
| Right | `0x00420150` | `Right` |  |
| Endpoint Role | `0x00420151` | `EndpointRole` |  |
| Defaults Information | `0x00420152` | `DefaultsInformation` |  |
| Object Defaults | `0x00420153` | `ObjectDefaults` |  |
| Ephemeral | `0x00420154` | `Ephemeral` |  |
| Server Hashed Password | `0x00420155` | `ServerHashedPassword` |  |
| One Time Password | `0x00420156` | `OneTimePassword` |  |
| Hashed Password | `0x00420157` | `HashedPassword` |  |
| Adjustment Type | `0x00420158` | `AdjustmentType` |  |
| PKCS#11 Interface | `0x00420159` | `PKCS_11Interface` |  |
| PKCS#11 Function | `0x0042015A` | `PKCS_11Function` |  |
| PKCS#11 Input Parameters | `0x0042015B` | `PKCS_11InputParameters` |  |
| PKCS#11 Output Parameters | `0x0042015C` | `PKCS_11OutputParameters` |  |
| PKCS#11 Return Code | `0x0042015D` | `PKCS_11ReturnCode` |  |
| Protection Storage Mask | `0x0042015E` | `ProtectionStorageMask` |  |
| Protection Storage Masks | `0x0042015F` | `ProtectionStorageMasks` |  |
| Interop Function | `0x00420160` | `InteropFunction` |  |
| Interop Identifier | `0x00420161` | `InteropIdentifier` |  |
| Adjustment Value | `0x00420162` | `AdjustmentValue` |  |
| Common Protection Storage Masks | `0x00420163` | `CommonProtectionStorageMasks` |  |
| Private Protection Storage Masks | `0x00420164` | `PrivateProtectionStorageMasks` |  |
| Public Protection Storage Masks | `0x00420165` | `PublicProtectionStorageMasks` |  |
| Object Groups | `0x00420166` | `ObjectGroups` |  |
| Object Types | `0x00420167` | `ObjectTypes` |  |
| Constraints | `0x00420168` | `Constraints` |  |
| Constraint | `0x00420169` | `Constraint` |  |

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

[TTLV Encoding](../ttlv-encoding.md) · [Item Data Types](../../references/item-data-types.md) · [Message Structure](../../messages/message-structure.md)
