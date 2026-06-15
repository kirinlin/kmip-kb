---
title: Application Specific Information
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.0", "1.1", "1.2", "1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.18"
status: reviewed
related: ["object-group"]
keywords: ["Application Specific Information", "Application Namespace", "Application Data", "server-generated data", "namespaces", "420004", "ApplicationSpecificInformation"]
tag_hex: "420004"
xml_text: "ApplicationSpecificInformation"
---

# Application Specific Information

## Overview

The Application Specific Information attribute is a multi-instance attribute that allows applications to attach arbitrary key-value pairs — an Application Namespace and Application Data — to managed objects. It is designed for application-layer tagging that falls outside the scope of standardised KMIP attributes.

## Guidance

Well-known namespace values include identifiers for email (SMIME), transport security (TLS, HTTPS), network security (IPSEC), key distribution (PGP), storage volumes, file naming, and a family of tape-specific namespaces (LTO4, LTO5, LTO6, LIBRARY-LTO, and related variants). Clients choose a namespace that identifies their application context, then use the Application Data field to store the application-specific identifier (such as an email address, domain name, volume ID, or file name).

KMIP optionally allows clients to request server-generated Application Data by omitting the Application Data field from a Set Attribute or Add Attribute request while specifying a recognised namespace. The server generates the data if the namespace is known and supported; if not, it returns an "Application Namespace Not Supported" error.

## Implementation Notes

Application Specific Information is a multi-instance attribute: a single object can have multiple instances, each with a different namespace and data pair. This allows the same key to be tagged by multiple applications simultaneously. Clients should use well-known namespace names for maximum interoperability. The LIBRARY-LTO4 and related tape namespaces are particularly important for the tape library key interoperability use case described in section 4.3.

## Related Concepts

See [Interoperable Key Naming for Tape](interoperable-key-naming-for-tape.md) for the tape library namespace usage.
