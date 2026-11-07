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


### Convenções de Singular vs. Plural no Projeto

* **Nome da Branch no Git:** **SINGULAR** (ex: `person`, `manufacturer`, `tutor`, `vaccine`).
* **Pasta do App (`apps/` e `templates/`):** **PLURAL** (ex: `apps/persons`, `apps/manufacturers`, `templates/persons`, `templates/manufacturers`).
* **Nome da Classe (`models.py` e `forms.py`):** **SINGULAR** em `PascalCase` (ex: `Person`, `PersonForm`, `Manufacturer`, `ManufacturerForm`).
* **Funções no `views.py` e arquivos HTML em `templates/` (Depende da ação):**
  * **Adicionar, Editar e Excluir:** **SINGULAR** (ex: `add_manufacturer`, `edit_manufacturer`, `delete_manufacturer` e `add_manufacturer.html`).
  * **Listar:** **PLURAL** (ex: `list_manufacturers` e `list_manufacturers.html`).


### Convenções de Nomenclatura para Banco de Dados

* **Tabelas e Colunas:** Devem ser escritas em **inglês**, utilizando apenas letras minúsculas e separadas por sublinhado (`snake_case`).

| Regra                 | Padrão                        | Exemplo                     |
| :-------------------- | :---------------------------- | :-------------------------- |
| **Nome da Tabela**    | Inglês, `snake_case`          | `vaccination`               |
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

### Padronização dos 14 Apps, Branches, Models e Colunas

1. **Pessoa**
   - Branch no Git (Singular): `person`
   - Pasta do App (Plural): `persons`
   - Classe (Singular): `Person`
   - Atributos: `name`, `cpf`, `phone`, `email`

2. **Fabricante**
   - Branch no Git (Singular): `manufacturer`
   - Pasta do App (Plural): `manufacturers`
   - Classe (Singular): `Manufacturer`
   - Atributos: `name`, `cnpj`, `country`, `email`

3. **Tutor**
   - Branch no Git (Singular): `tutor`
   - Pasta do App (Plural): `tutors`
   - Classe (Singular): `Tutor` (herda de `Person`)
   - Atributos: `photo`

4. **Vacina**
   - Branch no Git (Singular): `vaccine`
   - Pasta do App (Plural): `vaccines`
   - Classe (Singular): `Vaccine`
   - Atributos: `name`, `description`, `required_doses`, `interval_days`, `price`, `is_active`, `package_insert`
   - Relacionamentos: `manufacturer` (ForeignKey -> `Manufacturer`)

5. **Veterinário**
   - Branch no Git (Singular): `veterinarian`
   - Pasta do App (Plural): `veterinarians`
   - Classe (Singular): `Veterinarian` (herda de `Person`)
   - Atributos: `crmv`, `is_active`

6. **Espécie**
   - Branch no Git (Singular): `species`
   - Pasta do App (Plural): `species`
   - Classe (Singular): `Species`
   - Atributos: `name`, `description`, `average_lifespan_years`, `is_active`
   - Relacionamentos: `vaccine` (ManyToManyField -> `Vaccine`)

7. **Animal**
   - Branch no Git (Singular): `animal`
   - Pasta do App (Plural): `animals`
   - Classe (Singular): `Animal`
   - Atributos: `name`, `birth_date`, `sex`, `weight_kg`, `microchip`, `photo`
   - Relacionamentos: `tutor` (ForeignKey -> `Tutor`), `species` (ForeignKey -> `Species`)

8. **Lote**
   - Branch no Git (Singular): `batch`
   - Pasta do App (Plural): `batches`
   - Classe (Singular): `Batch`
   - Atributos: `number`, `fabrication_date`, `expiration_date`, `quantity`
   - Relacionamentos: `vaccine` (ForeignKey -> `Vaccine`)

9. **Medicamento**
   - Branch no Git (Singular): `medication`
   - Pasta do App (Plural): `medications`
   - Classe (Singular): `Medication`
   - Atributos: `name`, `active_ingredient`, `administration_route`, `price`, `is_controlled`
   - Relacionamentos: `manufacturer` (ForeignKey -> `Manufacturer`)

10. **Vacinação**
    - Branch no Git (Singular): `vaccination`
    - Pasta do App (Plural): `vaccinations`
    - Classe (Singular): `Vaccination`
    - Atributos: `applied_at`, `dose_number`, `application_site`, `weight_kg`, `notes`
    - Relacionamentos: `batch` (ForeignKey -> `Batch`)

11. **Receita**
    - Branch no Git (Singular): `recipe`
    - Pasta do App (Plural): `recipes`
    - Classe (Singular): `Recipe`
    - Atributos: `number`, `issue_date`, `valid_until`, `recipe_type`, `pdf_file`, `notes`

12. **Certificado**
    - Branch no Git (Singular): `certificate`
    - Pasta do App (Plural): `certificates`
    - Classe (Singular): `Certificate`
    - Atributos: `number`, `issue_date`, `valid_until`, `pdf_file`
    - Relacionamentos: `vaccination` (OneToOneField -> `Vaccination`)

13. **Agendamento**
    - Branch no Git (Singular): `appointment`
    - Pasta do App (Plural): `appointments`
    - Classe (Singular): `Appointment`
    - Atributos: `scheduled_at`, `appointment_type`, `status`, `notes`
    - Relacionamentos: `animal` (ForeignKey -> `Animal`), `veterinarian` (ForeignKey -> `Veterinarian`), `vaccination` (ManyToManyField -> `Vaccination`)

14. **Prescrição**
    - Branch no Git (Singular): `prescription`
    - Pasta do App (Plural): `prescriptions`
    - Classe (Singular): `Prescription`
    - Atributos: `dosage`, `frequency`, `duration_days`, `instructions`
    - Relacionamentos: `appointment` (ForeignKey -> `Appointment`), `medication` (ForeignKey -> `Medication`), `recipe` (OneToOneField -> `Recipe`)
