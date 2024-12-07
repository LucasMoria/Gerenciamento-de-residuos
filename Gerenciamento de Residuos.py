import tkinter as tk
from tkinter import ttk, messagebox

# Classe Residuo
class Residuo:
    TIPOS_VALIDOS = ["Plástico", "Vidro", "Metal", "Papel"]

    def __init__(self, tipo, quantidade):
        self.tipo = tipo
        self.quantidade = quantidade

    def validar_tipo(self):
        return self.tipo in Residuo.TIPOS_VALIDOS


# Função principal para a interface
def criar_interface():
    historico_residuos_validos = []
    historico_residuos_invalidos = []

    def registrar_residuo():
        tipo = tipo_var.get()
        quantidade = quantidade_var.get()

        if not quantidade.isdigit() or int(quantidade) <= 0:
            messagebox.showerror("Erro", "A quantidade deve ser um número inteiro positivo.")
            return

        quantidade = int(quantidade)
        residuo = Residuo(tipo, quantidade)

        if residuo.validar_tipo():
            historico_residuos_validos.append(residuo)
            mensagem = f"Resíduo válido registrado: {tipo}, {quantidade}kg."
        else:
            historico_residuos_invalidos.append(residuo)
            mensagem = f"Resíduo inválido registrado: {tipo}, {quantidade}kg."

        atualizar_historico()
        messagebox.showinfo("Registro de Resíduo", mensagem)

    def atualizar_historico():
        # Atualiza histórico de resíduos válidos
        for widget in validos_frame.winfo_children():
            widget.destroy()

        if not historico_residuos_validos:
            label = tk.Label(validos_frame, text="Nenhum resíduo válido registrado ainda.", anchor="w", justify="left")
            label.pack(fill="x", padx=5, pady=2)
        else:
            for residuo in historico_residuos_validos:
                label = tk.Label(validos_frame, text=f"{residuo.tipo}: {residuo.quantidade}kg", anchor="w", justify="left")
                label.pack(fill="x", padx=5, pady=2)

        # Atualiza histórico de resíduos inválidos
        for widget in invalidos_frame.winfo_children():
            widget.destroy()

        if not historico_residuos_invalidos:
            label = tk.Label(invalidos_frame, text="Nenhum resíduo inválido registrado ainda.", anchor="w", justify="left")
            label.pack(fill="x", padx=5, pady=2)
        else:
            for residuo in historico_residuos_invalidos:
                label = tk.Label(invalidos_frame, text=f"{residuo.tipo}: {residuo.quantidade}kg", anchor="w", justify="left")
                label.pack(fill="x", padx=5, pady=2)

    # Criando janela principal
    janela = tk.Tk()
    janela.title("Gerenciamento de Coleta Seletiva")
    janela.geometry("600x400")

    # Criando abas
    notebook = ttk.Notebook(janela)
    aba_registro = ttk.Frame(notebook)
    aba_validos = ttk.Frame(notebook)
    aba_invalidos = ttk.Frame(notebook)
    notebook.add(aba_registro, text="Registro")
    notebook.add(aba_validos, text="Histórico Válidos")
    notebook.add(aba_invalidos, text="Histórico Inválidos")
    notebook.pack(expand=1, fill="both")

    # Aba Registro
    registro_label = tk.Label(aba_registro, text="Registrar Resíduo", font=("Arial", 14))
    registro_label.pack(pady=10)

    tipo_label = tk.Label(aba_registro, text="Tipo de Resíduo:")
    tipo_label.pack(pady=5)
    tipo_var = tk.StringVar(value="Plástico")
    tipo_menu = ttk.Combobox(aba_registro, textvariable=tipo_var, values=["Plástico", "Vidro", "Metal", "Papel", "Orgânico"], state="readonly")
    tipo_menu.pack(pady=5)

    quantidade_label = tk.Label(aba_registro, text="Quantidade (kg):")
    quantidade_label.pack(pady=5)
    quantidade_var = tk.Entry(aba_registro)
    quantidade_var.pack(pady=5)

    registrar_btn = tk.Button(aba_registro, text="Registrar Resíduo", command=registrar_residuo)
    registrar_btn.pack(pady=10)

    # Aba Históricos
    # Históricos de resíduos válidos
    validos_label = tk.Label(aba_validos, text="Histórico de Resíduos Válidos", font=("Arial", 14))
    validos_label.pack(pady=10)
    validos_frame = tk.Frame(aba_validos)
    validos_frame.pack(expand=1, fill="both", padx=10, pady=5)

    # Históricos de resíduos inválidos
    invalidos_label = tk.Label(aba_invalidos, text="Histórico de Resíduos Inválidos", font=("Arial", 14))
    invalidos_label.pack(pady=10)
    invalidos_frame = tk.Frame(aba_invalidos)
    invalidos_frame.pack(expand=1, fill="both", padx=10, pady=5)

    # Iniciar a interface
    atualizar_historico()
    janela.mainloop()


# Executar a interface
criar_interface()
