---
title: Login and Logout
category: usage-guide
spec_version: "2.1"
spec_versions: ["1.4", "2.0", "2.1"]
source_section: "ug-3.47"
status: reviewed
related: ["authentication", "delegated-login"]
keywords: ["Login", "Logout", "login ticket", "authentication caching", "time limit", "request count"]
---

# Login and Logout

## Overview

Login and Logout exist to cache the outcome of a completed authentication exchange, spreading its cost across multiple subsequent requests without requiring re-authentication for each one. Login returns a login ticket that the client presents for subsequent requests without re-authenticating; Logout invalidates the ticket.

## Guidance

Login takes an optional time limit (the maximum duration the ticket is valid) and/or a request usage count (the maximum number of requests the ticket covers). The server determines the actual validity of the ticket within these client-specified constraints based on its own policy.

This mechanism is particularly useful in environments where full authentication (such as hardware token or certificate verification) is expensive per-request and the client wishes to amortise that cost across a session.

## Implementation Notes

Login/Logout tickets are distinct from TLS sessions: the TLS session provides transport-level continuity, while the Login ticket provides protocol-level authentication continuity. Deployments that use short-lived TLS connections (connection-per-request) can still benefit from Login tickets if the server maintains ticket state between connections. Tickets should be securely stored at the client and transmitted only over authenticated TLS channels.

## Related Concepts

See [Authentication](authentication.md) and [Delegated Login](delegated-login.md).
