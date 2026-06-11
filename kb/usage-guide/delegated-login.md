---
title: Delegated Login
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.3", "1.4", "2.0", "2.1"]
source_section: "ug-3.43"
status: reviewed
related: ["authentication", "login-and-logout"]
keywords: ["Delegated Login", "delegation", "login ticket", "subset of rights", "time limit", "request count"]
---

# Delegated Login

## Overview

The Delegated Login operation allows a client to delegate a subset of its access rights to another party, producing a login ticket. The ticket can be time-limited, usage-count-limited, restricted to specific operations, or restricted to specific objects.

## Guidance

A client with broad access rights can use Delegated Login to issue a ticket granting narrower rights to another client or process. The ticket specifies the set of permitted operations and the set of objects to which those operations may be applied. A time limit and/or a maximum request count can be set to ensure the delegation expires automatically.

## Implementation Notes

Delegated Login is useful in multi-tier architectures where a high-privilege service needs to grant limited access to a lower-privilege worker without sharing its full credentials. The resulting ticket replaces the need for the worker to have its own full authentication context. Servers that support Delegated Login may impose their own constraints on the scope of delegable rights.

## Related Concepts

See [Authentication](authentication.md) and [Login and Logout](login-and-logout.md).
