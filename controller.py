import time
import sqlite3 as sql

def createDB():
    conn = sql.connect("autoconocimiento.db")
    print ("Base de Datos de autoconocimiento creada")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("autoconocimiento.db")
    cursor = conn.cursor()
    cursor.execute
    ("""
    CREATE TABLE resource_totals (
    total_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_id INTEGER,
    total_budget DECIMAL(10,2),
    total_time_days INTEGER,
    resources_allocated TEXT,
    last_calculated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (plan_id) REFERENCES strategic_plan(plan_id)
    ;)
    """)
    print("Tabla creada")
    conn.commit()
    conn.close()

if __name__== "__main__":
    #createDB()
    createTable()
     </pre>
        </section>
        <section>
            <h2>4) Ejemplo de Tabla para la Base de Datos</h2>
            <p>La estructura de la tabla <code>respuestas</code> queda de la siguiente manera:</p>
            <table>
                <thead>
                    <tr>
                        <th>Campo</th>
                        <th>Tipo</th>
                        <th>Descripción</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>id_respuesta</td>
                        <td>INTEGER</td>
                        <td>Identificador único de cada respuesta (clave primaria).</td>
                    </tr>
                    <tr>
                        <td>id_pregunta</td>
                        <td>INTEGER</td>
                        <td>Identificador de la pregunta relacionada (clave foránea).</td>
                    </tr>
                    <tr>
                        <td>respuesta_usuario</td>
                        <td>TEXT</td>
                        <td>Respuesta del usuario ('A' o 'B').</td>
                    </tr>
                </tbody>
            </table>
        </section>
        <section>
            <h2>5) Imagenes Relacionadas</h2>
            <p>*Imagenes representativas del contenido:</p>
            <img src="ig.jpg" alt="Imagen relacionada con ingeniería de software">
        
             <img src="ag.jpg" alt="Imagen relacionada con ingeniería de software">
               <img src="og.png" alt="Imagen relacionada con ingeniería de software">
        </section>
    </div>
</body>
</html>




