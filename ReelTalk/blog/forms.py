from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, InputRequired, NumberRange, Length

class ContatoForm(FlaskForm):

    nome_usuario = StringField(
        'Nome do Usuario', 
        validators=[
            DataRequired(message="O campo de nome do usuario é obrigatório."),
  
        ]
    )

    nome = StringField(
        'Nome',
        validators=[
            DataRequired(message="O campo nome é obrigatorio"),
            Length(min=2, max=50, message="O nome deve ter entre 2 e 50 caracteres.")
        ]
    )
    senha = StringField(
        "Senha",
        validators=[
            DataRequired(message="O campo de senha é obrigatorio"),
            Length(min=1)
        ]
    )
    email = StringField(
        'Email', 
        validators=[
            DataRequired(message="O campo de email é obrigatório."),
            Email(message="Digite um endereço de email válido.")
        ]
    )
    niver = DateField(
        'Niver', 
        format='%Y-%m-%d',
        validators=[
            DataRequired(message="O campo de idade é obrigatório.")
        ]
    )
    
    enviar = SubmitField('Enviar')