from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class AumentarValoresApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)
        
        texto_label = Label(text='Cole o texto aqui:')
        layout.add_widget(texto_label)

        self.texto_textinput = TextInput(multiline=True)
        layout.add_widget(self.texto_textinput)

        aumento_label = Label(text='Valor para aumento:')
        layout.add_widget(aumento_label)

        self.aumento_textinput = TextInput()
        layout.add_widget(self.aumento_textinput)

        aplicar_button = Button(text='Aplicar Alterações')
        aplicar_button.bind(on_press=self.on_aplicar)
        layout.add_widget(aplicar_button)

        saida_label = Label(text='Texto alterado:')
        layout.add_widget(saida_label)

        self.saida_textinput = TextInput(multiline=True, readonly=True)
        layout.add_widget(self.saida_textinput)

        return layout

    def on_aplicar(self, instance):
        texto_original = self.texto_textinput.text
        aumento_str = self.aumento_textinput.text

        try:
            aumento = float(aumento_str)
        except ValueError:
            self.saida_textinput.text = 'Valor de aumento inválido.'
            return

        linhas = texto_original.split('\n')

        linhas_alteradas = []
        for linha in linhas:
            indice_simbolo = linha.find("•")
            if indice_simbolo != -1:
                parte_valor = linha[indice_simbolo + 1:].strip()
                try:
                    valor = float(parte_valor.replace(",", "").replace(".", "").replace(" ", ""))
                    novo_valor = valor + aumento
                    linha_alterada = linha[:indice_simbolo + 1] + " {:.2f}".format(novo_valor)
                    linhas_alteradas.append(linha_alterada)
                except ValueError:
                    linhas_alteradas.append(linha)
            else:
                linhas_alteradas.append(linha)

        texto_alterado = '\n'.join(linhas_alteradas)
        self.saida_textinput.text = texto_alterado + "\nAlterações aplicadas com sucesso."

if __name__ == '__main__':
    AumentarValoresApp().run()

