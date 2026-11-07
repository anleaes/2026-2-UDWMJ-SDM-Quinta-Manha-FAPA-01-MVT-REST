### Convenções de Tipos de Commit (`<tipo>`)

| Tipo       | Descrição                                                                    |
| :--------- | :--------------------------------------------------------------------------- |
| `feat`     | Adição de uma nova funcionalidade ao sistema.                                |
| `fix`      | Correção de um erro ou bug.                                                  |
| `docs`     | Alterações exclusivas na documentação.                                       |
| `style`    | Mudanças de formatação que não afetam a lógica do código.                    |
| `refactor` | Alteração no código que melhora sua estrutura sem alterar seu comportamento. |
| `perf`     | Mudança voltada para melhoria de desempenho.                                 |
| `test`     | Adição de testes ausentes ou correção de testes existentes.                  |
| `build`    | Alterações que afetam o sistema de compilação ou dependências externas.      |
| `ci`       | Mudanças nos arquivos e scripts de integração contínua.                      |
| `chore`    | Tarefas de manutenção rotineiras que não alteram código fonte ou testes.     |
| `revert`   | Reversão de um commit anterior.                                              |


### Convenções de Nomenclatura para Banco de Dados

* **Tabelas e Colunas:** Devem ser escritas em **inglês**, no **singular**, utilizando apenas letras minúsculas e separadas por sublinhado (`snake_case`).

| Regra                 | Padrão                        | Exemplo                     |
| :-------------------- | :---------------------------- | :-------------------------- |
| **Nome da Tabela**    | Singular, inglês, `snake_case`| `vaccination`               |
| **Chave Primária (PK)**| Identificador padrão         | `id`                        |
| **Atributos/Colunas** | Singular, inglês, `snake_case`| `applied_at`, `dose_number` |

---

### Exemplo Prático de Tabela

Baseado na estrutura da entidade `Vacinacao`:

```sql
CREATE TABLE vaccination (
    id INT PRIMARY KEY,
    applied_at TIMESTAMP,
    dose_number INT,
    application_site VARCHAR(100),
    weight_kg FLOAT,
    notes TEXT
);
```

---

### Padronização dos 14 Apps, Models e Colunas

1. **Pessoa (`persons`)**
   - Branch / App: `persons`
   - Classe (Model): `Person`
   - Tabela: `person`
   - Atributos: `name`, `cpf`, `phone`, `email`

2. **Fabricante (`manufacturers`)**
   - Branch / App: `manufacturers`
   - Classe (Model): `Manufacturer`
   - Tabela: `manufacturer`
   - Atributos: `name`, `cnpj`, `country`, `email`

3. **Tutor (`tutors`)**
   - Branch / App: `tutors`
   - Classe (Model): `Tutor` (herda de `Person`)
   - Tabela: `tutor`
   - Atributos: `photo`

4. **Vacina (`vaccines`)**
   - Branch / App: `vaccines`
   - Classe (Model): `Vaccine`
   - Tabela: `vaccine`
   - Atributos: `name`, `description`, `required_doses`, `interval_days`, `price`, `is_active`, `package_insert`
   - Relacionamentos: `manufacturer` (ForeignKey -> `Manufacturer`)

5. **Veterinário (`veterinarians`)**
   - Branch / App: `veterinarians`
   - Classe (Model): `Veterinarian` (herda de `Person`)
   - Tabela: `veterinarian`
   - Atributos: `crmv`, `is_active`

6. **Espécie (`species`)**
   - Branch / App: `species`
   - Classe (Model): `Species`
   - Tabela: `species`
   - Atributos: `name`, `description`, `average_lifespan_years`, `is_active`
   - Relacionamentos: `vaccine` (ManyToManyField -> `Vaccine`)

7. **Animal (`animals`)**
   - Branch / App: `animals`
   - Classe (Model): `Animal`
   - Tabela: `animal`
   - Atributos: `name`, `birth_date`, `sex`, `weight_kg`, `microchip`, `photo`
   - Relacionamentos: `tutor` (ForeignKey -> `Tutor`), `species` (ForeignKey -> `Species`)

8. **Lote (`batches`)**
   - Branch / App: `batches`
   - Classe (Model): `Batch`
   - Tabela: `batch`
   - Atributos: `number`, `fabrication_date`, `expiration_date`, `quantity`
   - Relacionamentos: `vaccine` (ForeignKey -> `Vaccine`)

9. **Medicamento (`medications`)**
   - Branch / App: `medications`
   - Classe (Model): `Medication`
   - Tabela: `medication`
   - Atributos: `name`, `active_ingredient`, `administration_route`, `price`, `is_controlled`
   - Relacionamentos: `manufacturer` (ForeignKey -> `Manufacturer`)

10. **Vacinação (`vaccinations`)**
    - Branch / App: `vaccinations`
    - Classe (Model): `Vaccination`
    - Tabela: `vaccination`
    - Atributos: `applied_at`, `dose_number`, `application_site`, `weight_kg`, `notes`
    - Relacionamentos: `batch` (ForeignKey -> `Batch`)

11. **Receita (`recipes`)**
    - Branch / App: `recipes`
    - Classe (Model): `Recipe`
    - Tabela: `recipe`
    - Atributos: `number`, `issue_date`, `valid_until`, `recipe_type`, `pdf_file`, `notes`

12. **Certificado (`certificates`)**
    - Branch / App: `certificates`
    - Classe (Model): `Certificate`
    - Tabela: `certificate`
    - Atributos: `number`, `issue_date`, `valid_until`, `pdf_file`
    - Relacionamentos: `vaccination` (OneToOneField -> `Vaccination`)

13. **Agendamento (`appointments`)**
    - Branch / App: `appointments`
    - Classe (Model): `Appointment`
    - Tabela: `appointment`
    - Atributos: `scheduled_at`, `appointment_type`, `status`, `notes`
    - Relacionamentos: `animal` (ForeignKey -> `Animal`), `veterinarian` (ForeignKey -> `Veterinarian`), `vaccination` (ManyToManyField -> `Vaccination`)

14. **Prescrição (`prescriptions`)**
    - Branch / App: `prescriptions`
    - Classe (Model): `Prescription`
    - Tabela: `prescription`
    - Atributos: `dosage`, `frequency`, `duration_days`, `instructions`
    - Relacionamentos: `appointment` (ForeignKey -> `Appointment`), `medication` (ForeignKey -> `Medication`), `recipe` (OneToOneField -> `Recipe`)
