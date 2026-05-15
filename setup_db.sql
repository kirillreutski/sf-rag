-- Template: do not run directly, use setup_guide.py instead.
-- Placeholders {GUIDE} and {TABLE} are replaced by setup_guide.py.

CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS {TABLE} (
    id          UUID PRIMARY KEY,
    source      TEXT        NOT NULL,
    breadcrumb  TEXT        NOT NULL,
    heading     TEXT        NOT NULL,
    text        TEXT        NOT NULL,
    token_count INT         NOT NULL,
    embedding   vector(768) NOT NULL
);

CREATE INDEX IF NOT EXISTS {TABLE}_embedding_idx
    ON {TABLE} USING hnsw (embedding vector_cosine_ops)
    WITH (m = 16, ef_construction = 64);

CREATE OR REPLACE FUNCTION search_{GUIDE}(
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
        id, source, breadcrumb, heading, text,
        1 - (embedding <=> query_embedding) AS similarity
    FROM  {TABLE}
    WHERE 1 - (embedding <=> query_embedding) > min_similarity
    ORDER BY embedding <=> query_embedding
    LIMIT match_count;
$$;
