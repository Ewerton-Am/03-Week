import mysql.connector

def my_company():
    # Conexão com o banco
    conection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2t2o3n6Ok15ago1996.",
        database="my_company"
    )

    point = conection.cursor()

    # Create table if not exist
    point.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            position VARCHAR(255),
            name VARCHAR(255)
        )
    """)

    # Insert data only if empty
    point.execute("SELECT COUNT(*) FROM employees")
    if point.fetchone()[0] == 0:
        point.execute("""
            INSERT INTO employees (position, name) VALUES
            ('CEO', 'Mariana Souza'),
            ('Diretor Financeiro', 'Carlos Almeida'),
            ('Gerente de RH', 'Fernanda Lima'),
            ('Coordenador de Marketing', 'Lucas Ferreira'),
            ('Analista de Sistemas', 'Patrícia Gomes'),
            ('Desenvolvedor Back-End', 'Rafael Oliveira'),
            ('Desenvolvedor Front-End', 'Juliana Costa'),
            ('Designer Gráfico', 'Bruno Martins'),
            ('Assistente Administrativo', 'Larissa Rocha'),
            ('Estagiário', 'Thiago Mendes')
        """)
        conection.commit()

    point.close()
    return conection

