import os
import sys


from pathlib import Path

import duckdb

from dotenv import load_dotenv


def get_db_path():
    """Load the database path from .env file."""
    # Load .env from the project root
    project_root = Path(__file__).parent.parent
    env_path = project_root / ".env"
    
    if not env_path.exists():
        print(f"Error: .env file not found at {env_path}")
        sys.exit(1)
    
    load_dotenv(env_path)
    
    db_path = os.getenv("SILVER_DUCKDB_PATH")
    if not db_path:
        print("Error: SILVER_DUCKDB_PATH not found in .env")
        sys.exit(1)
    
    # Convert relative path to absolute
    if not os.path.isabs(db_path):
        db_path = project_root / db_path
    else:
        db_path = Path(db_path)
    
    if not db_path.exists():
        print(f"Error: Database file not found at {db_path}")
        sys.exit(1)
    
    return db_path


def get_all_tables(conn):
    """Get list of all tables in the database."""
    query = """
    SELECT table_schema, table_name 
    FROM information_schema.tables 
    WHERE table_schema NOT IN ('information_schema', 'pg_catalog')
    ORDER BY table_schema, table_name
    """
    return conn.execute(query).fetchall()


def get_table_schema(conn, schema_name, table_name):
    """Get the schema information for a specific table."""
    query = f"""
    SELECT 
        column_name,
        data_type,
        is_nullable,
        column_default
    FROM information_schema.columns
    WHERE table_schema = '{schema_name}' AND table_name = '{table_name}'
    ORDER BY ordinal_position
    """
    return conn.execute(query).fetchall()


def get_table_sample(conn, schema_name, table_name, n=10):
    """Get a random sample of n rows from a table."""
    full_table_name = f'"{schema_name}"."{table_name}"' if schema_name else f'"{table_name}"'
    
    # First, get the count
    count_query = f"SELECT COUNT(*) FROM {full_table_name}"
    count = conn.execute(count_query).fetchone()[0]
    
    if count == 0:
        return None, []
    
    # Get sample
    sample_query = f"SELECT * FROM {full_table_name} USING SAMPLE {min(n, count)} ROWS"
    result = conn.execute(sample_query)
    
    columns = [desc[0] for desc in result.description]
    rows = result.fetchall()
    
    return columns, rows


def escape_markdown(value):
    """Escape special markdown characters in table cells."""
    if value is None:
        return "NULL"
    
    value_str = str(value)
    
    # Escape pipe characters
    value_str = value_str.replace("|", "\\|")
    
    # Replace newlines with spaces
    value_str = value_str.replace("\n", " ")
    
    # Truncate very long strings
    if len(value_str) > 100:
        value_str = value_str[:97] + "..."
    
    return value_str


def generate_schema_doc(conn, output_path):
    """Generate markdown documentation for all table schemas."""
    tables = get_all_tables(conn)
    
    with open(output_path, "w") as f:
        f.write("# Database Schema Documentation\n\n")
        f.write(f"Total tables: {len(tables)}\n\n")
        f.write("---\n\n")
        
        for schema_name, table_name in tables:
            full_name = f"{schema_name}.{table_name}" if schema_name else table_name
            f.write(f"## {full_name}\n\n")
            
            schema = get_table_schema(conn, schema_name, table_name)
            
            if schema:
                f.write("| Column Name | Data Type | Nullable | Default |\n")
                f.write("|-------------|-----------|----------|----------|\n")
                
                for col_name, data_type, is_nullable, col_default in schema:
                    nullable = "YES" if is_nullable == "YES" else "NO"
                    default = escape_markdown(col_default) if col_default else "-"
                    f.write(f"| {col_name} | {data_type} | {nullable} | {default} |\n")
            else:
                f.write("*No schema information available*\n")
            
            f.write("\n---\n\n")
    
    print(f"Schema documentation saved to: {output_path}")


def generate_samples_doc(conn, output_path, sample_size=10):
    """Generate markdown documentation with sample data from each table."""
    tables = get_all_tables(conn)
    
    with open(output_path, "w") as f:
        f.write("# Database Sample Data\n\n")
        f.write(f"Showing up to {sample_size} random rows from each table.\n\n")
        f.write("---\n\n")
        
        for schema_name, table_name in tables:
            full_name = f"{schema_name}.{table_name}" if schema_name else table_name
            f.write(f"## {full_name}\n\n")
            
            columns, rows = get_table_sample(conn, schema_name, table_name, sample_size)
            
            if not rows:
                f.write("*Table is empty*\n\n")
            elif columns:
                # Write table header
                f.write("| " + " | ".join(columns) + " |\n")
                f.write("|" + "|".join(["-" * (len(col) + 2) for col in columns]) + "|\n")
                
                # Write rows
                for row in rows:
                    escaped_row = [escape_markdown(value) for value in row]
                    f.write("| " + " | ".join(escaped_row) + " |\n")
            else:
                f.write("*No data available*\n")
            
            f.write("\n---\n\n")
    
    print(f"Sample data documentation saved to: {output_path}")


def main():
    """Main function to generate database documentation."""
    print("Database Documentation Generator")
    print("=" * 50)
    
    # Get database path
    db_path = get_db_path()
    print(f"Using database: {db_path}")
    
    # Connect to database
    print("Connecting to database...")
    conn = duckdb.connect(str(db_path), read_only=True)
    
    try:
        # Get output directory
        output_dir = Path(__file__).parent
        
        # Generate schema documentation
        print("\nGenerating schema documentation...")
        schema_doc_path = output_dir / "db_schema.md"
        generate_schema_doc(conn, schema_doc_path)
        
        # Generate samples documentation
        print("\nGenerating sample data documentation...")
        samples_doc_path = output_dir / "db_samples.md"
        generate_samples_doc(conn, samples_doc_path)
        
        print("\n" + "=" * 50)
        print("Documentation generated successfully!")
        print(f"\nOutput files:")
        print(f"  - {schema_doc_path}")
        print(f"  - {samples_doc_path}")
        
    finally:
        conn.close()


if __name__ == "__main__":
    main()
