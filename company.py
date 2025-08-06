import mysql.connector
import db

def my_company():
    conection = db.db_connection()

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

