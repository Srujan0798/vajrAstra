# mcp_detailed (converted from mcp_detailed.jsonl - all records, fields verbatim)

## Record 1 (from mcp_detailed.jsonl)
- **source_url**: https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle
- **date**: 2026-06-18
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  MCP Initialization: client sends initialize request with protocolVersion, capabilities (roots, sampling, etc.), clientInfo. Server responds with protocolVersion, capabilities, serverInfo, instructions. Client sends initialized notification. Capability negotiation: roots (file system access), sampling (LLM sampling), tools, resources, prompts. Version agreement required before operation.
- **decision_it_changes**: W6 architecture: MCP initialization for OCR engine tool server capabilities
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 2 (from mcp_detailed.jsonl)
- **source_url**: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization
- **date**: 2026-03-26
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  MCP OAuth 2.1 flow: 1) Client discovers auth server via Authorization Server Metadata (RFC8414) at /.well-known/oauth-authorization-server. 2) Dynamic Client Registration (RFC7591) for client credentials. 3) Authorization code grant or client credentials grant. 4) Access token used as Bearer token for MCP requests. Token introspection for validation. Scopes control resource access. Optional for implementations.
- **decision_it_changes**: W6 architecture: OAuth 2.1 flow for OCR validation tool authentication
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 3 (from mcp_detailed.jsonl)
- **source_url**: https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/api/registry-authorization.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  Registry as OAuth 2.1 Resource Server: validates access tokens same as MCP servers. Clients reuse MCP auth implementation. Scopes: mcp-registry:read (list/read metadata), mcp-registry:write (publish/update/delete). User-level authorization for specific resources. Official registry: public read, custom JWT for publish (legacy). Namespace ownership via GitHub/DNS verification.
- **decision_it_changes**: W6 architecture: registry auth for OCR engine tool publishing/discovery
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 4 (from mcp_detailed.jsonl)
- **source_url**: https://modelcontextprotocol.io/registry/about
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  MCP server.json metadata: name (io.github.user/server-name), version, description, repository, homepage, license, keywords. Packages: npm (package name), pypi, docker (image), binary (url, checksum). Execution: command, args, env. Capabilities: tools, resources, prompts. Requirements: node, python, docker versions. Repository: type (github), url. README, CHANGELOG links. Standardized for discovery.
- **decision_it_changes**: W6 architecture: server.json for OCR engine tool metadata
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 5 (from mcp_detailed.jsonl)
- **source_url**: https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index
- **date**: 2026-07-28
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  MCP Authorization 2026: OAuth Client ID Metadata Documents (draft-ietf-oauth-client-id-metadata-document-00) for client configuration. Updated Authorization Server Discovery. Roles: protected MCP server (resource server), MCP client, authorization server. OAuth 2.1 with security measures for confidential/public clients. Dynamic Client Registration SHOULD be supported. Server Metadata MUST be implemented.
- **decision_it_changes**: W6 architecture: updated MCP auth for OCR validation tool security
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 6 (from mcp_detailed.jsonl)
- **source_url**: https://modelcontextprotocol.info/tools/registry
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 3
- **extraction**:

  MCP Registry API: REST endpoints for server discovery, metadata retrieval, publishing. Search by name, capability, keyword. Namespace management: GitHub (io.github.username/*), DNS verification. Authentication: GitHub OAuth for namespace ownership. Server.json format standardized. Package registries (npm, PyPI, Docker) host code; MCP Registry hosts metadata pointing to packages. No private server support.
- **decision_it_changes**: W6 architecture: registry API for automated OCR tool discovery/install
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 7 (from mcp_detailed.jsonl)
- **source_url**: https://registry.modelcontextprotocol.io/
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Official MCP Registry UI: search, filter latest versions, browse servers. API base URLs: production (registry.modelcontextprotocol.io), staging, local. Built by MCP contributors (Anthropic, GitHub, PulseMCP, Microsoft). Server entries with name, description, capabilities, installation info. Open for community contributions.
- **decision_it_changes**: W6 architecture: registry browsing for OCR validation tool discovery
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline
