---
title: Mandatory Quantum Safe Test Cases KMIP v2.0
category: profile
spec_version: "2.0"
spec_versions: ["2.0"]
source_section: "prof-5.17"
status: reviewed
related: ["quantum-safe-profiles", "quantum-safe-client", "quantum-safe-server"]
keywords: ["quantum safe", "test cases", "QS-M", "mandatory test", "conformance", "Protection Period", "Protection Level", "PQC"]
---

# Mandatory Quantum Safe Test Cases KMIP v2.0

## Overview

The Mandatory Quantum Safe Test Cases for KMIP v2.0 (§5.17 of [KMIP-Prof]) define the minimum interoperability test scenarios that a [Quantum Safe Client](quantum-safe-client.md) and [Quantum Safe Server](quantum-safe-server.md) must pass to claim conformance with the Quantum Safe profile at the KMIP 2.0 protocol version. KMIP v2.1 defines a separate set of test cases in a parallel article.

## Test Case Identifiers

Test case identifiers follow the pattern `QS-M-<n>-20` for mandatory cases and `QS-O-<n>-20` for optional cases, where `20` denotes the KMIP 2.0 version.

## Mandatory Test Cases

**QS-M-1-20** — The client connects to the server over TLS 1.3 and invokes Query to retrieve the server's capabilities. The test verifies that the TLS 1.3 handshake succeeds and that the Query response enumerates the server's supported quantum-safe operations and object types.

**QS-M-2-20** — The client invokes Create, providing `Protection Period` and `Protection Level` as attributes in the request. The server must generate a symmetric key using a quantum-safe algorithm appropriate to the specified protection parameters and return a `Unique Identifier`. The test verifies that the resulting key object carries the `Quantum Safe` attribute set to True and that the algorithm selection is consistent with the requested protection parameters.

## Permitted Test Case Variations

The following values may legitimately differ between implementations without affecting conformance:
- `UniqueIdentifier` and `UniqueBatchItemIdentifier` (server-generated values)
- `TimeStamp` and datetime attributes (`InitialDate`, `LastChangeDate`, etc.) when not fixed in the request
- `Cryptographic Algorithm` and `Cryptographic Length` selected by the server, provided they are from the approved quantum-safe list and satisfy the stated protection parameters
- Server-generated key material

## Implications for Implementers

- Both mandatory test cases must pass for a client or server to claim the Quantum Safe profile at KMIP 2.0. The test count is deliberately small; future KMIP-Prof versions may add test cases as PQC algorithm availability matures.
- QS-M-1-20 is effectively a connectivity test: if TLS 1.3 negotiation fails, the test fails before any KMIP message is exchanged.
- QS-M-2-20 requires the server to make an algorithm selection. Servers should document their selection logic so that conformance test validators can verify that the chosen algorithm satisfies the stated `Protection Period` and `Protection Level`.

## Related Concepts

[Quantum Safe Profiles](quantum-safe-profiles.md) ·
[Quantum Safe Client](quantum-safe-client.md) ·
[Quantum Safe Server](quantum-safe-server.md)
