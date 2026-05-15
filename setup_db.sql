-- Run once against your PostgreSQL database.
-- Requires pgvector extension (https://github.com/pgvector/pgvector).

CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS apex_chunks (
    id          UUID PRIMARY KEY,
    source      TEXT        NOT NULL,
    breadcrumb  TEXT        NOT NULL,
    heading     TEXT        NOT NULL,
    text        TEXT        NOT NULL,
    token_count INT         NOT NULL,
    embedding   vector(768) NOT NULL
);

-- HNSW index for fast cosine-similarity search.
-- Tune m / ef_construction after loading data if needed.
CREATE INDEX IF NOT EXISTS apex_chunks_embedding_idx
    ON apex_chunks USING hnsw (embedding vector_cosine_ops)
    WITH (m = 16, ef_construction = 64);

-- Convenience search function called by the MCP server.
CREATE OR REPLACE FUNCTION search_apex_docs(
    query_embedding vector(768),
    match_count     INT   DEFAULT 5,
    min_similarity  FLOAT DEFAULT 0.3
)
RETURNS TABLE (
    id          UUID,
    source      TEXT,
    breadcrumb  TEXT,
    heading     TEXT,
    text        TEXT,
    similarity  FLOAT
)
LANGUAGE sql STABLE
AS $$
    SELECT
        id,
        source,
        breadcrumb,
        heading,
        text,
        1 - (embedding <=> query_embedding) AS similarity
    FROM  apex_chunks
    WHERE 1 - (embedding <=> query_embedding) > min_similarity
    ORDER BY embedding <=> query_embedding
    LIMIT match_count;
$$;
