# mcp_servers (converted from mcp_servers.jsonl - all records, fields verbatim)

## Record 1 (from mcp_servers.jsonl)
- **source_url**: https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle
- **date**: 2026-06-18
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  MCP Lifecycle: 3 phases - Initialization (capability negotiation, protocol version agreement), Operation (normal protocol communication), Shutdown (graceful termination). Client MUST initiate with initialize request. Server responds with initialize response. Client sends initialized notification. Connection closed on disconnect. Rigorous lifecycle ensures proper capability negotiation and state management.
- **decision_it_changes**: W6 architecture: MCP lifecycle for OCR engine tool server connections
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 2 (from mcp_servers.jsonl)
- **source_url**: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization
- **date**: 2026-03-26
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  MCP Authorization: OAuth 2.1 at transport level. Protected MCP server = OAuth 2.1 resource server. MCP client = OAuth 2.1 client. Authorization server issues access tokens. Authorization Server Discovery specifies how server indicates auth server location. Optional for MCP implementations. Dynamic Client Registration (RFC7591) SHOULD be supported. Authorization Server Metadata (RFC8414) MUST be implemented by auth servers and clients.
- **decision_it_changes**: W6 architecture: MCP OAuth 2.1 for secure OCR engine tool access
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 3 (from mcp_servers.jsonl)
- **source_url**: https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/api/registry-authorization.md
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 4
- **extraction**:

  MCP Registry Authorization: Registry acts as OAuth 2.1 Resource Server. MCP clients reuse existing MCP auth implementation. Scopes: mcp-registry:read (list/read server metadata), mcp-registry:write (publish/update/delete servers). User-level authorization controls specific resource access. Official registry public for reading, custom JWT-based auth for publishing (legacy).
- **decision_it_changes**: W6 architecture: MCP registry auth for OCR engine tool discovery
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 4 (from mcp_servers.jsonl)
- **source_url**: https://modelcontextprotocol.io/registry/about
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  MCP Registry: centralized metadata repository for publicly accessible MCP servers. Backed by Anthropic, GitHub, PulseMCP, Microsoft. Single place for server creators to publish metadata. Namespace management via DNS verification. REST API for discovery. Standardized server.json format: unique name (io.github.user/server-name), location (npm package, remote URL), execution instructions (cmd args, env vars), discovery data (description, capabilities). Does not host code - points to npm, PyPI, Docker Hub. Supports open/closed source. No private servers.
- **decision_it_changes**: W6 architecture: MCP registry for OCR engine tool discovery and installation
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 5 (from mcp_servers.jsonl)
- **source_url**: https://registry.modelcontextprotocol.io/
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 3
- **extraction**:

  Official MCP Registry at registry.modelcontextprotocol.io. Discover MCP servers. Search, filter by latest versions. Built in open by MCP contributors. API base URLs: production, staging, local. Server entries with standardized metadata.
- **decision_it_changes**: W6 architecture: registry browsing for OCR validation tool discovery
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 6 (from mcp_servers.jsonl)
- **source_url**: https://modelcontextprotocol.info/tools/registry
- **date**: 2026-09-27
- **status**: PRIMARY
- **relevance**: 4
- **recency**: 5
- **actionability**: 3
- **extraction**:

  MCP Registry as app store for MCP servers. Server entries use server.json: Identity (unique name io.github.user/server-name), Packages (where to download: npm, pypi, docker). Authentication and namespaces: GitHub namespaces (io.github.username/*), verification via GitHub OAuth or DNS. API specification for implementing registries. Official hosted registry at registry.modelcontextprotocol.io.
- **decision_it_changes**: W6 architecture: registry API for automated OCR engine tool installation
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline

## Record 7 (from mcp_servers.jsonl)
- **source_url**: https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index
- **date**: 2026-07-28
- **status**: PRIMARY
- **relevance**: 5
- **recency**: 5
- **actionability**: 5
- **extraction**:

  MCP Authorization 2026-07-28: OAuth 2.1 with OAuth Client ID Metadata Documents (draft-ietf-oauth-client-id-metadata-document-00). Roles: protected MCP server (resource server), MCP client, authorization server. Authorization Server Discovery specifies how server indicates auth server location. Updated from 2025 spec with newer OAuth drafts.
- **decision_it_changes**: W6 architecture: updated MCP auth for OCR validation tool security
- **transfer**: SURVIVES
- **transfer_harness_fact**: 18 Indic langs, weak cells, 200-dpi citizen docs, no paid keys, no training until W6 freeze, offline pipeline
