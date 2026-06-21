---
title: Client Registration Method Enumeration
category: enumerations
spec_version: "2.1"
spec_versions: ["1.2","1.3","1.4","2.0","2.1"]
source_section: "11.10"
status: reviewed
related: ["query", "query-function-enumeration", "login", "credential-type-enumeration"]
keywords: ["client registration", "registration method", "provisioning", "client identity", "server pre-generated", "4200F6", "ClientRegistrationMethod"]
tag_hex: "4200F6"
xml_text: "ClientRegistrationMethod"
tag_type: "Enumeration"
---

# Client Registration Method Enumeration

## Overview

The Client Registration Method enumeration describes how a KMIP client identity is established with the server. In enterprise deployments, clients do not always self-register; sometimes credentials are pre-provisioned by administrators, sometimes generated on demand by the server, and sometimes brought by the client itself. Knowing the registration method helps the server apply the appropriate policy and helps administrators understand the provenance of client identities. This enumeration is surfaced in Query responses when a client asks about the server's capabilities and supported registration workflows.

## Fields & Structure

| Name | Value | XML Text | Description |
|---|---|---|---|
| Unspecified | `00000001` | `Unspecified` |  |
| Server Pre-Generated | `00000002` | `ServerPreGenerated` |  |
| Server On-Demand | `00000003` | `ServerOnDemand` |  |
| Client Generated | `00000004` | `ClientGenerated` |  |
| Client Registered | `00000005` | `ClientRegistered` |  |

- **Unspecified**: The registration method is not declared or is not applicable. Acts as a catch-all for deployments that do not distinguish among methods.
- **Server Pre-Generated**: The server generates the client's credentials (certificates, tokens, or other identity material) ahead of time and distributes them through an out-of-band channel such as a management console or secure enrollment ceremony.
- **Server On-Demand**: The server generates and issues credentials in response to an enrollment request at connection time. Similar to SCEP or EST enrollment flows where the client triggers credential issuance.
- **Client Generated**: The client generates its own credentials (typically a key pair and certificate signing request) and presents them to the server for enrollment. The server validates and trusts the credentials after verifying the request.
- **Client Registered**: The client arrives with pre-existing credentials issued by a trusted third party (such as a CA certificate chain) and registers those credentials with the server without the server needing to issue anything new.

## Examples

A storage array that ships with a factory-installed device certificate uses **Client Registered** — it presents its manufacturer-issued certificate to the KMIP server at first connection. A software client provisioned by a deployment script that generates a key pair and submits a CSR to the server uses the **Server On-Demand** flow.

## Related

- [Query operation](../operations/query.md) — returns server capabilities including supported registration methods
- [Query Function Enumeration](query-function-enumeration.md) — controls which sections of information a Query returns
- [Credential Type Enumeration](credential-type-enumeration.md) — the type of credential used after registration
